from PyQt6.QtWidgets import QFileDialog, QMainWindow, QApplication, QAbstractItemDelegate, QColorDialog, QStyle
from PyQt6.QtCore import Qt, QObject, QTimer, QUrl, QItemSelection, QModelIndex
from PyQt6.QtGui import QPalette, QColor, QColorConstants
from tcxmodel import TrackPointsModel, TrackPointModel, TCXLoader
from gui.main_remaster_ui import Ui_MainWindow

from internalWidgets import StatusBarGroupBox
from PyQt6 import QtWebEngineWidgets, QtWebEngineCore
import sys
import resources.resource
from internalWidgets import MapWindow

sys.argv.append("--disable-web-security")
class itDel(QAbstractItemDelegate):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__()
    pass

class mainGUI(QMainWindow, Ui_MainWindow):
    fileName = ''
    tcx = None

    def __init__(self, app:QApplication):
        super().__init__()
        self.setupUi(self)

        self.buttonCalculateSpeed.clicked.connect(self._calculateSpeed)
        self.actionSave.triggered.connect(self._onSaveFile)
        self.actionOpen.triggered.connect(self._onOpenFile)
        self.actionExit.triggered.connect(self._onExit)
        self.actionClear.triggered.connect(self._onClear)

        self.app = app
        self.model = TrackPointsModel(palette=app.palette())
        self.model.rowCountChanged.connect(lambda x: self.slider.setRange(1 if x!=0 else 0, x))
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
        self._applyDelegates()
        self.progress = StatusBarGroupBox(parent=self.statusbar)
        self.statusbar.addPermanentWidget(self.progress, 1)
        self._noDataDisable(False)
        self.pushButtonFind.clicked.connect(self._onFindButton)
        self.pushButtonFindClear.clicked.connect(self._onFindButton)

        self.markStatSelColor.clicked.connect(self._markStationarySelectColor)
        self.pushButtonMarkStat.clicked.connect(lambda: self.model.markStationary(self.spinBoxMarkStatSelectRange.value()))

        self.timerClear =  QTimer(self)
        self.timerClear.setInterval(5000)
        self.timerClear.setSingleShot(False)
        self.timerClear.setTimerType(Qt.TimerType.CoarseTimer)
        self.timerClear.start()
        self._connectSignals()
        self.tabifyDockWidget(self.dockWidgetFind, self.dockWidgetProcessing)
        self.tabifyDockWidget(self.dockWidgetFind, self.dockWidgetStatistics)
        self.tabifyDockWidget(self.dockWidgetFind, self.dockWidgetFiltering)
        self.tabifyDockWidget(self.dockWidgetFind, self.dockWidgetFileInfo)
        self._openMap()
        self.tableView.selectionModel().currentRowChanged.connect(self._selectionChanged)

        # self.dockWidgetStatistics.titleBarWidget().palette().setColor
    def _selectionChanged(self, new:QModelIndex,old:QModelIndex):
        longIndex = self.model.index(new.row(), TrackPointModel.nameToIndex('longitude'))
        latIndex = self.model.index(new.row(), TrackPointModel.nameToIndex('latitude'))
        long = self.model.data(longIndex,  Qt.ItemDataRole.EditRole)
        lat = self.model.data(latIndex,  Qt.ItemDataRole.EditRole)
        self.mapWindow.sendMarkPoint([long, lat])

    def _onFindButton(self):
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
        self.model.findByExpression(data)

    def _openMap(self):
        if hasattr(self,"mapWindow") is False or self.mapWindow is None:
            self.mapWindow = MapWindow(parent=self)
            self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.mapWindow)
        else:
            self.mapWindow.setVisible(True)
        pass

    def _markStationarySelectColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            pal = QPalette()
            pal.setColor(QPalette.ColorRole.Button, color)
            self.markStatSelColor.setPalette(pal)

    def _connectSignals(self):
        # self.slider.selectedIntervalChanged.connect(lambda val: print("selectedIntervalChanged", val))
        self.slider.selectedIntervalChanged.connect(self.model.filterByRowNumbers)
        self.slider.selectionCountChanged.connect(self.progress.updateSelection)
        self.slider.selectedIntervalChanged.connect(lambda val: self._noDataDisable(val[1]-val[0]>0))
        self.model.allTrackPointsCountChanged.connect(self.progress.updateTackPoints)
        self.timerClear.timeout.connect(lambda: self.progress.updateTimerMessage.emit(''))
        self.timerClear.timeout.connect(lambda: self.progress.updateProgress.emit(0))
        self.model.statusMessage.connect(self.progress.updateTimerMessage)
        self.editFindBySpeed.textChanged.connect(lambda x: print(x))
        self.model.workingProgress.connect(self.progress.updateProgress)
        #debug
        # self.slider.selectedMaxIntervalChanged.connect(lambda val: print("maxChanged", val))
        # self.slider.selectedMinIntervalChanged.connect(lambda val: print("minChanged", val))

    def _noDataDisable(self, enabled:bool):
        self.slider.setEnabled(enabled)
        # self.tabProcessing.setEnabled(enabled)
        # self.tabFiltering.setEnabled(enabled)

    def _onOpenFile(self):
        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'All Files (*.tcx)')
        if not file_name:
            return
        self.fileName = file_name
        self.labelFilePath.setText(file_name)

        tcxLoader = TCXLoader(self.fileName)
        tcxLoader.workingProgress.connect(self.progress.updateProgress)
        tcxLoader.load_tcx_file()
        self.model.loadData(tcxLoader.getTrackPoints())
        self.tableView.resizeColumnsToContents()
        self._updateFileInfoTab(tcxLoader)
        self._updateStatisticsTab()
        self._updateMap()

    def _updateFileInfoTab(self, tcxLoader:TCXLoader):
        self.inputNotes.setText(tcxLoader.getNotes())
        self.inputId.setText(tcxLoader.getId())
        self.inputSport.setText(tcxLoader.getType())
        self.inputLaps.setText(str(len(tcxLoader.getLaps())))
        self.inputTrackPoints.setText(str(len(tcxLoader.getTrackPoints())))
        pass

    def _updateStatisticsTab(self):
        values = {
            "latitude": {
                "max": 0,
                "min": 0,
                "missing": 0
            },
            "longitude": {
                "max": 0,
                "min": 0,
                "missing": 0
            },
            "altitude": {
                "max": 0,
                "min": 0,
                "missing": 0
            },
            "hartRate": {
                "max": 0,
                "min": 0,
                "missing": 0
            },
            "distance": {
                "max": 0,
                "min": 0,
                "missing": 0
            },
            "calculatedDistance": {
                "max": 0,
                "min": 0,
                "missing": 0
            },
            "speed": {
                "max": 0,
                "min": 0,
                "missing": 0
            },
            "calculatedSpeed": {
                "max": 0,
                "min": 0,
                "missing": 0
            }
        }
        for row in range(0, self.model.rowCount()):
            for col in range(0, self.model.columnCount()):
                val = self.model.data(self.model.index(row, col), Qt.ItemDataRole.EditRole)
                colName = TrackPointModel.indexToName(col)
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

    def _updateMap(self):
        coordinates = []
        for row in range(0, self.model.rowCount()):
            longitude = self.model.data(self.model.index(row, TrackPointModel.nameToIndex('longitude')), Qt.ItemDataRole.EditRole)
            latitude = self.model.data(self.model.index(row, TrackPointModel.nameToIndex('latitude')), Qt.ItemDataRole.EditRole)
            if longitude is not None and latitude is not None:
                coordinates.append([longitude, latitude])
        self.mapWindow.sendNewCoordinates(coordinates)
        pass

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

    def _onSaveFile(self):
        self.progress.hide()
        print('Save file')

    def _calculateSpeed(self):
        self.model.sortBy('time', Qt.SortOrder.AscendingOrder)
        colDist = TrackPointModel.nameToIndex('distance')
        colCalcDist = TrackPointModel.nameToIndex('calculatedSpeed')
        updateIndex = self.model.index(0, colCalcDist)
        self.model.setData(updateIndex, 0, Qt.ItemDataRole.EditRole)
        for row in range(1, self.model.rowCount()):
            prevIndex = self.model.index(row-1, colDist)
            index = self.model.index(row, colDist)

            prevData = self.model.data(prevIndex, Qt.ItemDataRole.EditRole)
            data = self.model.data(index, Qt.ItemDataRole.EditRole)

            updateIndex = self.model.index(row, colCalcDist)
            if prevData is not None and data is not None:
                newVal = ((data - prevData)*360)/100
            else:
                newVal = 0
            self.model.setData(updateIndex, newVal, Qt.ItemDataRole.EditRole)
        self._updateStatisticsTab()
        self.tableView.resizeColumnsToContents()
        self.tableView.reset()

    def _onExit(self):
        self.app.exit()
        pass

    def _applyDelegates(self):
        for i in range(self.model.columnCount()):
            self.tableView.setItemDelegateForColumn(i, TrackPointModel.getColDelegate(i))

    def _onClear(self):
        self.model.clearData()# = TrackPointsModel()
        self.tableView.resizeColumnsToContents()
