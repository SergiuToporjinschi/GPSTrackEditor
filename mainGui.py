import sys

from tcxmodel import TrackPointsModel, TrackPointModel, TCXLoader
from internalWidgets import StatusBarGroupBox

from gui.DockWidget import MapDockWidget, StatisticsDockWidget, FileInfoDockWidget, FilterDockWidget, ProcessingDockWidget, MarkingDockWidget
from gui.main_remaster_ui import Ui_MainWindow

from PySide6.QtGui import QPalette
from PySide6.QtCore import Qt, QObject, QTimer, QModelIndex
from PySide6.QtWidgets import QFileDialog, QMainWindow, QApplication, QAbstractItemDelegate, QColorDialog
import gpstracker_rc

sys.argv.append("--disable-web-security")
# class itDel(QAbstractItemDelegate):
#     def __init__(self, parent: QObject | None = ...) -> None:
#         super().__init__()
#     pass
gpstracker_rc.qInitResources()
class mainGUI(QMainWindow, Ui_MainWindow):
    fileName = ''
    tcx = None

    def __init__(self, app:QApplication):
        super().__init__()
        self.setupUi(self)
        self.tcxLoader = TCXLoader()
        # self.buttonCalculateSpeed.clicked.connect(self._calculateSpeed)
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
        # self.pushButtonFind.clicked.connect(self._onFindButton)
        # self.pushButtonFindClear.clicked.connect(self._onFindButton)

        # self.pushButtonMarkStat.clicked.connect(lambda: self.model.markStationary(self.spinBoxMarkStatSelectRange.value()))

        self._connectSignals()

        # adding docks---------------------------------------------
        self.mapWindow = MapDockWidget(parent=self, model=self.model, selectionModel=self.tableView.selectionModel())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.mapWindow)

        self.dockStatistics = StatisticsDockWidget(parent=self, model=self.model)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockStatistics)

        self.dockFileInfo = FileInfoDockWidget(self, self.tcxLoader)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockFileInfo)
        self.dockFileInfo.statusMessage.connect(self.progress.updateTimerMessage)

        self.dockFilter = FilterDockWidget(parent=self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockFilter)

        self.dockProcessing = ProcessingDockWidget(parent=self, model=self.model)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockProcessing)

        self.dockMarking = MarkingDockWidget(parent=self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockMarking)

        self.tabifyDockWidget(self.dockFileInfo, self.dockStatistics)
        self.tabifyDockWidget(self.dockFileInfo, self.dockFilter)
        self.tabifyDockWidget(self.dockFileInfo, self.dockProcessing)
        self.tabifyDockWidget(self.dockFileInfo, self.dockMarking)
        # connect signals
        self.model.mainSeriesChanged.connect(self.dockStatistics.calculateStatistics)
        self.model.clearData()

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

    # def _markStationarySelectColor(self):
    #     color = QColorDialog.getColor()
    #     if color.isValid():
    #         pal = QPalette()
    #         pal.setColor(QPalette.ColorRole.Button, color)
    #         self.markStatSelColor.setPalette(pal)

    def _connectSignals(self):
        # self.slider.selectedIntervalChanged.connect(lambda val: print("selectedIntervalChanged", val))
        self.slider.selectedIntervalChanged.connect(self.model.filterByRowNumbers)
        self.slider.selectionCountChanged.connect(self.progress.updateSelection)
        self.slider.selectedIntervalChanged.connect(lambda val: self._noDataDisable(val[1]-val[0]>0))
        self.model.allTrackPointsCountChanged.connect(self.progress.updateTackPoints)
        # self.timerClear.timeout.connect(lambda: self.progress.updateTimerMessage.emit(''))
        # self.timerClear.timeout.connect(lambda: self.progress.updateProgress.emit(0))
        self.model.statusMessage.connect(self.progress.updateTimerMessage)
        # self.editFindBySpeed.textChanged.connect(lambda x: print(x))
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
        # self.labelFilePath.setText(file_name)

        self.tcxLoader.workingProgress.connect(self.progress.updateProgress)
        self.tcxLoader.load_tcx_file(file_name)
        self.model.loadData(self.tcxLoader.getTrackPoints())
        self.tableView.resizeColumnsToContents()


    def _onSaveFile(self):
        self.progress.hide()
        print('Save file')

    def _onExit(self):
        self.app.exit()
        pass

    def _applyDelegates(self):
        for i in range(self.model.columnCount()):
            self.tableView.setItemDelegateForColumn(i, TrackPointModel.getColDelegate(i))

    def _onClear(self):
        self.model.clearData()# = TrackPointsModel()
        self.tableView.resizeColumnsToContents()
