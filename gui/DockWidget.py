import typing, os, json, re
from qtpy.QtCore import Signal, Slot
from tcxmodel import TrackPointsModel, TCXLoader, TrackPointModel

from gui.map_dock_ui import Ui_DockWidget as mapDock
from gui.statistics_dock_ui import Ui_DockWidget as statisticsDock
from gui.file_info_dock_ui import Ui_DockWidget as fileInfoDock
from gui.filter_dock_ui import Ui_DockWidget as filterDock
from gui.processing_dock_ui import Ui_DockWidget as processingDock
from gui.marking_dock_ui import Ui_DockWidget as markingDock
from abc import ABC, abstractmethod

from PySide6.QtGui import QPalette, QColor, QColorConstants
from PySide6.QtCore import Qt, QFile, QIODevice, QUrl, QModelIndex, QItemSelectionModel
from PySide6.QtWidgets import QWidget, QDockWidget, QColorDialog
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

class AbstractModelDockWidget():
    startProcessing = Signal() #before processing data (to clear the status maybe)
    statusMessage = Signal(str) #sending messages for status bar
    progressUpdate = Signal(int) #incrementing the progress bar
    finishedProcessing = Signal() #processing finished (for resetting the status bar maybe)

    def __init__(self, parent: typing.Optional[QWidget] = ..., model:typing.Optional[TrackPointsModel]=...) -> None:
        super().__init__(parent)
        self.model = model
        self.setupUi(self)
        self._setupUi()

    @abstractmethod
    def _setupUi(self):
        pass



class MarkingDockWidget(AbstractModelDockWidget, QDockWidget, markingDock):
    colorCustomMarking:QColor = QColorConstants.Red
    colorStationaryMarking: QColor = QColorConstants.Yellow
    pattern = re.compile(r'([<|>|=|\s]+)\s*(\d*[.|,]?\d+)\s*([&|]{1})*\s*')
    marker = {
        "indexes": [],
        "color": QColor
    }
    markers = []
    def _setupUi(self):
        self._setColor(self.pushStatMarkSelColor, self.colorStationaryMarking)
        self._setColor(self.pushCustomMarkSelColor, self.colorCustomMarking)

        self.pushCustomMark.clicked.connect(self._onCustomMarkButton)
        self.pushCustomMarkClear.clicked.connect(lambda: self._clearMarker('custom'))
        self.pushCustomMarkSelColor.clicked.connect(lambda: self._setColor(self.pushCustomMarkSelColor))

        self.pushStatMark.clicked.connect(lambda: self._markStationary(self.spinBoxMarkStatSelectRange.value()))
        self.pushStatMarkClear.clicked.connect(lambda: self._clearMarker('stationary'))
        self.pushStatMarkSelColor.clicked.connect(lambda: self._setColor(self.pushStatMarkSelColor))



        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))

    def _setColor(self, control, color = None):
        if color is None:
            color = QColorDialog.getColor()
        if color.isValid():
            pal = QPalette()
            pal.setColor(QPalette.ColorRole.Button, color)
            control.setPalette(pal)

    def _markStationary(self, val):
        indexes = []
        prevItem = None
        color = self.pushStatMarkSelColor.palette().button().color()
        for index, item in enumerate(self.model.trackPoints):
            if item.data['distance'] is not None and prevItem.data['distance'] is not None and abs(prevItem.data['distance'] - item.data['distance']) <= val:
                indexes.append(index)
                indexes.append(index-1)
            prevItem = item
        self.model.addMarker('stationary', indexes, color)

    def _clearMarker(self, name):
        self.model.clearMarker(name)

    def _onCustomMarkButton(self):
        data = {
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
        color = self.pushCustomMarkSelColor.palette().button().color()
        try:
            indexes = []
            expression = self._createExpression(data)
            if len(expression) == 0:
                self._lastFindDataExpression = None
                return
            for index, item in enumerate(self.model.trackPoints):
                if eval(expression):
                    indexes.append(index)
        except Exception as e:
            self._lastFindDataExpression = None
            self.statusMessage.emit(f"Syntax error (syntax: <=,<,<>><value><&,|>)")
        self._lastFindDataExpression = data
        self.model.addMarker('custom', indexes, color)
        pass

    def _createExpression(self, findBy):
        # exp = self._createExpression(findBy)
        expression = []
        for key, value in findBy.items():
            if value is not None and value.strip() != "":
                expression.append(self._addKey(key, self.pattern.findall(value)))

        return ' or '.join(expression)

    def _addKey(self, key:str, expression: list[tuple]):
        result = ''
        key = 'item.data["'+key+'"]'
        for item in expression:
            item = [key] + [(val.replace('&', 'and').replace('|', 'or').replace('=', '==')) for val in item]
            result += ' '.join(item) + ' '
        return key + ' is not None and ' + result.strip()

class ProcessingDockWidget(AbstractModelDockWidget, QDockWidget, processingDock):

    def _setupUi(self):
        self.buttonCalculateSpeed.clicked.connect(self._calculateSpeed)
        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))

    def _calculateSpeed(self):
        self.statusMessage.emit('Calculating speed...')
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
        self.statusMessage.emit('')



class FilterDockWidget(AbstractModelDockWidget, QDockWidget, filterDock):
    def _setupUi(self):
        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))


class FileInfoDockWidget(AbstractModelDockWidget, QDockWidget, fileInfoDock):

    def __init__(self, parent: typing.Optional[QWidget] = ..., tcxLoader:typing.Optional[TCXLoader]=...):
        super().__init__(parent, None)
        tcxLoader.fileDataChanged.connect(self._loadInfo)

    @Slot()
    def _loadInfo(self, activityData):
        self.statusMessage.emit('Loading file ...')
        self.inputFilePath.setText(str(activityData['file']))
        self.inputNotes.setText(activityData['notes'])
        self.inputId.setText(activityData['id'])
        self.inputSport.setText(activityData['type'])
        self.inputLaps.setText(str(activityData['lapsCount']))
        self.inputTrackPoints.setText(str(activityData['trackPointsCount']))



class StatisticsDockWidget(AbstractModelDockWidget, QDockWidget, statisticsDock):

    @Slot()
    def calculateStatistics(self):
        self.statusMessage.emit('Calculating statistics...')
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
                val, colName = self.model.dataByIndex(row, col, Qt.ItemDataRole.EditRole)
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
        self.statusMessage.emit('')

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



class MapDockWidget(AbstractModelDockWidget, QDockWidget, mapDock):

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
