# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'processing_dock.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateTimeEdit, QDockWidget,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter,
    QTabWidget, QTableView, QToolButton, QVBoxLayout,
    QWidget)
import gpstracker_rc

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(478, 676)
        DockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.dockWidgetContents)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 478, 652))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.buttonShiftTime = QPushButton(self.tab)
        self.buttonShiftTime.setObjectName(u"buttonShiftTime")

        self.gridLayout.addWidget(self.buttonShiftTime, 0, 2, 1, 1)

        self.startDateTime_2 = QDateTimeEdit(self.tab)
        self.startDateTime_2.setObjectName(u"startDateTime_2")
        self.startDateTime_2.setCalendarPopup(True)
        self.startDateTime_2.setTimeSpec(Qt.UTC)

        self.gridLayout.addWidget(self.startDateTime_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(self.tab_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.frame_5 = QFrame(self.splitter)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButtonDelete = QToolButton(self.frame_6)
        self.toolButtonDelete.setObjectName(u"toolButtonDelete")
        self.toolButtonDelete.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/resources/icons/delete-column.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonDelete.setIcon(icon)
        self.toolButtonDelete.setAutoRaise(True)
        self.toolButtonDelete.setProperty("activeOnState", 1)

        self.horizontalLayout_2.addWidget(self.toolButtonDelete)

        self.toolButtonEdit = QToolButton(self.frame_6)
        self.toolButtonEdit.setObjectName(u"toolButtonEdit")
        self.toolButtonEdit.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/resources/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonEdit.setIcon(icon1)
        self.toolButtonEdit.setAutoRaise(True)
        self.toolButtonEdit.setProperty("activeOnState", 1)

        self.horizontalLayout_2.addWidget(self.toolButtonEdit)

        self.toolButtonActivateAll = QToolButton(self.frame_6)
        self.toolButtonActivateAll.setObjectName(u"toolButtonActivateAll")
        self.toolButtonActivateAll.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(u":/resources/icons/apply-all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonActivateAll.setIcon(icon2)
        self.toolButtonActivateAll.setAutoRaise(True)
        self.toolButtonActivateAll.setProperty("activeOnState", 1)

        self.horizontalLayout_2.addWidget(self.toolButtonActivateAll)

        self.toolButtonDeactivateAll = QToolButton(self.frame_6)
        self.toolButtonDeactivateAll.setObjectName(u"toolButtonDeactivateAll")
        self.toolButtonDeactivateAll.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/resources/icons/clear-all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonDeactivateAll.setIcon(icon3)
        self.toolButtonDeactivateAll.setAutoRaise(True)
        self.toolButtonDeactivateAll.setProperty("activeOnState", 1)

        self.horizontalLayout_2.addWidget(self.toolButtonDeactivateAll)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.tableViewCol = QTableView(self.frame_5)
        self.tableViewCol.setObjectName(u"tableViewCol")
        self.tableViewCol.setAlternatingRowColors(True)
        self.tableViewCol.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewCol.setProperty("activeOnState", 1)
        self.tableViewCol.verticalHeader().setMinimumSectionSize(20)
        self.tableViewCol.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_3.addWidget(self.tableViewCol)

        self.splitter.addWidget(self.frame_5)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEditName = QLineEdit(self.frame)
        self.lineEditName.setObjectName(u"lineEditName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditName)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEditExpression = QLineEdit(self.frame)
        self.lineEditExpression.setObjectName(u"lineEditExpression")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditExpression)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAddColumn = QPushButton(self.frame_4)
        self.pushButtonAddColumn.setObjectName(u"pushButtonAddColumn")
        icon4 = QIcon()
        icon4.addFile(u":/resources/icons/add-column.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddColumn.setIcon(icon4)

        self.horizontalLayout.addWidget(self.pushButtonAddColumn)

        self.pushButtonCancelEdit = QPushButton(self.frame_4)
        self.pushButtonCancelEdit.setObjectName(u"pushButtonCancelEdit")
        self.pushButtonCancelEdit.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/resources/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCancelEdit.setIcon(icon5)
        self.pushButtonCancelEdit.setProperty("activeOnState", 2)

        self.horizontalLayout.addWidget(self.pushButtonCancelEdit)


        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.frame_4)

        self.splitter.addWidget(self.frame)

        self.verticalLayout_4.addWidget(self.splitter)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea_3)

        DockWidget.setWidget(self.dockWidgetContents)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.lineEditName)
        self.label_3.setBuddy(self.lineEditExpression)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.toolButtonDelete, self.toolButtonEdit)
        QWidget.setTabOrder(self.toolButtonEdit, self.tableViewCol)
        QWidget.setTabOrder(self.tableViewCol, self.lineEditName)
        QWidget.setTabOrder(self.lineEditName, self.lineEditExpression)
        QWidget.setTabOrder(self.lineEditExpression, self.pushButtonAddColumn)
        QWidget.setTabOrder(self.pushButtonAddColumn, self.pushButtonCancelEdit)
        QWidget.setTabOrder(self.pushButtonCancelEdit, self.startDateTime_2)
        QWidget.setTabOrder(self.startDateTime_2, self.scrollArea_3)
        QWidget.setTabOrder(self.scrollArea_3, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.buttonShiftTime)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Processing", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Time shifting", None))
        self.buttonShiftTime.setText(QCoreApplication.translate("DockWidget", u"Shift time", None))
        self.startDateTime_2.setDisplayFormat(QCoreApplication.translate("DockWidget", u"dd-MM-yyyy HH:mm:ss.zzz t", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"Time shift", None))
#if QT_CONFIG(tooltip)
        self.toolButtonDelete.setToolTip(QCoreApplication.translate("DockWidget", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonDelete.setText(QCoreApplication.translate("DockWidget", u" Delete", None))
#if QT_CONFIG(tooltip)
        self.toolButtonEdit.setToolTip(QCoreApplication.translate("DockWidget", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonEdit.setText(QCoreApplication.translate("DockWidget", u" Edit", None))
#if QT_CONFIG(tooltip)
        self.toolButtonActivateAll.setToolTip(QCoreApplication.translate("DockWidget", u"Activate all", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonActivateAll.setText(QCoreApplication.translate("DockWidget", u"Activate all", None))
#if QT_CONFIG(tooltip)
        self.toolButtonDeactivateAll.setToolTip(QCoreApplication.translate("DockWidget", u"Deactivate all", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonDeactivateAll.setText(QCoreApplication.translate("DockWidget", u"Deactivate all", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DockWidget", u"Stats with letter, no space, no special characters \n"
"[function name]\n"
"Column name should start with \"row.\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Name", None))
#if QT_CONFIG(tooltip)
        self.lineEditName.setToolTip(QCoreApplication.translate("DockWidget", u"Stats with letter, no space, no special characters \n"
"[function name]\n"
"Column name should start with \"row.\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Expression:", None))
        self.pushButtonAddColumn.setText(QCoreApplication.translate("DockWidget", u" Add column", None))
#if QT_CONFIG(shortcut)
        self.pushButtonAddColumn.setShortcut(QCoreApplication.translate("DockWidget", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButtonCancelEdit.setText(QCoreApplication.translate("DockWidget", u"Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Calculated Columns", None))
    # retranslateUi

