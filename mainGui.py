import sys

from TCXModel import TrackPointsModel, TCXColModel # TrackPointModel
from FileLoader import TCXLoader

from internalWidgets import QtSliderFilterWidgetPlugin
from gui.main_remaster_ui import Ui_MainWindow
from StatusBar import StatusBarGroupBox, StatusMessage

from gui.DockWidget import MapDockWidget, StatisticsDockWidget, FileInfoDockWidget, FilterDockWidget, ProcessingDockWidget, MarkingDockWidget
from AbstractModelWidget import AbstractModelWidget, AbstractNotificationWidget
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMainWindow, QApplication
import gpstracker_rc

sys.argv.append("--disable-web-security")

gpstracker_rc.qInitResources()


class mainGUI(QMainWindow, Ui_MainWindow):
    fileName = ''
    tcx = None

    def __init__(self, app:QApplication):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.actionSave.triggered.connect(self._onSaveFile)
        self.actionOpen.triggered.connect(self._onOpenFile)
        self.actionExit.triggered.connect(self._onExit)
        self.actionClear.triggered.connect(self._onClear)

        self.model = TrackPointsModel(palette=app.palette())
        self.tableView.setModel(self.model)
        self.model.mainSeriesChanged.connect(self.tableView.resizeColumnsToContents)

        self._applyDelegates()

        # adding statusBar ----------------------------------------
        self.statusInfoBar = StatusBarGroupBox(parent=self.statusbar)
        self.statusbar.addPermanentWidget(self.statusInfoBar, 1)

        # adding fileLoader ---------------------------------------
        self.tcxLoader = TCXLoader()
        self.tcxLoader.trackPointsChanged.connect(self.model.loadData)

        # adding slider -------------------------------------------
        self.trimmerSlider = QtSliderFilterWidgetPlugin(self, self.model)
        self.sliderLayout.addWidget(self.trimmerSlider)

        # adding docks---------------------------------------------
        self.mapWindow = MapDockWidget(self, self.model, self.tableView.selectionModel())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.mapWindow)

        self.dockStatistics = StatisticsDockWidget(self, self.model)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockStatistics)

        self.dockFileInfo = FileInfoDockWidget(self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockFileInfo)
        self.tcxLoader.fileDataChanged.connect(self.dockFileInfo.loadInfo)

        self.dockFilter = FilterDockWidget(self, self.model)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockFilter)

        self.dockProcessing = ProcessingDockWidget(self, self.model)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockProcessing)

        self.dockMarking = MarkingDockWidget(self, self.model)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockMarking)

        self.tabifyDockWidget(self.dockFileInfo, self.dockStatistics)
        self.tabifyDockWidget(self.dockFileInfo, self.dockFilter)
        self.tabifyDockWidget(self.dockFileInfo, self.dockProcessing)
        self.tabifyDockWidget(self.dockFileInfo, self.dockMarking)

        # connect signals -----------------------------------------
        self._connectSignalsToStatusBar()
        self.model.mainSeriesChanged.connect(self.dockStatistics.calculateStatistics)
        self.model.clearData()

    def _connectSignalsToStatusBar(self):
        self.model.mainSeriesLengthChanged.connect(self.statusInfoBar.updateTackLen)
        self.model.trimRangeChanged.connect(self.statusInfoBar.updateTrimmerLen)

        self.model.statusMessage.connect(self.statusInfoBar.updateMessage)
        self.model.workingProgress.connect(self.statusInfoBar.updateProgress)

        self.model.mainSeriesChanged.connect(self.tableView.resizeColumnsToContents)
        for _, item in vars(self).items():
            if isinstance(item, AbstractNotificationWidget):
                item.statusMessage.connect(self.statusInfoBar.updateMessage)
                item.updateProgress.connect(self.statusInfoBar.updateProgress)
                pass

    def _onOpenFile(self):
        self.statusInfoBar.updateMessage.emit(StatusMessage('Loading file...'))
        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'All Files (*.tcx)')
        if not file_name:
            return
        self.fileName = file_name
        self.tcxLoader.loadTCXAsync(file_name)

    def _onSaveFile(self):
        self.statusInfoBar.updateMessage.emit(StatusMessage('Loading file...', 10000, QColor('green')))

    def _onExit(self):
        self.app.exit()
        pass

    def _applyDelegates(self):
        for i in range(self.model.columnCount()):
            self.tableView.setItemDelegateForColumn(i, TCXColModel()[i].delegate)

    def _onClear(self):
        self.model.clearData()# = TrackPointsModel()
        self.tableView.resizeColumnsToContents()
