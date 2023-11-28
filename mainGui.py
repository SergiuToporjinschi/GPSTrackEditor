from models import TrackPointsModel, TCXColModel # TrackPointModel
from loaders import TCXLoader

from internalWidgets import QtSliderFilterWidgetPlugin
from modules import MarkingDockWidget
from gui.main_remaster_ui import Ui_MainWindow

from gui.StatusBar import StatusBarGroupBox
from StatusMessage import StatusMessage
from config import *
from gui.DockWidget import *
from abstracts import AbstractNotificationWidget
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QByteArray
from PySide6.QtWidgets import QFileDialog, QMainWindow, QApplication, QSplitter, QTabBar, QDockWidget
import gpstracker_rc

# sys.argv.append("--disable-web-security")

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
        self._settingsTable()
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

        self.tabifyDockWidget(self.dockFileInfo, self.dockFilter)
        self.tabifyDockWidget(self.dockFileInfo, self.dockProcessing)
        self.tabifyDockWidget(self.dockFileInfo, self.dockMarking)
        self.tabifyDockWidget(self.dockFileInfo, self.dockStatistics)
        # connect signals -----------------------------------------
        self._connectSignalsToStatusBar()
        self.model.mainSeriesChanged.connect(self.dockStatistics.calculateStatistics)
        self.model.clearData()

    def _onSaveFile(self):
        self.statusInfoBar.updateMessage.emit(StatusMessage('Saving file...', QColor('green'), 10000))
        # docks = [i for i in self.children() if isinstance(i, QDockWidget)][:]
        # Config.setValueG(ConfigGroup.MainWindow, ConfigAttribute.State1, self.saveState())
        # self.saveState()?

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
        self.model.sort(0, Qt.SortOrder.AscendingOrder)
        self.tcxLoader.loadTCXAsync(file_name)



    def _onExit(self):
        self.app.exit()
        pass

    def _applyDelegates(self):
        for i in range(self.model.columnCount()):
            self.tableView.setItemDelegateForColumn(i, TCXColModel()[i].delegate)

    def _onClear(self):
        self.model.clearData()# = TrackPointsModel()
        self.tableView.resizeColumnsToContents()

    def _settingsTable(self):
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)

        col, direction = Config.valueG(ConfigGroup.TrackGrid, ConfigAttribute.Sorting, (-1, Qt.SortOrder.AscendingOrder))

        self.model.mainSeriesChanged.connect(self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch))

        self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        self.tableView.horizontalHeader().setSortIndicator(col, direction)
        self.tableView.horizontalHeader().sortIndicatorChanged.connect(lambda colNo, direction: Config.setValueG(ConfigGroup.TrackGrid, ConfigAttribute.Sorting, (colNo, direction)))
