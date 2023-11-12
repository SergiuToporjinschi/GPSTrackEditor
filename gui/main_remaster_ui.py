# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_remaster.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDateTimeEdit, QDockWidget, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTableView,
    QToolBar, QVBoxLayout, QWidget)

from internalWidgets import QtSliderFilterWidgetPlugin

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(853, 885)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAnimated(False)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.GroupedDragging)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u":/folder-open-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u":/content-save-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        icon2.addFile(u":/exit-run.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon3 = QIcon()
        icon3.addFile(u":/close-circle-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClear.setIcon(icon3)
        self.actionclose = QAction(MainWindow)
        self.actionclose.setObjectName(u"actionclose")
        self.actionclose.setCheckable(True)
        self.actionclose.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setSizeIncrement(QSize(0, 34))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.verticalTableLayout = QVBoxLayout(self.frame)
        self.verticalTableLayout.setObjectName(u"verticalTableLayout")
        self.verticalTableLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMidLineWidth(1)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)

        self.verticalTableLayout.addWidget(self.tableView)

        self.slider = QtSliderFilterWidgetPlugin(self.frame)
        self.slider.setObjectName(u"slider")
        self.slider.setFrameShape(QFrame.StyledPanel)
        self.slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.slider)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalTableLayout.addWidget(self.slider)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 853, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidgetFiltering = QDockWidget(MainWindow)
        self.dockWidgetFiltering.setObjectName(u"dockWidgetFiltering")
        self.dockWidgetFiltering.setMinimumSize(QSize(544, 98))
        self.dockWidgetFiltering.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetFiltering.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_10 = QWidget()
        self.dockWidgetContents_10.setObjectName(u"dockWidgetContents_10")
        self.verticalLayout_6 = QVBoxLayout(self.dockWidgetContents_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 5, 0, 0)
        self.scrollArea_5 = QScrollArea(self.dockWidgetContents_10)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setFrameShadow(QFrame.Plain)
        self.scrollArea_5.setLineWidth(0)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 507, 320))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 9, -1)
        self.doubleSpinBox_31 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_31.setObjectName(u"doubleSpinBox_31")
        self.doubleSpinBox_31.setMinimumSize(QSize(0, 22))
        self.doubleSpinBox_31.setMaximumSize(QSize(16777215, 22))
        self.doubleSpinBox_31.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_31.setDecimals(16)
        self.doubleSpinBox_31.setMaximum(999999.000000000000000)
        self.doubleSpinBox_31.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_31, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.label_169 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_169.setObjectName(u"label_169")

        self.gridLayout.addWidget(self.label_169, 0, 1, 1, 1)

        self.doubleSpinBox_25 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_25.setObjectName(u"doubleSpinBox_25")
        self.doubleSpinBox_25.setMinimumSize(QSize(0, 22))
        self.doubleSpinBox_25.setMaximumSize(QSize(16777215, 22))
        self.doubleSpinBox_25.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_25.setDecimals(12)
        self.doubleSpinBox_25.setMaximum(999999.000000000000000)
        self.doubleSpinBox_25.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_25, 7, 1, 1, 1)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")
        self.doubleSpinBox_16.setMinimumSize(QSize(0, 22))
        self.doubleSpinBox_16.setMaximumSize(QSize(16777215, 22))
        self.doubleSpinBox_16.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_16.setDecimals(8)
        self.doubleSpinBox_16.setMaximum(999999.000000000000000)
        self.doubleSpinBox_16.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_16, 10, 2, 1, 1)

        self.doubleSpinBox_22 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_22.setObjectName(u"doubleSpinBox_22")
        self.doubleSpinBox_22.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_22.setDecimals(8)
        self.doubleSpinBox_22.setMaximum(999999.000000000000000)
        self.doubleSpinBox_22.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_22, 5, 2, 1, 1)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_3, 3, 0, 1, 1)

        self.checkBox_10 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_10, 10, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_7, 7, 0, 1, 1)

        self.dateTimeEdit_4 = QDateTimeEdit(self.scrollAreaWidgetContents_5)
        self.dateTimeEdit_4.setObjectName(u"dateTimeEdit_4")
        self.dateTimeEdit_4.setSizeIncrement(QSize(50, 0))
        self.dateTimeEdit_4.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateTimeEdit_4.setCalendarPopup(True)
        self.dateTimeEdit_4.setTimeSpec(Qt.UTC)

        self.gridLayout.addWidget(self.dateTimeEdit_4, 2, 2, 1, 1)

        self.doubleSpinBox_27 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_27.setObjectName(u"doubleSpinBox_27")
        self.doubleSpinBox_27.setMinimumSize(QSize(0, 22))
        self.doubleSpinBox_27.setMaximumSize(QSize(16777215, 22))
        self.doubleSpinBox_27.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_27.setDecimals(16)
        self.doubleSpinBox_27.setMaximum(999999.000000000000000)
        self.doubleSpinBox_27.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_27, 3, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_9, 9, 0, 1, 1)

        self.doubleSpinBox_28 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_28.setObjectName(u"doubleSpinBox_28")
        self.doubleSpinBox_28.setMinimumSize(QSize(0, 22))
        self.doubleSpinBox_28.setMaximumSize(QSize(16777215, 22))
        self.doubleSpinBox_28.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_28.setDecimals(16)
        self.doubleSpinBox_28.setMaximum(999999.000000000000000)
        self.doubleSpinBox_28.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_28, 3, 2, 1, 1)

        self.doubleSpinBox_24 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_24.setObjectName(u"doubleSpinBox_24")
        self.doubleSpinBox_24.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_24.setDecimals(3)
        self.doubleSpinBox_24.setMaximum(999999.000000000000000)
        self.doubleSpinBox_24.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_24, 8, 2, 1, 1)

        self.doubleSpinBox_29 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_29.setObjectName(u"doubleSpinBox_29")
        self.doubleSpinBox_29.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_29.setDecimals(12)
        self.doubleSpinBox_29.setMaximum(999999.000000000000000)
        self.doubleSpinBox_29.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_29, 6, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_8, 8, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_4, 4, 0, 1, 1)

        self.doubleSpinBox_26 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_26.setObjectName(u"doubleSpinBox_26")
        self.doubleSpinBox_26.setMinimumSize(QSize(0, 22))
        self.doubleSpinBox_26.setMaximumSize(QSize(16777215, 22))
        self.doubleSpinBox_26.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_26.setDecimals(12)
        self.doubleSpinBox_26.setMaximum(999999.000000000000000)
        self.doubleSpinBox_26.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_26, 7, 2, 1, 1)

        self.doubleSpinBox_18 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_18.setObjectName(u"doubleSpinBox_18")
        self.doubleSpinBox_18.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_18.setMaximum(999999.000000000000000)
        self.doubleSpinBox_18.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_18, 9, 2, 1, 1)

        self.doubleSpinBox_32 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_32.setObjectName(u"doubleSpinBox_32")
        self.doubleSpinBox_32.setMinimumSize(QSize(0, 22))
        self.doubleSpinBox_32.setMaximumSize(QSize(16777215, 22))
        self.doubleSpinBox_32.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_32.setDecimals(16)
        self.doubleSpinBox_32.setMaximum(999999.000000000000000)
        self.doubleSpinBox_32.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_32, 1, 2, 1, 1)

        self.label_170 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_170.setObjectName(u"label_170")

        self.gridLayout.addWidget(self.label_170, 0, 2, 1, 1)

        self.checkBox_6 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_6, 6, 0, 1, 1)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")
        self.doubleSpinBox_15.setMinimumSize(QSize(0, 22))
        self.doubleSpinBox_15.setMaximumSize(QSize(16777215, 22))
        self.doubleSpinBox_15.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_15.setDecimals(8)
        self.doubleSpinBox_15.setMaximum(999999.000000000000000)
        self.doubleSpinBox_15.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_15, 10, 1, 1, 1)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(False)

        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)

        self.doubleSpinBox_30 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_30.setObjectName(u"doubleSpinBox_30")
        self.doubleSpinBox_30.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_30.setDecimals(12)
        self.doubleSpinBox_30.setMaximum(999999.000000000000000)
        self.doubleSpinBox_30.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_30, 6, 2, 1, 1)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")
        self.doubleSpinBox_17.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_17.setMaximum(999999.000000000000000)
        self.doubleSpinBox_17.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_17, 9, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_5, 5, 0, 1, 1)

        self.doubleSpinBox_21 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_21.setObjectName(u"doubleSpinBox_21")
        self.doubleSpinBox_21.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_21.setDecimals(8)
        self.doubleSpinBox_21.setMaximum(999999.000000000000000)
        self.doubleSpinBox_21.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_21, 5, 1, 1, 1)

        self.dateTimeEdit_3 = QDateTimeEdit(self.scrollAreaWidgetContents_5)
        self.dateTimeEdit_3.setObjectName(u"dateTimeEdit_3")
        self.dateTimeEdit_3.setSizeIncrement(QSize(50, 0))
        self.dateTimeEdit_3.setCalendarPopup(True)
        self.dateTimeEdit_3.setTimeSpec(Qt.UTC)

        self.gridLayout.addWidget(self.dateTimeEdit_3, 2, 1, 1, 1)

        self.doubleSpinBox_23 = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_23.setObjectName(u"doubleSpinBox_23")
        self.doubleSpinBox_23.setSizeIncrement(QSize(50, 0))
        self.doubleSpinBox_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_23.setDecimals(3)
        self.doubleSpinBox_23.setMaximum(999999.000000000000000)
        self.doubleSpinBox_23.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_23, 8, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 11, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setSizeIncrement(QSize(50, 0))
        self.comboBox_2.setMaxVisibleItems(10)

        self.gridLayout.addWidget(self.comboBox_2, 4, 1, 1, 2)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_6.addWidget(self.scrollArea_5)

        self.dockWidgetFiltering.setWidget(self.dockWidgetContents_10)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidgetFiltering)
        self.dockWidgetStatistics = QDockWidget(MainWindow)
        self.dockWidgetStatistics.setObjectName(u"dockWidgetStatistics")
        self.dockWidgetStatistics.setMinimumSize(QSize(544, 150))
        self.dockWidgetStatistics.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetStatistics.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_7 = QWidget()
        self.dockWidgetContents_7.setObjectName(u"dockWidgetContents_7")
        self.verticalLayout_8 = QVBoxLayout(self.dockWidgetContents_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 5, 0, 0)
        self.scrollArea_2 = QScrollArea(self.dockWidgetContents_7)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 507, 1171))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 9, 9, 0)
        self.groupBox_27 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.gridLayout_28 = QGridLayout(self.groupBox_27)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_151 = QLabel(self.groupBox_27)
        self.label_151.setObjectName(u"label_151")
        font = QFont()
        font.setBold(True)
        self.label_151.setFont(font)

        self.gridLayout_28.addWidget(self.label_151, 2, 0, 1, 1)

        self.labelCalculatedDistanceMaxM = QLabel(self.groupBox_27)
        self.labelCalculatedDistanceMaxM.setObjectName(u"labelCalculatedDistanceMaxM")
        self.labelCalculatedDistanceMaxM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.labelCalculatedDistanceMaxM, 3, 1, 1, 1)

        self.label_152 = QLabel(self.groupBox_27)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font)

        self.gridLayout_28.addWidget(self.label_152, 1, 0, 1, 1)

        self.label_153 = QLabel(self.groupBox_27)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setFont(font)

        self.gridLayout_28.addWidget(self.label_153, 3, 0, 1, 1)

        self.label_154 = QLabel(self.groupBox_27)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setFont(font)
        self.label_154.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.label_154, 0, 2, 1, 1)

        self.label_155 = QLabel(self.groupBox_27)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setFont(font)
        self.label_155.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.label_155, 0, 1, 1, 1)

        self.labelCalculatedDistanceAvgM = QLabel(self.groupBox_27)
        self.labelCalculatedDistanceAvgM.setObjectName(u"labelCalculatedDistanceAvgM")
        self.labelCalculatedDistanceAvgM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.labelCalculatedDistanceAvgM, 2, 1, 1, 1)

        self.labelCalculatedDistanceMinM = QLabel(self.groupBox_27)
        self.labelCalculatedDistanceMinM.setObjectName(u"labelCalculatedDistanceMinM")
        self.labelCalculatedDistanceMinM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.labelCalculatedDistanceMinM, 1, 1, 1, 1)

        self.labelCalculatedDistanceAvgKM = QLabel(self.groupBox_27)
        self.labelCalculatedDistanceAvgKM.setObjectName(u"labelCalculatedDistanceAvgKM")
        self.labelCalculatedDistanceAvgKM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.labelCalculatedDistanceAvgKM, 2, 2, 1, 1)

        self.labelCalculatedDistanceMaxKM = QLabel(self.groupBox_27)
        self.labelCalculatedDistanceMaxKM.setObjectName(u"labelCalculatedDistanceMaxKM")
        self.labelCalculatedDistanceMaxKM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.labelCalculatedDistanceMaxKM, 3, 2, 1, 1)

        self.labelCalculatedDistanceMinKM = QLabel(self.groupBox_27)
        self.labelCalculatedDistanceMinKM.setObjectName(u"labelCalculatedDistanceMinKM")
        self.labelCalculatedDistanceMinKM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.labelCalculatedDistanceMinKM, 1, 2, 1, 1)

        self.label_156 = QLabel(self.groupBox_27)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font)

        self.gridLayout_28.addWidget(self.label_156, 4, 0, 1, 1)

        self.labelCalculatedDistanceMissing = QLabel(self.groupBox_27)
        self.labelCalculatedDistanceMissing.setObjectName(u"labelCalculatedDistanceMissing")
        self.labelCalculatedDistanceMissing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.labelCalculatedDistanceMissing, 4, 1, 1, 2)


        self.verticalLayout_7.addWidget(self.groupBox_27)

        self.groupBox_26 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.gridLayout_27 = QGridLayout(self.groupBox_26)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_145 = QLabel(self.groupBox_26)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setFont(font)
        self.label_145.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.label_145, 0, 1, 1, 1)

        self.labelDistanceMissing = QLabel(self.groupBox_26)
        self.labelDistanceMissing.setObjectName(u"labelDistanceMissing")
        self.labelDistanceMissing.setLineWidth(2)
        self.labelDistanceMissing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelDistanceMissing, 4, 1, 1, 2)

        self.labelDistanceMaxKM = QLabel(self.groupBox_26)
        self.labelDistanceMaxKM.setObjectName(u"labelDistanceMaxKM")
        self.labelDistanceMaxKM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelDistanceMaxKM, 3, 2, 1, 1)

        self.label_146 = QLabel(self.groupBox_26)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font)

        self.gridLayout_27.addWidget(self.label_146, 2, 0, 1, 1)

        self.labelDistanceMinKM = QLabel(self.groupBox_26)
        self.labelDistanceMinKM.setObjectName(u"labelDistanceMinKM")
        self.labelDistanceMinKM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelDistanceMinKM, 1, 2, 1, 1)

        self.labelDistanceAvgM = QLabel(self.groupBox_26)
        self.labelDistanceAvgM.setObjectName(u"labelDistanceAvgM")
        self.labelDistanceAvgM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelDistanceAvgM, 2, 1, 1, 1)

        self.labelDistanceMaxM = QLabel(self.groupBox_26)
        self.labelDistanceMaxM.setObjectName(u"labelDistanceMaxM")
        self.labelDistanceMaxM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelDistanceMaxM, 3, 1, 1, 1)

        self.label_147 = QLabel(self.groupBox_26)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setFont(font)

        self.gridLayout_27.addWidget(self.label_147, 1, 0, 1, 1)

        self.labelDistanceAvgKM = QLabel(self.groupBox_26)
        self.labelDistanceAvgKM.setObjectName(u"labelDistanceAvgKM")
        self.labelDistanceAvgKM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelDistanceAvgKM, 2, 2, 1, 1)

        self.label_148 = QLabel(self.groupBox_26)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setFont(font)

        self.gridLayout_27.addWidget(self.label_148, 3, 0, 1, 1)

        self.label_149 = QLabel(self.groupBox_26)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setFont(font)
        self.label_149.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.label_149, 0, 2, 1, 1)

        self.labelDistanceMinM = QLabel(self.groupBox_26)
        self.labelDistanceMinM.setObjectName(u"labelDistanceMinM")
        self.labelDistanceMinM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.labelDistanceMinM, 1, 1, 1, 1)

        self.label_150 = QLabel(self.groupBox_26)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setFont(font)

        self.gridLayout_27.addWidget(self.label_150, 4, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_26)

        self.groupBox_25 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.gridLayout_26 = QGridLayout(self.groupBox_25)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_139 = QLabel(self.groupBox_25)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setFont(font)
        self.label_139.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_139, 0, 1, 1, 1)

        self.label_140 = QLabel(self.groupBox_25)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setFont(font)

        self.gridLayout_26.addWidget(self.label_140, 3, 0, 1, 1)

        self.labelCalculatedSpeedMissing = QLabel(self.groupBox_25)
        self.labelCalculatedSpeedMissing.setObjectName(u"labelCalculatedSpeedMissing")
        self.labelCalculatedSpeedMissing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelCalculatedSpeedMissing, 4, 1, 1, 2)

        self.labelCalculatedSpeedMaxKMPH = QLabel(self.groupBox_25)
        self.labelCalculatedSpeedMaxKMPH.setObjectName(u"labelCalculatedSpeedMaxKMPH")
        self.labelCalculatedSpeedMaxKMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelCalculatedSpeedMaxKMPH, 3, 2, 1, 1)

        self.label_141 = QLabel(self.groupBox_25)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setFont(font)

        self.gridLayout_26.addWidget(self.label_141, 1, 0, 1, 1)

        self.label_142 = QLabel(self.groupBox_25)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setFont(font)
        self.label_142.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_142, 0, 2, 1, 1)

        self.label_143 = QLabel(self.groupBox_25)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setFont(font)

        self.gridLayout_26.addWidget(self.label_143, 4, 0, 1, 1)

        self.labelCalculatedSpeedAvgMPH = QLabel(self.groupBox_25)
        self.labelCalculatedSpeedAvgMPH.setObjectName(u"labelCalculatedSpeedAvgMPH")
        self.labelCalculatedSpeedAvgMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelCalculatedSpeedAvgMPH, 2, 1, 1, 1)

        self.labelCalculatedSpeedMinMPH = QLabel(self.groupBox_25)
        self.labelCalculatedSpeedMinMPH.setObjectName(u"labelCalculatedSpeedMinMPH")
        self.labelCalculatedSpeedMinMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelCalculatedSpeedMinMPH, 1, 1, 1, 1)

        self.labelCalculatedSpeedMinKMPH = QLabel(self.groupBox_25)
        self.labelCalculatedSpeedMinKMPH.setObjectName(u"labelCalculatedSpeedMinKMPH")
        self.labelCalculatedSpeedMinKMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelCalculatedSpeedMinKMPH, 1, 2, 1, 1)

        self.labelCalculatedSpeedAvgKMPH = QLabel(self.groupBox_25)
        self.labelCalculatedSpeedAvgKMPH.setObjectName(u"labelCalculatedSpeedAvgKMPH")
        self.labelCalculatedSpeedAvgKMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelCalculatedSpeedAvgKMPH, 2, 2, 1, 1)

        self.label_144 = QLabel(self.groupBox_25)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setFont(font)

        self.gridLayout_26.addWidget(self.label_144, 2, 0, 1, 1)

        self.labelCalculatedSpeedMaxMPH = QLabel(self.groupBox_25)
        self.labelCalculatedSpeedMaxMPH.setObjectName(u"labelCalculatedSpeedMaxMPH")
        self.labelCalculatedSpeedMaxMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.labelCalculatedSpeedMaxMPH, 3, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_25)

        self.groupBox_24 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_24.setObjectName(u"groupBox_24")
        font1 = QFont()
        font1.setBold(False)
        self.groupBox_24.setFont(font1)
        self.gridLayout_25 = QGridLayout(self.groupBox_24)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(15)
        self.labelSpeedAvgKMPH = QLabel(self.groupBox_24)
        self.labelSpeedAvgKMPH.setObjectName(u"labelSpeedAvgKMPH")
        self.labelSpeedAvgKMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelSpeedAvgKMPH, 2, 2, 1, 1)

        self.labelSpeedMinKMPH = QLabel(self.groupBox_24)
        self.labelSpeedMinKMPH.setObjectName(u"labelSpeedMinKMPH")
        self.labelSpeedMinKMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelSpeedMinKMPH, 1, 2, 1, 1)

        self.label_133 = QLabel(self.groupBox_24)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font)
        self.label_133.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_133, 0, 1, 1, 1)

        self.label_134 = QLabel(self.groupBox_24)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font)

        self.gridLayout_25.addWidget(self.label_134, 3, 0, 1, 1)

        self.labelSpeedMaxKMPH = QLabel(self.groupBox_24)
        self.labelSpeedMaxKMPH.setObjectName(u"labelSpeedMaxKMPH")
        self.labelSpeedMaxKMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelSpeedMaxKMPH, 3, 2, 1, 1)

        self.labelSpeedAvgMPH = QLabel(self.groupBox_24)
        self.labelSpeedAvgMPH.setObjectName(u"labelSpeedAvgMPH")
        self.labelSpeedAvgMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelSpeedAvgMPH, 2, 1, 1, 1)

        self.label_135 = QLabel(self.groupBox_24)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font)

        self.gridLayout_25.addWidget(self.label_135, 1, 0, 1, 1)

        self.labelSpeedMaxMPH = QLabel(self.groupBox_24)
        self.labelSpeedMaxMPH.setObjectName(u"labelSpeedMaxMPH")
        self.labelSpeedMaxMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelSpeedMaxMPH, 3, 1, 1, 1)

        self.labelSpeedMinMPH = QLabel(self.groupBox_24)
        self.labelSpeedMinMPH.setObjectName(u"labelSpeedMinMPH")
        self.labelSpeedMinMPH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelSpeedMinMPH, 1, 1, 1, 1)

        self.label_136 = QLabel(self.groupBox_24)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setFont(font)

        self.gridLayout_25.addWidget(self.label_136, 2, 0, 1, 1)

        self.label_137 = QLabel(self.groupBox_24)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setFont(font)
        self.label_137.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_137, 0, 2, 1, 1)

        self.label_138 = QLabel(self.groupBox_24)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setFont(font)

        self.gridLayout_25.addWidget(self.label_138, 4, 0, 1, 1)

        self.labelSpeedMissing = QLabel(self.groupBox_24)
        self.labelSpeedMissing.setObjectName(u"labelSpeedMissing")
        self.labelSpeedMissing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelSpeedMissing, 4, 1, 1, 2)


        self.verticalLayout_7.addWidget(self.groupBox_24)

        self.groupBox_23 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_24 = QGridLayout(self.groupBox_23)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_127 = QLabel(self.groupBox_23)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setFont(font)

        self.gridLayout_24.addWidget(self.label_127, 2, 0, 1, 1)

        self.label_128 = QLabel(self.groupBox_23)
        self.label_128.setObjectName(u"label_128")

        self.gridLayout_24.addWidget(self.label_128, 0, 0, 1, 1)

        self.labelAltitudeMin = QLabel(self.groupBox_23)
        self.labelAltitudeMin.setObjectName(u"labelAltitudeMin")
        self.labelAltitudeMin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.labelAltitudeMin, 1, 1, 1, 1)

        self.labelAltitudeMax = QLabel(self.groupBox_23)
        self.labelAltitudeMax.setObjectName(u"labelAltitudeMax")
        self.labelAltitudeMax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.labelAltitudeMax, 3, 1, 1, 1)

        self.label_129 = QLabel(self.groupBox_23)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font)

        self.gridLayout_24.addWidget(self.label_129, 1, 0, 1, 1)

        self.labelAltitudeAvg = QLabel(self.groupBox_23)
        self.labelAltitudeAvg.setObjectName(u"labelAltitudeAvg")
        self.labelAltitudeAvg.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.labelAltitudeAvg, 2, 1, 1, 1)

        self.label_130 = QLabel(self.groupBox_23)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setFont(font)
        self.label_130.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_130, 0, 1, 1, 1)

        self.label_131 = QLabel(self.groupBox_23)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setFont(font)

        self.gridLayout_24.addWidget(self.label_131, 3, 0, 1, 1)

        self.label_132 = QLabel(self.groupBox_23)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font)

        self.gridLayout_24.addWidget(self.label_132, 4, 0, 1, 1)

        self.labelAltitudeMissing = QLabel(self.groupBox_23)
        self.labelAltitudeMissing.setObjectName(u"labelAltitudeMissing")
        self.labelAltitudeMissing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.labelAltitudeMissing, 4, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_23)

        self.groupBox_22 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_23 = QGridLayout(self.groupBox_22)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_121 = QLabel(self.groupBox_22)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setFont(font)

        self.gridLayout_23.addWidget(self.label_121, 2, 0, 1, 1)

        self.label_122 = QLabel(self.groupBox_22)
        self.label_122.setObjectName(u"label_122")

        self.gridLayout_23.addWidget(self.label_122, 0, 0, 1, 1)

        self.labelLongitudeMin = QLabel(self.groupBox_22)
        self.labelLongitudeMin.setObjectName(u"labelLongitudeMin")
        self.labelLongitudeMin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.labelLongitudeMin, 1, 1, 1, 1)

        self.labelLongitudeMax = QLabel(self.groupBox_22)
        self.labelLongitudeMax.setObjectName(u"labelLongitudeMax")
        self.labelLongitudeMax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.labelLongitudeMax, 3, 1, 1, 1)

        self.label_123 = QLabel(self.groupBox_22)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font)

        self.gridLayout_23.addWidget(self.label_123, 1, 0, 1, 1)

        self.labelLongitudeAvg = QLabel(self.groupBox_22)
        self.labelLongitudeAvg.setObjectName(u"labelLongitudeAvg")
        self.labelLongitudeAvg.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.labelLongitudeAvg, 2, 1, 1, 1)

        self.label_124 = QLabel(self.groupBox_22)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font)
        self.label_124.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_124, 0, 1, 1, 1)

        self.label_125 = QLabel(self.groupBox_22)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font)

        self.gridLayout_23.addWidget(self.label_125, 3, 0, 1, 1)

        self.label_126 = QLabel(self.groupBox_22)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setFont(font)

        self.gridLayout_23.addWidget(self.label_126, 4, 0, 1, 1)

        self.labelLongitudeMissing = QLabel(self.groupBox_22)
        self.labelLongitudeMissing.setObjectName(u"labelLongitudeMissing")
        self.labelLongitudeMissing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.labelLongitudeMissing, 4, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_22)

        self.groupBox_21 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_22 = QGridLayout(self.groupBox_21)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_115 = QLabel(self.groupBox_21)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font)

        self.gridLayout_22.addWidget(self.label_115, 2, 0, 1, 1)

        self.label_116 = QLabel(self.groupBox_21)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_22.addWidget(self.label_116, 0, 0, 1, 1)

        self.labelLatitudeMin = QLabel(self.groupBox_21)
        self.labelLatitudeMin.setObjectName(u"labelLatitudeMin")
        self.labelLatitudeMin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.labelLatitudeMin, 1, 1, 1, 1)

        self.labelLatitudeMax = QLabel(self.groupBox_21)
        self.labelLatitudeMax.setObjectName(u"labelLatitudeMax")
        self.labelLatitudeMax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.labelLatitudeMax, 3, 1, 1, 1)

        self.label_117 = QLabel(self.groupBox_21)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setFont(font)

        self.gridLayout_22.addWidget(self.label_117, 1, 0, 1, 1)

        self.labelLatitudeAvg = QLabel(self.groupBox_21)
        self.labelLatitudeAvg.setObjectName(u"labelLatitudeAvg")
        self.labelLatitudeAvg.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.labelLatitudeAvg, 2, 1, 1, 1)

        self.label_118 = QLabel(self.groupBox_21)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setFont(font)
        self.label_118.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_118, 0, 1, 1, 1)

        self.label_119 = QLabel(self.groupBox_21)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font)

        self.gridLayout_22.addWidget(self.label_119, 3, 0, 1, 1)

        self.label_120 = QLabel(self.groupBox_21)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setFont(font)

        self.gridLayout_22.addWidget(self.label_120, 4, 0, 1, 1)

        self.labelLatitudeMissing = QLabel(self.groupBox_21)
        self.labelLatitudeMissing.setObjectName(u"labelLatitudeMissing")
        self.labelLatitudeMissing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.labelLatitudeMissing, 4, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_21)

        self.groupBox_20 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_21 = QGridLayout(self.groupBox_20)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_109 = QLabel(self.groupBox_20)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font)

        self.gridLayout_21.addWidget(self.label_109, 2, 0, 1, 1)

        self.label_110 = QLabel(self.groupBox_20)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_21.addWidget(self.label_110, 0, 0, 1, 1)

        self.labelHartRateMin = QLabel(self.groupBox_20)
        self.labelHartRateMin.setObjectName(u"labelHartRateMin")
        self.labelHartRateMin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.labelHartRateMin, 1, 1, 1, 1)

        self.labelHartRateMax = QLabel(self.groupBox_20)
        self.labelHartRateMax.setObjectName(u"labelHartRateMax")
        self.labelHartRateMax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.labelHartRateMax, 3, 1, 1, 1)

        self.label_111 = QLabel(self.groupBox_20)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font)

        self.gridLayout_21.addWidget(self.label_111, 1, 0, 1, 1)

        self.labelHartRateAvg = QLabel(self.groupBox_20)
        self.labelHartRateAvg.setObjectName(u"labelHartRateAvg")
        self.labelHartRateAvg.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.labelHartRateAvg, 2, 1, 1, 1)

        self.label_112 = QLabel(self.groupBox_20)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setFont(font)
        self.label_112.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_112, 0, 1, 1, 1)

        self.label_113 = QLabel(self.groupBox_20)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font)

        self.gridLayout_21.addWidget(self.label_113, 3, 0, 1, 1)

        self.label_114 = QLabel(self.groupBox_20)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setFont(font)

        self.gridLayout_21.addWidget(self.label_114, 4, 0, 1, 1)

        self.labelHartRateMissing = QLabel(self.groupBox_20)
        self.labelHartRateMissing.setObjectName(u"labelHartRateMissing")
        self.labelHartRateMissing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.labelHartRateMissing, 4, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_20)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.dockWidgetStatistics.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidgetStatistics)
        self.dockWidgetFileInfo = QDockWidget(MainWindow)
        self.dockWidgetFileInfo.setObjectName(u"dockWidgetFileInfo")
        self.dockWidgetFileInfo.setMinimumSize(QSize(544, 113))
        self.dockWidgetFileInfo.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetFileInfo.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 5, 0, 0)
        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 507, 162))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 9, 0)
        self.labelSport = QLabel(self.scrollAreaWidgetContents)
        self.labelSport.setObjectName(u"labelSport")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelSport)

        self.inputSport = QLineEdit(self.scrollAreaWidgetContents)
        self.inputSport.setObjectName(u"inputSport")
        self.inputSport.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputSport)

        self.lableFile = QLabel(self.scrollAreaWidgetContents)
        self.lableFile.setObjectName(u"lableFile")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lableFile)

        self.labelFilePath = QLineEdit(self.scrollAreaWidgetContents)
        self.labelFilePath.setObjectName(u"labelFilePath")
        self.labelFilePath.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelFilePath)

        self.labelLapsNo = QLabel(self.scrollAreaWidgetContents)
        self.labelLapsNo.setObjectName(u"labelLapsNo")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelLapsNo)

        self.inputLaps = QLineEdit(self.scrollAreaWidgetContents)
        self.inputLaps.setObjectName(u"inputLaps")
        self.inputLaps.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputLaps)

        self.labelID = QLabel(self.scrollAreaWidgetContents)
        self.labelID.setObjectName(u"labelID")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelID)

        self.inputId = QLineEdit(self.scrollAreaWidgetContents)
        self.inputId.setObjectName(u"inputId")
        self.inputId.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputId)

        self.labelTrackPointsNo = QLabel(self.scrollAreaWidgetContents)
        self.labelTrackPointsNo.setObjectName(u"labelTrackPointsNo")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelTrackPointsNo)

        self.inputTrackPoints = QLineEdit(self.scrollAreaWidgetContents)
        self.inputTrackPoints.setObjectName(u"inputTrackPoints")
        self.inputTrackPoints.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.inputTrackPoints)

        self.labelNotes = QLabel(self.scrollAreaWidgetContents)
        self.labelNotes.setObjectName(u"labelNotes")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelNotes)

        self.inputNotes = QLineEdit(self.scrollAreaWidgetContents)
        self.inputNotes.setObjectName(u"inputNotes")
        self.inputNotes.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.inputNotes)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.dockWidgetFileInfo.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidgetFileInfo)
        self.dockWidgetProcessing = QDockWidget(MainWindow)
        self.dockWidgetProcessing.setObjectName(u"dockWidgetProcessing")
        self.dockWidgetProcessing.setMinimumSize(QSize(544, 98))
        self.dockWidgetProcessing.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetProcessing.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName(u"dockWidgetContents_8")
        self.verticalLayout_9 = QVBoxLayout(self.dockWidgetContents_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 5, 0, 0)
        self.scrollArea_3 = QScrollArea(self.dockWidgetContents_8)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 524, 69))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, 9, 0)
        self.label_171 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_171.setObjectName(u"label_171")
        sizePolicy.setHeightForWidth(self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_171, 3, 0, 1, 1)

        self.buttonCalculateSpeed = QPushButton(self.scrollAreaWidgetContents_3)
        self.buttonCalculateSpeed.setObjectName(u"buttonCalculateSpeed")

        self.gridLayout_2.addWidget(self.buttonCalculateSpeed, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.startDateTime_2 = QDateTimeEdit(self.scrollAreaWidgetContents_3)
        self.startDateTime_2.setObjectName(u"startDateTime_2")
        self.startDateTime_2.setCalendarPopup(True)
        self.startDateTime_2.setTimeSpec(Qt.UTC)

        self.gridLayout_2.addWidget(self.startDateTime_2, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.buttonCalculateSpeed_3 = QPushButton(self.scrollAreaWidgetContents_3)
        self.buttonCalculateSpeed_3.setObjectName(u"buttonCalculateSpeed_3")

        self.gridLayout_2.addWidget(self.buttonCalculateSpeed_3, 3, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_9.addWidget(self.scrollArea_3)

        self.dockWidgetProcessing.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidgetProcessing)
        self.dockWidgetFind = QDockWidget(MainWindow)
        self.dockWidgetFind.setObjectName(u"dockWidgetFind")
        self.dockWidgetFind.setMinimumSize(QSize(544, 98))
        self.dockWidgetFind.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetFind.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_9 = QWidget()
        self.dockWidgetContents_9.setObjectName(u"dockWidgetContents_9")
        self.verticalLayout_11 = QVBoxLayout(self.dockWidgetContents_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 5, 0, 0)
        self.scrollArea_4 = QScrollArea(self.dockWidgetContents_9)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QFrame.Plain)
        self.scrollArea_4.setLineWidth(0)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 507, 506))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frameFilders1_2 = QFrame(self.scrollAreaWidgetContents_4)
        self.frameFilders1_2.setObjectName(u"frameFilders1_2")
        self.frameFilders1_2.setFrameShape(QFrame.NoFrame)
        self.frameFilders1_2.setFrameShadow(QFrame.Raised)
        self.formLayout_6 = QFormLayout(self.frameFilders1_2)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(0, 0, 9, 0)
        self.label_167 = QLabel(self.frameFilders1_2)
        self.label_167.setObjectName(u"label_167")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_167)

        self.editFindByAltitude = QLineEdit(self.frameFilders1_2)
        self.editFindByAltitude.setObjectName(u"editFindByAltitude")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.editFindByAltitude)

        self.label_168 = QLabel(self.frameFilders1_2)
        self.label_168.setObjectName(u"label_168")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_168)

        self.editFindByHartRate = QLineEdit(self.frameFilders1_2)
        self.editFindByHartRate.setObjectName(u"editFindByHartRate")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.editFindByHartRate)

        self.label_165 = QLabel(self.frameFilders1_2)
        self.label_165.setObjectName(u"label_165")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_165)

        self.label_164 = QLabel(self.frameFilders1_2)
        self.label_164.setObjectName(u"label_164")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_164)

        self.label_166 = QLabel(self.frameFilders1_2)
        self.label_166.setObjectName(u"label_166")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_166)

        self.editFindByLatitude = QLineEdit(self.frameFilders1_2)
        self.editFindByLatitude.setObjectName(u"editFindByLatitude")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.editFindByLatitude)

        self.editFindByLongitude = QLineEdit(self.frameFilders1_2)
        self.editFindByLongitude.setObjectName(u"editFindByLongitude")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.editFindByLongitude)

        self.editFindByTime = QLineEdit(self.frameFilders1_2)
        self.editFindByTime.setObjectName(u"editFindByTime")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.editFindByTime)

        self.label_158 = QLabel(self.frameFilders1_2)
        self.label_158.setObjectName(u"label_158")

        self.formLayout_6.setWidget(5, QFormLayout.LabelRole, self.label_158)

        self.editFindByDistance = QLineEdit(self.frameFilders1_2)
        self.editFindByDistance.setObjectName(u"editFindByDistance")

        self.formLayout_6.setWidget(5, QFormLayout.FieldRole, self.editFindByDistance)

        self.label_159 = QLabel(self.frameFilders1_2)
        self.label_159.setObjectName(u"label_159")

        self.formLayout_6.setWidget(6, QFormLayout.LabelRole, self.label_159)

        self.editFindByCalculatedDistance = QLineEdit(self.frameFilders1_2)
        self.editFindByCalculatedDistance.setObjectName(u"editFindByCalculatedDistance")

        self.formLayout_6.setWidget(6, QFormLayout.FieldRole, self.editFindByCalculatedDistance)

        self.label_160 = QLabel(self.frameFilders1_2)
        self.label_160.setObjectName(u"label_160")

        self.formLayout_6.setWidget(7, QFormLayout.LabelRole, self.label_160)

        self.editFindBySpeed = QLineEdit(self.frameFilders1_2)
        self.editFindBySpeed.setObjectName(u"editFindBySpeed")

        self.formLayout_6.setWidget(7, QFormLayout.FieldRole, self.editFindBySpeed)

        self.label_161 = QLabel(self.frameFilders1_2)
        self.label_161.setObjectName(u"label_161")

        self.formLayout_6.setWidget(8, QFormLayout.LabelRole, self.label_161)

        self.editFindByCalculatedSpeed = QLineEdit(self.frameFilders1_2)
        self.editFindByCalculatedSpeed.setObjectName(u"editFindByCalculatedSpeed")

        self.formLayout_6.setWidget(8, QFormLayout.FieldRole, self.editFindByCalculatedSpeed)

        self.label_162 = QLabel(self.frameFilders1_2)
        self.label_162.setObjectName(u"label_162")

        self.formLayout_6.setWidget(9, QFormLayout.LabelRole, self.label_162)

        self.editFindBySensorState = QLineEdit(self.frameFilders1_2)
        self.editFindBySensorState.setObjectName(u"editFindBySensorState")

        self.formLayout_6.setWidget(9, QFormLayout.FieldRole, self.editFindBySensorState)

        self.groupBoxFilterButtons_2 = QGroupBox(self.frameFilders1_2)
        self.groupBoxFilterButtons_2.setObjectName(u"groupBoxFilterButtons_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBoxFilterButtons_2.sizePolicy().hasHeightForWidth())
        self.groupBoxFilterButtons_2.setSizePolicy(sizePolicy3)
        self.groupBoxFilterButtons_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBoxFilterButtons_2.setFlat(True)
        self.verticalLayout_12 = QVBoxLayout(self.groupBoxFilterButtons_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButtonFind = QPushButton(self.groupBoxFilterButtons_2)
        self.pushButtonFind.setObjectName(u"pushButtonFind")

        self.verticalLayout_12.addWidget(self.pushButtonFind)

        self.pushButtonFindClear = QPushButton(self.groupBoxFilterButtons_2)
        self.pushButtonFindClear.setObjectName(u"pushButtonFindClear")

        self.verticalLayout_12.addWidget(self.pushButtonFindClear)


        self.formLayout_6.setWidget(10, QFormLayout.FieldRole, self.groupBoxFilterButtons_2)


        self.verticalLayout_14.addWidget(self.frameFilders1_2)

        self.groupBox_28 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_28)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_163 = QLabel(self.groupBox_28)
        self.label_163.setObjectName(u"label_163")
        sizePolicy2.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.label_163)

        self.spinBoxMarkStatSelectRange = QDoubleSpinBox(self.groupBox_28)
        self.spinBoxMarkStatSelectRange.setObjectName(u"spinBoxMarkStatSelectRange")

        self.verticalLayout_13.addWidget(self.spinBoxMarkStatSelectRange)

        self.markStatSelColor = QPushButton(self.groupBox_28)
        self.markStatSelColor.setObjectName(u"markStatSelColor")
        self.markStatSelColor.setFocusPolicy(Qt.NoFocus)
        self.markStatSelColor.setAutoFillBackground(True)
        self.markStatSelColor.setFlat(True)

        self.verticalLayout_13.addWidget(self.markStatSelColor)

        self.pushButtonMarkStat = QPushButton(self.groupBox_28)
        self.pushButtonMarkStat.setObjectName(u"pushButtonMarkStat")

        self.verticalLayout_13.addWidget(self.pushButtonMarkStat)


        self.verticalLayout_14.addWidget(self.groupBox_28)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_11.addWidget(self.scrollArea_4)

        self.dockWidgetFind.setWidget(self.dockWidgetContents_9)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidgetFind)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.labelSport.setBuddy(self.inputSport)
        self.lableFile.setBuddy(self.labelFilePath)
        self.labelLapsNo.setBuddy(self.inputLaps)
        self.labelID.setBuddy(self.inputId)
        self.labelTrackPointsNo.setBuddy(self.inputTrackPoints)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionClear)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(shortcut)
        self.actionClear.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionclose.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.dockWidgetFiltering.setWindowTitle(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.doubleSpinBox_31.setSpecialValueText("")
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.doubleSpinBox_25.setSpecialValueText("")
        self.doubleSpinBox_16.setSpecialValueText("")
        self.doubleSpinBox_22.setSpecialValueText("")
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Calculated distance", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Calculated speed", None))
        self.dateTimeEdit_4.setSpecialValueText("")
        self.dateTimeEdit_4.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy HH:mm:ss.zzz t", None))
        self.doubleSpinBox_27.setSpecialValueText("")
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Hart rate", None))
        self.doubleSpinBox_28.setSpecialValueText("")
        self.doubleSpinBox_24.setSpecialValueText("")
        self.doubleSpinBox_29.setSpecialValueText("")
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Sensor state", None))
        self.doubleSpinBox_26.setSpecialValueText("")
        self.doubleSpinBox_18.setSpecialValueText("")
        self.doubleSpinBox_32.setSpecialValueText("")
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.doubleSpinBox_15.setSpecialValueText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.doubleSpinBox_30.setSpecialValueText("")
        self.doubleSpinBox_17.setSpecialValueText("")
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.doubleSpinBox_21.setSpecialValueText("")
        self.dateTimeEdit_3.setSpecialValueText("")
        self.dateTimeEdit_3.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy HH:mm:ss.zzz t", None))
        self.doubleSpinBox_23.setSpecialValueText("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Absent", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Present", None))

        self.dockWidgetStatistics.setWindowTitle(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Calculated distance", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Avg:", None))
        self.labelCalculatedDistanceMaxM.setText("")
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.labelCalculatedDistanceAvgM.setText("")
        self.labelCalculatedDistanceMinM.setText("")
        self.labelCalculatedDistanceAvgKM.setText("")
        self.labelCalculatedDistanceMaxKM.setText("")
        self.labelCalculatedDistanceMinKM.setText("")
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Missing:", None))
        self.labelCalculatedDistanceMissing.setText("")
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.labelDistanceMissing.setText("")
        self.labelDistanceMaxKM.setText("")
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Avg:", None))
        self.labelDistanceMinKM.setText("")
        self.labelDistanceAvgM.setText("")
        self.labelDistanceMaxM.setText("")
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.labelDistanceAvgKM.setText("")
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.labelDistanceMinM.setText("")
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Missing:", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Calculated speed", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"m/h", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.labelCalculatedSpeedMissing.setText("")
        self.labelCalculatedSpeedMaxKMPH.setText("")
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"km/h", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Missing:", None))
        self.labelCalculatedSpeedAvgMPH.setText("")
        self.labelCalculatedSpeedMinMPH.setText("")
        self.labelCalculatedSpeedMinKMPH.setText("")
        self.labelCalculatedSpeedAvgKMPH.setText("")
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Avg:", None))
        self.labelCalculatedSpeedMaxMPH.setText("")
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.labelSpeedAvgKMPH.setText("")
        self.labelSpeedMinKMPH.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"m/h", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.labelSpeedMaxKMPH.setText("")
        self.labelSpeedAvgMPH.setText("")
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.labelSpeedMaxMPH.setText("")
        self.labelSpeedMinMPH.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Avg:", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"km/h", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Missing:", None))
        self.labelSpeedMissing.setText("")
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Avg:", None))
        self.label_128.setText("")
        self.labelAltitudeMin.setText("")
        self.labelAltitudeMax.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.labelAltitudeAvg.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Missing:", None))
        self.labelAltitudeMissing.setText("")
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Avg:", None))
        self.label_122.setText("")
        self.labelLongitudeMin.setText("")
        self.labelLongitudeMax.setText("")
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.labelLongitudeAvg.setText("")
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Missing:", None))
        self.labelLongitudeMissing.setText("")
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Avg:", None))
        self.label_116.setText("")
        self.labelLatitudeMin.setText("")
        self.labelLatitudeMax.setText("")
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.labelLatitudeAvg.setText("")
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Missing:", None))
        self.labelLatitudeMissing.setText("")
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Hart rate", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Avg:", None))
        self.label_110.setText("")
        self.labelHartRateMin.setText("")
        self.labelHartRateMax.setText("")
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.labelHartRateAvg.setText("")
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"bpm", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Missing:", None))
        self.labelHartRateMissing.setText("")
        self.dockWidgetFileInfo.setWindowTitle(QCoreApplication.translate("MainWindow", u"File info", None))
        self.labelSport.setText(QCoreApplication.translate("MainWindow", u"Sport", None))
#if QT_CONFIG(tooltip)
        self.inputSport.setToolTip(QCoreApplication.translate("MainWindow", u"Sport", None))
#endif // QT_CONFIG(tooltip)
        self.lableFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.labelLapsNo.setText(QCoreApplication.translate("MainWindow", u"Laps", None))
#if QT_CONFIG(tooltip)
        self.inputLaps.setToolTip(QCoreApplication.translate("MainWindow", u"Number of laps", None))
#endif // QT_CONFIG(tooltip)
        self.labelID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.labelTrackPointsNo.setText(QCoreApplication.translate("MainWindow", u"Track points:", None))
#if QT_CONFIG(tooltip)
        self.inputTrackPoints.setToolTip(QCoreApplication.translate("MainWindow", u"Number of track points", None))
#endif // QT_CONFIG(tooltip)
        self.labelNotes.setText(QCoreApplication.translate("MainWindow", u"Notes:", None))
        self.dockWidgetProcessing.setWindowTitle(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.buttonCalculateSpeed.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.startDateTime_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy HH:mm:ss.zzz t", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Shift time", None))
        self.buttonCalculateSpeed_3.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Time shifting", None))
        self.dockWidgetFind.setWindowTitle(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Altitude:", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Hart rate:", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Latitude:", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Longitude:", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Distance:", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Calculated distance:", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Calculated speed:", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Sensor state", None))
        self.groupBoxFilterButtons_2.setTitle("")
        self.pushButtonFind.setText(QCoreApplication.translate("MainWindow", u"Find..", None))
        self.pushButtonFindClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Mark stationary", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Range:", None))
        self.markStatSelColor.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.pushButtonMarkStat.setText(QCoreApplication.translate("MainWindow", u"Mark ", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

