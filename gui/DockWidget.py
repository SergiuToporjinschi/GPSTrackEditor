import typing, json, re
from qtpy.QtCore import Signal, Slot
from PySide6.QtGui import QPalette, QColor, QColorConstants, QMouseEvent, QAction, QContextMenuEvent
from PySide6.QtCore import Qt, QFile, QIODevice, QUrl, QModelIndex, QItemSelectionModel, QEvent
from PySide6.QtWidgets import QWidget, QDockWidget, QColorDialog, QHeaderView, QStyledItemDelegate,  QMenu
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

from models import TrackPointsModel, TCXRowModel, JsonTreeModel
from abstracts import AbstractModelWidget, AbstractWidgetMaximizeable
from StatusMessage import StatusMessage
from dto import FileDataDTO, MarkerDto
from delegates import MapSettingsDelegate
from trackStatistics import StatisticsDto, StatisticsModel

from gui.map_dock_ui import Ui_DockWidget as mapDock
from gui.statistics_dock_ui import Ui_DockWidget as statisticsDock
from gui.file_info_dock_ui import Ui_DockWidget as fileInfoDock
from gui.filter_dock_ui import Ui_DockWidget as filterDock
from gui.processing_dock_ui import Ui_DockWidget as processingDock
from gui.marking_dock_ui import Ui_DockWidget as markingDock


class MarkingDockWidget(AbstractModelWidget, AbstractWidgetMaximizeable, markingDock):
    colorCustomMarking:QColor = QColorConstants.Red
    colorStationaryMarking: QColor = QColorConstants.Yellow
    pattern = re.compile(r'([<|>|=|\s]+)\s*(\d*[.|,]?\d+)\s*([&|]{1})*\s*')
    markers : [MarkerDto] = []

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

    def _markStationary(self, marker: typing.Optional[MarkerDto] = None):
        self.statusMessage.emit(StatusMessage('Marking...'))
        self.updateProgress.emit(0)
        color = self.pushStatMarkSelColor.palette().button().color()
        tolerance = self.spinBoxMarkStatTolerance.value()
        marker = MarkerDto('stationary', [], color, tolerance) if not isinstance(marker, MarkerDto) or marker is None else marker
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

    def _onCustomMarkButton(self, marker: typing.Optional[MarkerDto] = None):
        self.statusMessage.emit(StatusMessage('Marking...'))
        marker = self._buildCustomMarker() if not isinstance(marker, MarkerDto) or marker is None else marker
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
        return MarkerDto('custom', [], color, ' or '.join(expression))

    def _buildCustomMarkerKey(self, key:str, expression: list[tuple]):
        result = ''
        # key = 'item.data["'+key+'"]'
        key = f'item.getValueByColName("{key}")'
        for item in expression:
            item = [key] + [(val.replace('&', 'and').replace('|', 'or').replace('=', '==')) for val in item]
            result += ' '.join(item) + ' '
        return key + ' is not None and ' + result.strip()

    def _applyMarker(self, marker: MarkerDto):
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
        self.model.beginResetModel()
        self.model.sortBy('time', Qt.SortOrder.AscendingOrder)
        prevDistance = None
        for item in self.model.iterateAllTracks():
            if prevDistance is not None and item is not None and item.distance is not None:
                newSpeed = ((item.distance - prevDistance) * 360) / 100
            else:
                newSpeed = 0
            prevDistance = item.distance
            item.calculatedSpeed = newSpeed
        self.model.endResetModel()
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

    class RightAlignmentDelegate(QStyledItemDelegate):
        def initStyleOption(self, option, index):
            super().initStyleOption(option, index)
            option.displayAlignment = Qt.AlignmentFlag.AlignRight

    def _setupUi(self):
        self.statisticsModel = StatisticsModel()
        self.tableStatistics.setModel(self.statisticsModel)
        self.tableStatistics.setItemDelegate(StatisticsDockWidget.RightAlignmentDelegate())
        self.statisticsModel.modelReset.connect(self.tableStatistics.resizeColumnsToContents)
        self.tableStatistics.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    @Slot()
    def calculateStatistics(self):
        self.statusMessage.emit(StatusMessage('Calculating statistics...'))
        self.statisticsModel.beginResetModel()
        for dataItem in self.model.iterateTrimmedTracks():
            for item in self.statisticsModel.iterateIndexes():
                if item.dataType is str: continue
                if item.dtoAttribute is None:
                    # eval(f'self.{item.func}(dataItem, item)')
                    continue
                val = getattr(dataItem, item.dtoAttribute)
                if val is None:
                    item.missing = item.missing + 1
                    continue
                if val is None or item.min is None or item.min > val: item.min = val
                if val is None or item.max is None or item.max < val: item.max = val
                item.avg  = (item.min + item.max) / 2
        self.statisticsModel.endResetModel()
        self.statusMessage.emit(None)

    def toKm(self, currentValueItem:StatisticsDto, modelItem:TCXRowModel):
        pass
    def findMax(self, currentValueItem:StatisticsDto, modelItem:TCXRowModel):
        pass
    def findAvg(self, currentValueItem:StatisticsDto, modelItem:TCXRowModel):
        pass
    def findMissing(self, currentValueItem:StatisticsDto, modelItem:TCXRowModel):
        pass

class MapDockWidget(AbstractModelWidget, QDockWidget, mapDock):
    configChanged = Signal(str)        # map configuration changes, updates map
    mainSeriesChanged = Signal(str)    # main series has changed in table, updates current main track on map
    currentPositionPoint = Signal(str) # current position changed on table, updates current position on map
    trimmedSeriesChanged = Signal(str) # trimmed series has changed in table, updates current trimmed track on map

    def __init__(self, parent: QWidget | None = ..., model: TrackPointsModel | None = ..., selectionModel: QItemSelectionModel | None = ...) -> None:
        self.tableSelectionModel = selectionModel
        super().__init__(parent, model)

    def _setupUi(self):
        self.model.mainSeriesLengthChanged.connect(self._loadMainTrack)
        self.tableSelectionModel.currentRowChanged.connect(self._sendMarkPoint)
        self.model.trimRangeChanged.connect(self._loadTrimmedTrack)

        # self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ":/resources/index.html"))
        self.file_path = "E:/IOT/Projects/Python/GPSTrackEditor/resources/index.html"

        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)

        self.channel = QWebChannel()
        self.channel.registerObject("backEnd", self)

        self.browser.page().setWebChannel(self.channel)
        self.browser.setUrl(QUrl.fromLocalFile(self.file_path))

        # self.browser.setHtml(self._getResourceContent(':/resources/index.html'))
        self.browser.show()

        # settings tab ------------------------------------------------
        self.treeViewMapPropertiesModel = JsonTreeModel()
        self.treeViewMapPropertiesModel.load(json.loads(self._getResourceContent(':/resources/mapDefaultProperties.json')))

        self.treeViewMapProperties.setModel(self.treeViewMapPropertiesModel)
        self.treeViewMapProperties.setItemDelegate(MapSettingsDelegate())
        self.treeViewMapProperties.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.treeViewMapProperties.expandAll()
        self.treeViewMapPropertiesModel.configChanged.connect(self.configChanged)

    def _loadTrimmedTrack(self):
        self.trimmedSeriesChanged.emit(json.dumps(self._getTrimmedTrackPointsCoordinates()))

    def _loadMainTrack(self):
        self.mainSeriesChanged.emit(json.dumps(self._getAllTrackPointsCoordinates()))

    def _sendMarkPoint(self, new:QModelIndex, old:QModelIndex):
        item = self.model.getTrimmedDataItem(new.row())
        self.currentPositionPoint.emit(json.dumps([item.longitude, item.latitude]))

    def _getResourceContent(self, resourceFilePath: str):
        htmlContent = ""
        html_resource = QFile(resourceFilePath)
        if html_resource.open(QIODevice.ReadOnly | QIODevice.Text):
            html_content = html_resource.readAll().data().decode('utf-8')
            htmlContent = html_content
            html_resource.close()
        return htmlContent

    def _getAllTrackPointsCoordinates(self):
        coordinates = []
        for item in self.model.iterateAllTracks():
            if item.longitude is not None and item.latitude is not None:
                coordinates.append([item.longitude, item.latitude])
        return coordinates

    def _getTrimmedTrackPointsCoordinates(self):
        coordinates = []
        for item in self.model.iterateTrimmedTracks():
            if item.longitude is not None and item.latitude is not None:
                coordinates.append([item.longitude, item.latitude])
        return coordinates