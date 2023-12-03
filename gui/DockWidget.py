import typing, json, pandas as pd
from qtpy.QtCore import Signal, Slot
from PySide6.QtCore import Qt, QFile, QIODevice, QUrl, QModelIndex, QItemSelectionModel
from PySide6.QtWidgets import QWidget, QDockWidget, QHeaderView, QStyledItemDelegate
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

from models import TrackPointsModel, JsonTreeModel
from abstracts import AbstractModelWidget
from StatusMessage import StatusMessage
from dto import FileDataDTO
from delegates import MapSettingsDelegate
from trackStatistics import StatisticsModel

from gui.map_dock_ui import Ui_DockWidget as mapDock
from gui.statistics_dock_ui import Ui_DockWidget as statisticsDock
from gui.file_info_dock_ui import Ui_DockWidget as fileInfoDock
from gui.filter_dock_ui import Ui_DockWidget as filterDock
from gui.processing_dock_ui import Ui_DockWidget as processingDock

class ProcessingDockWidget(AbstractModelWidget, QDockWidget, processingDock):

    def _setupUi(self):
        self.buttonCalculateSpeed.clicked.connect(self._calculateSpeed)
        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))

    def _calculateSpeed(self):
        pass

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
        for item in self.statisticsModel.iterateIndexes():
            if item.dtoAttribute is None or item.dtoAttribute == 'sensorState':
                item.min = '-'
                item.max = '-'
                item.avg = '-'
                continue
            min = self.model.allTrackPoints[item.dtoAttribute].min()
            max = self.model.allTrackPoints[item.dtoAttribute].max()
            mean = self.model.allTrackPoints[item.dtoAttribute].mean()
            item.min = float(min) if not pd.isna(min) else '-'
            item.max = float(max) if not pd.isna(max) else '-'
            item.avg = float(mean) if not pd.isna(mean) else '-'
        self.statisticsModel.endResetModel()
        self.statusMessage.emit(None)

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
        if self.model.rowCount() <= 0: return
        coordinates = []
        for a, b in zip(self.model.allTrackPoints['longitude'], self.model.allTrackPoints['latitude']):
            if pd.notna(a) and pd.notna(b):
                coordinates.append([a,b])
        return coordinates

    def _getTrimmedTrackPointsCoordinates(self):
        filtered = self.model.allTrackPoints.loc[self.model.trimmerInterval.min:self.model.trimmerInterval.max, ['longitude', 'latitude']]
        coordinates = []
        for a, b in zip(filtered['longitude'], filtered['latitude']):
            if pd.notna(a) and pd.notna(b):
                coordinates.append([a,b])
        return coordinates