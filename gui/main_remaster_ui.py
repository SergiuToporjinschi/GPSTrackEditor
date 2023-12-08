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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QTableView, QToolBar, QVBoxLayout,
    QWidget)
import gpstracker_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(497, 547)
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
        icon.addFile(u":/resources/icons/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u":/resources/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        icon2.addFile(u":/resources/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon3 = QIcon()
        icon3.addFile(u":/resources/icons/clear-all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClear.setIcon(icon3)
        self.actionclose = QAction(MainWindow)
        self.actionclose.setObjectName(u"actionclose")
        self.actionclose.setCheckable(True)
        icon4 = QIcon()
        iconThemeName = u"application-x-executable"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u":/resources/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.actionclose.setIcon(icon4)
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
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setMinimumSectionSize(30)

        self.verticalTableLayout.addWidget(self.tableView)

        self.sliderLayout = QVBoxLayout()
        self.sliderLayout.setObjectName(u"sliderLayout")

        self.verticalTableLayout.addLayout(self.sliderLayout)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 497, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

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
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

