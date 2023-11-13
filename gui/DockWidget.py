import typing, os, json
from qtpy.QtCore import Signal, Slot
from tcxmodel import TrackPointsModel, TCXLoader, TrackPointModel

from gui.map_dock_ui import Ui_DockWidget as mapDock
from gui.statistics_dock_ui import Ui_DockWidget as statisticsDock
from gui.file_info_dock_ui import Ui_DockWidget as fileInfoDock
from gui.filter_dock_ui import Ui_DockWidget as filterDock
from gui.processing_dock_ui import Ui_DockWidget as processingDock
from gui.marking_dock_ui import Ui_DockWidget as markingDock
from abc import ABC, abstractmethod

from PySide6.QtGui import QPalette
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
    def _setupUi(self):
        self.markStatSelColor.clicked.connect(self._markStationarySelectColor)
        self.pushButtonMarkStat.clicked.connect(lambda: self.model.markStationary(self.spinBoxMarkStatSelectRange.value()))

    def _markStationarySelectColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            pal = QPalette()
            pal.setColor(QPalette.ColorRole.Button, color)
            self.markStatSelColor.setPalette(pal)


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
        pass



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
