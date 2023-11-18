import typing, os, json, re
from qtpy.QtCore import Signal, Slot
from PySide6.QtGui import QPalette, QColor, QColorConstants
from PySide6.QtCore import Qt, QFile, QIODevice, QUrl, QModelIndex, QItemSelectionModel
from PySide6.QtWidgets import QWidget, QDockWidget, QColorDialog
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

from TCXModel import TrackPointsModel, Marker
from AbstractModelWidget import AbstractModelWidget
from StatusBar import StatusMessage
from TrackDataDTO import FileDataDTO

from gui.map_dock_ui import Ui_DockWidget as mapDock
from gui.statistics_dock_ui import Ui_DockWidget as statisticsDock
from gui.file_info_dock_ui import Ui_DockWidget as fileInfoDock
from gui.filter_dock_ui import Ui_DockWidget as filterDock
from gui.processing_dock_ui import Ui_DockWidget as processingDock
from gui.marking_dock_ui import Ui_DockWidget as markingDock



class MarkingDockWidget(AbstractModelWidget, QDockWidget, markingDock):
    colorCustomMarking:QColor = QColorConstants.Red
    colorStationaryMarking: QColor = QColorConstants.Yellow
    pattern = re.compile(r'([<|>|=|\s]+)\s*(\d*[.|,]?\d+)\s*([&|]{1})*\s*')
    markers : [Marker] = []
    def _setupUi(self):
        self._setColor(self.pushStatMarkSelColor, self.colorStationaryMarking)
        self._setColor(self.pushCustomMarkSelColor, self.colorCustomMarking)

        self.pushCustomMark.clicked.connect(self._onCustomMarkButton)
        self.pushCustomMarkClear.clicked.connect(lambda: self._clearMarker('custom'))
        self.pushCustomMarkSelColor.clicked.connect(lambda: self._setColor(self.pushCustomMarkSelColor))

        self.pushStatMark.clicked.connect(self._markStationary)
        self.pushStatMarkClear.clicked.connect(lambda: self._clearMarker('stationary'))
        self.pushStatMarkSelColor.clicked.connect(lambda: self._setColor(self.pushStatMarkSelColor))

        self.model.contentChanged.connect(self._refreshMarkers)
        self.model.trimRangeChanged.connect(self._refreshMarkers)

        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))
        pass

    def _setColor(self, control, color = None):
        if color is None:
            color = QColorDialog.getColor()
        if color.isValid():
            pal = QPalette()
            pal.setColor(QPalette.ColorRole.Button, color)
            control.setPalette(pal)
        pass

    def _markStationary(self, marker: typing.Optional[Marker] = None):
        self.statusMessage.emit(StatusMessage('Marking...'))
        self.updateProgress.emit(0)
        color = self.pushStatMarkSelColor.palette().button().color()
        tolerance = self.spinBoxMarkStatTolerance.value()
        marker = Marker('stationary', [], color, tolerance) if not isinstance(marker, Marker) or marker is None else marker
        marker.indexes.clear()
        prevItem = None
        trackPointsCount = len(self.model.allTrackPoints)
        for index, item in enumerate(self.model.allTrackPoints):
            self.updateProgress.emit(int((index + 1)/trackPointsCount))
            self.statusMessage.emit(StatusMessage(f'Marking... index {index}'))
            dist = item.getValueByColName('distance')
            prevDist = prevItem.getValueByColName('distance') if prevItem is not None else None
            if dist is not None and prevDist is not None and abs(prevDist - dist) <= marker.expression:
                marker.indexes.append(index)
                marker.indexes.append(index - 1)
            prevItem = item
        self._applyMarker(marker)
        self.updateProgress.emit(0)
        self.statusMessage.emit(None)
        pass

    def _clearMarker(self, name):
        self.markers[:] = [maker for maker in self.markers if maker.name != name]
        self.model.clearMarker(name)
        pass

    def _onCustomMarkButton(self, marker: typing.Optional[Marker] = None):
        self.statusMessage.emit(StatusMessage('Marking...'))
        marker = self._buildCustomMarker() if not isinstance(marker, Marker) or marker is None else marker
        try:
            marker.indexes = []
            trackPointsCount = len(self.model.allTrackPoints)
            for index, item in enumerate(self.model.allTrackPoints):
                self.updateProgress.emit(int((index + 1)/trackPointsCount))
                if eval(marker.expression):
                    marker.indexes.append(index)
            self.updateProgress.emit(0)
        except Exception:
            self._lastFindDataExpression = None
            self.statusMessage.emit(f"Syntax error (syntax: <=,<,<>><value><&,|>)")
        self._applyMarker(marker)
        self.statusMessage.emit(None)
        self.updateProgress.emit(0)
        pass

    def _buildCustomMarker(self):
        findBy = {
            "time": self.editFindByTime.text(),
            "latitude": self.editFindByLatitude.text(),
            "longitude": self.editFindByLongitude.text(),
            "distance": self.editFindByDistance.text(),
            "calculatedDistance": self.editFindByCalculatedDistance.text(),
            "altitude": self.editFindByAltitude.text(),
            "speed": self.editFindBySpeed.text(),
            "calculatedSpeed": self.editFindByCalculatedSpeed.text(),
            "hartRate": self.editFindByHartRate.text(),
            "sensorState": self.editFindBySensorState.text()
        }
        expression = []
        for key, value in findBy.items():
            if value is not None and value.strip() != "":
                expression.append(self._buildCustomMarkerKey(key, self.pattern.findall(value)))
        color = self.pushCustomMarkSelColor.palette().button().color()
        return Marker('custom', [], color, ' or '.join(expression))

    def _buildCustomMarkerKey(self, key:str, expression: list[tuple]):
        result = ''
        # key = 'item.data["'+key+'"]'
        key = f'item.getValueByColName("{key}")'
        for item in expression:
            item = [key] + [(val.replace('&', 'and').replace('|', 'or').replace('=', '==')) for val in item]
            result += ' '.join(item) + ' '
        return key + ' is not None and ' + result.strip()

    def _applyMarker(self, marker: Marker):
        if marker not in self.markers:
            self.markers.append(marker)
        self.model.addMarker(marker)
        pass

    def _refreshMarkers(self):
        self.model.clearAllMarker()

        for marker in self.markers:
            if marker.name == 'custom':
                self._onCustomMarkButton(marker)
            elif marker.name == 'stationary':
                self._markStationary(marker)
            self.model.addMarker(marker)
        pass



class ProcessingDockWidget(AbstractModelWidget, QDockWidget, processingDock):

    def _setupUi(self):
        self.buttonCalculateSpeed.clicked.connect(self._calculateSpeed)
        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))

    def _calculateSpeed(self):
        self.statusMessage.emit(StatusMessage('Calculating speed...'))
        self.model.sortBy('time', Qt.SortOrder.AscendingOrder)
        self.model.setDataByColumnName(0, 'calculatedSpeed', 0, Qt.ItemDataRole.EditRole)
        for row in range(1, self.model.rowCount()):
            prevData = self.model.dataByColName(row-1, 'distance')
            data = self.model.dataByColName(row, 'distance')
            if prevData is not None and data is not None:
                newVal = ((data - prevData) * 360) / 100
            else:
                newVal = 0
            self.model.setDataByColumnName(row, 'calculatedSpeed', newVal, Qt.ItemDataRole.EditRole)
        self.statusMessage.emit(None)



class FilterDockWidget(AbstractModelWidget, QDockWidget, filterDock):
    def _setupUi(self):
        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))



class FileInfoDockWidget(AbstractModelWidget, QDockWidget, fileInfoDock):

    def __init__(self, parent: typing.Optional[QWidget] = ...):
        super().__init__(parent, None)
        # tcxLoader.fileDataChanged.connect(self._loadInfo)

    @Slot()
    def loadInfo(self, activityData:FileDataDTO):
        self.inputFilePath.setText(activityData.filePath)
        self.inputNotes.setText(activityData.notes)
        self.inputId.setText(activityData.id)
        self.inputSport.setText(activityData.activityType)
        self.inputLaps.setText(str(activityData.lapsCount))
        self.inputTrackPoints.setText(str(activityData.trackPointsCount))



class StatisticsDockWidget(AbstractModelWidget, QDockWidget, statisticsDock):

    @Slot()
    def calculateStatistics(self):
        self.statusMessage.emit(StatusMessage('Calculating statistics...'))
        values = {
            "latitude": {"max": 0,"min": 0,"missing": 0},
            "longitude": {"max": 0,"min": 0,"missing": 0},
            "altitude": {"max": 0,"min": 0,"missing": 0},
            "hartRate": {"max": 0,"min": 0,"missing": 0},
            "distance": {"max": 0,"min": 0,"missing": 0},
            "calculatedDistance": {"max": 0,"min": 0,"missing": 0},
            "speed": {"max": 0,"min": 0,"missing": 0},
            "calculatedSpeed": {"max": 0,"min": 0,"missing": 0}
        }
        for row in range(0, self.model.rowCount()):
            for col in range(0, self.model.columnCount()):
                val, colName = self.model.dataAndAttributeByIndex(row, col, Qt.ItemDataRole.EditRole)
                ent = values.get(colName)
                if val is None:
                    ent['missing'] = ent['missing'] + 1
                elif ent is not None:
                    ent['max'] = val if val > ent['max'] else ent['max']
                    ent['min'] = val if val < ent['min'] else ent['min']

        self._updateGroup("speed", values, 12, [('MPH',1),('KMPH',100)])
        self._updateGroup("calculatedSpeed", values, 16, [('MPH',1),('KMPH',100)])
        self._updateGroup("distance", values, 16, [('M',1),('KM',100)])
        self._updateGroup("calculatedDistance", values, 16, [('M',1),('KM',100)])
        self._updateGroup("hartRate", values, 2)
        self._updateGroup("longitude", values, 8)
        self._updateGroup("latitude", values, 8)
        self._updateGroup("altitude", values, 3)
        self.statusMessage.emit(None)



    def _updateGroup(self, name:str, values:dict, dec:int, sufix:[tuple] = [("",1)]):
        ent = values.get(name)
        fieldName = name[0].upper() + name[1:]
        for item in sufix:
            suf, div = item
            vars(self)['label'+fieldName+'Min'+suf].setText(f'{ent.get("min")/div:.{dec}f}')
            vars(self)['label'+fieldName+'Max'+suf].setText(f'{ent.get("max")/div:.{dec}f}')
            vars(self)['label'+fieldName+'Avg'+suf].setText(f'{(ent.get("max") + ent.get("min"))/div / 2:.{dec}f}')

        missField = vars(self)['label'+fieldName+'Missing']
        missVal = str(ent.get("missing")) if ent.get("missing") > 0 else "None"
        missField.setText(missVal)
        if missVal != 'None':
            missField.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            missField.setStyleSheet("")



class MapDockWidget(AbstractModelWidget, QDockWidget, mapDock):

    mainSeriesChanged = Signal(str)
    markPoint = Signal(str)

    def __init__(self, parent: QWidget | None = ..., model: TrackPointsModel | None = ..., selectionModel: QItemSelectionModel | None = ...) -> None:
        self.tableSelectionModel = selectionModel
        super().__init__(parent, model)

    def _setupUi(self):
        self.model.mainSeriesLengthChanged.connect(self._loadMainTrack)
        self.tableSelectionModel.currentRowChanged.connect(self._sendMarkPoint)

        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ":/resources/index.html"))

        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)

        self.channel = QWebChannel()
        self.channel.registerObject("backEnd", self)

        self.browser.page().setWebChannel(self.channel)
        # self.browser.setUrl(QUrl.fromLocalFile(self.file_path))
        self.browser.setUrl(QUrl.fromLocalFile(":/resources/index.html"))
        self.browser.setHtml(self._getHTML())
        self.browser.show()

    def _loadMainTrack(self):
        self.mainSeriesChanged.emit(json.dumps(self._getCoordinates()))

    def _sendMarkPoint(self, new:QModelIndex, old:QModelIndex):
        (longitude, latitude) = self.model.dataByColNames(new.row(), ('longitude', 'latitude'))
        self.markPoint.emit(json.dumps([longitude, latitude]))

    def _getHTML(self):
        htmlContent = ""
        html_resource = QFile(':/resources/index.html')  # Assuming 'index.html' is the file in your qrc
        if html_resource.open(QIODevice.ReadOnly | QIODevice.Text):
            html_content = html_resource.readAll().data().decode('utf-8')
            htmlContent = html_content
            html_resource.close()
        return htmlContent

    def _getCoordinates(self):
        coordinates = []
        for row in range(0, self.model.rowCount()):
            (longitude, latitude) = self.model.dataByColNames(row, ('longitude', 'latitude'))
            if longitude is not None and latitude is not None:
                coordinates.append([longitude, latitude])
        return coordinates
