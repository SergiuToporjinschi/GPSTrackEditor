# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'marking_dock.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDockWidget, QDoubleSpinBox,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QToolButton, QTreeView, QVBoxLayout, QWidget)
import gpstracker_rc

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(676, 826)
        DockWidget.setFloating(False)
        DockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.actionMaximize = QAction(DockWidget)
        self.actionMaximize.setObjectName(u"actionMaximize")
        self.actionMaximize.setMenuRole(QAction.NoRole)
        self.actionDelete = QAction(DockWidget)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionDelete.setMenuRole(QAction.NoRole)
        self.actionActivate = QAction(DockWidget)
        self.actionActivate.setObjectName(u"actionActivate")
        self.actionActivate.setCheckable(True)
        self.actionActivate.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionSelectAll = QAction(DockWidget)
        self.actionSelectAll.setObjectName(u"actionSelectAll")
        self.actionSelectAll.setMenuRole(QAction.NoRole)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.dockWidgetContents)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QFrame.Plain)
        self.scrollArea_4.setLineWidth(0)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 676, 802))
        self.scrollAreaWidgetContents_4.setAutoFillBackground(True)
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.scrollAreaWidgetContents_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setHandleWidth(10)
        self.frameTop = QFrame(self.splitter_2)
        self.frameTop.setObjectName(u"frameTop")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameTop.sizePolicy().hasHeightForWidth())
        self.frameTop.setSizePolicy(sizePolicy)
        self.frameTop.setFrameShape(QFrame.NoFrame)
        self.frameTop.setFrameShadow(QFrame.Plain)
        self.frameTop.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frameTop)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayoutAddToolbar = QHBoxLayout()
        self.horizontalLayoutAddToolbar.setObjectName(u"horizontalLayoutAddToolbar")
        self.toolDelete = QToolButton(self.frameTop)
        self.toolDelete.setObjectName(u"toolDelete")
        self.toolDelete.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/resources/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolDelete.setIcon(icon)
        self.toolDelete.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolDelete.setAutoRaise(True)
        self.toolDelete.setProperty("activeOnState", 1)

        self.horizontalLayoutAddToolbar.addWidget(self.toolDelete)

        self.toolEdit = QToolButton(self.frameTop)
        self.toolEdit.setObjectName(u"toolEdit")
        self.toolEdit.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/resources/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolEdit.setIcon(icon1)
        self.toolEdit.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolEdit.setAutoRaise(True)
        self.toolEdit.setProperty("activeOnState", 1)

        self.horizontalLayoutAddToolbar.addWidget(self.toolEdit)

        self.toolActivateAll = QToolButton(self.frameTop)
        self.toolActivateAll.setObjectName(u"toolActivateAll")
        icon2 = QIcon()
        icon2.addFile(u":/resources/icons/apply-all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolActivateAll.setIcon(icon2)
        self.toolActivateAll.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolActivateAll.setAutoRaise(True)
        self.toolActivateAll.setProperty("activeOnState", 1)

        self.horizontalLayoutAddToolbar.addWidget(self.toolActivateAll)

        self.toolClearAll = QToolButton(self.frameTop)
        self.toolClearAll.setObjectName(u"toolClearAll")
        icon3 = QIcon()
        icon3.addFile(u":/resources/icons/clear-all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolClearAll.setIcon(icon3)
        self.toolClearAll.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolClearAll.setAutoRaise(True)
        self.toolClearAll.setProperty("activeOnState", 1)

        self.horizontalLayoutAddToolbar.addWidget(self.toolClearAll)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutAddToolbar.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayoutAddToolbar)

        self.treeViewMarker = QTreeView(self.frameTop)
        self.treeViewMarker.setObjectName(u"treeViewMarker")
        self.treeViewMarker.setAlternatingRowColors(True)
        self.treeViewMarker.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeViewMarker.setUniformRowHeights(True)
        self.treeViewMarker.setAnimated(True)
        self.treeViewMarker.setProperty("activeOnState", 1)

        self.verticalLayout_3.addWidget(self.treeViewMarker)

        self.splitter_2.addWidget(self.frameTop)
        self.frameBottom = QFrame(self.splitter_2)
        self.frameBottom.setObjectName(u"frameBottom")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameBottom.sizePolicy().hasHeightForWidth())
        self.frameBottom.setSizePolicy(sizePolicy1)
        self.frameBottom.setFrameShape(QFrame.NoFrame)
        self.frameBottom.setFrameShadow(QFrame.Plain)
        self.frameBottom.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frameBottom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalToolbar = QHBoxLayout()
        self.horizontalToolbar.setObjectName(u"horizontalToolbar")
        self.label_169 = QLabel(self.frameBottom)
        self.label_169.setObjectName(u"label_169")

        self.horizontalToolbar.addWidget(self.label_169)

        self.editMarkerName = QLineEdit(self.frameBottom)
        self.editMarkerName.setObjectName(u"editMarkerName")

        self.horizontalToolbar.addWidget(self.editMarkerName)

        self.pushAdd = QPushButton(self.frameBottom)
        self.pushAdd.setObjectName(u"pushAdd")

        self.horizontalToolbar.addWidget(self.pushAdd)

        self.pushCancelEdit = QPushButton(self.frameBottom)
        self.pushCancelEdit.setObjectName(u"pushCancelEdit")
        self.pushCancelEdit.setEnabled(False)
        self.pushCancelEdit.setProperty("activeOnState", 2)

        self.horizontalToolbar.addWidget(self.pushCancelEdit)


        self.verticalLayout_2.addLayout(self.horizontalToolbar)

        self.tabWidget = QTabWidget(self.frameBottom)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabCustom = QWidget()
        self.tabCustom.setObjectName(u"tabCustom")
        self.formLayout = QFormLayout(self.tabCustom)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(9, -1, 9, -1)
        self.label_167 = QLabel(self.tabCustom)
        self.label_167.setObjectName(u"label_167")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_167)

        self.editCustomColExpression = QLineEdit(self.tabCustom)
        self.editCustomColExpression.setObjectName(u"editCustomColExpression")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editCustomColExpression)

        self.tabWidget.addTab(self.tabCustom, "")
        self.tabStationary = QWidget()
        self.tabStationary.setObjectName(u"tabStationary")
        self.formLayout_2 = QFormLayout(self.tabStationary)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_163 = QLabel(self.tabStationary)
        self.label_163.setObjectName(u"label_163")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy2)
        self.label_163.setMinimumSize(QSize(106, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_163)

        self.spinBoxStatTolerance = QDoubleSpinBox(self.tabStationary)
        self.spinBoxStatTolerance.setObjectName(u"spinBoxStatTolerance")
        self.spinBoxStatTolerance.setMaximumSize(QSize(16777210, 16777215))
        self.spinBoxStatTolerance.setContextMenuPolicy(Qt.PreventContextMenu)
        self.spinBoxStatTolerance.setToolTipDuration(-8)
        self.spinBoxStatTolerance.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBoxStatTolerance)

        self.tabWidget.addTab(self.tabStationary, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.splitter_2.addWidget(self.frameBottom)

        self.verticalLayout_4.addWidget(self.splitter_2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.scrollArea_4)

        DockWidget.setWidget(self.dockWidgetContents)
#if QT_CONFIG(shortcut)
        self.label_167.setBuddy(self.editCustomColExpression)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.toolDelete, self.treeViewMarker)
        QWidget.setTabOrder(self.treeViewMarker, self.scrollArea_4)

        self.retranslateUi(DockWidget)
        self.actionSelectAll.triggered.connect(self.treeViewMarker.selectAll)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Marking", None))
        self.actionMaximize.setText(QCoreApplication.translate("DockWidget", u"Maximize", None))
#if QT_CONFIG(shortcut)
        self.actionMaximize.setShortcut(QCoreApplication.translate("DockWidget", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("DockWidget", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.actionDelete.setToolTip(QCoreApplication.translate("DockWidget", u"Delete current selected marker", None))
#endif // QT_CONFIG(tooltip)
        self.actionActivate.setText(QCoreApplication.translate("DockWidget", u"Active", None))
#if QT_CONFIG(tooltip)
        self.actionActivate.setToolTip(QCoreApplication.translate("DockWidget", u"Activates/deactivates current selected marker", None))
#endif // QT_CONFIG(tooltip)
        self.actionSelectAll.setText(QCoreApplication.translate("DockWidget", u"Select all", None))
#if QT_CONFIG(tooltip)
        self.actionSelectAll.setToolTip(QCoreApplication.translate("DockWidget", u"Select all records", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSelectAll.setShortcut(QCoreApplication.translate("DockWidget", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("DockWidget", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("DockWidget", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.toolEdit.setToolTip(QCoreApplication.translate("DockWidget", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.toolEdit.setText(QCoreApplication.translate("DockWidget", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.toolActivateAll.setToolTip(QCoreApplication.translate("DockWidget", u"Apply all", None))
#endif // QT_CONFIG(tooltip)
        self.toolActivateAll.setText(QCoreApplication.translate("DockWidget", u"Apply all", None))
#if QT_CONFIG(tooltip)
        self.toolClearAll.setToolTip(QCoreApplication.translate("DockWidget", u" Clear all", None))
#endif // QT_CONFIG(tooltip)
        self.toolClearAll.setText(QCoreApplication.translate("DockWidget", u" Clear all", None))
        self.label_169.setText(QCoreApplication.translate("DockWidget", u"Name:", None))
        self.editMarkerName.setPlaceholderText(QCoreApplication.translate("DockWidget", u"Marker name", None))
#if QT_CONFIG(tooltip)
        self.pushAdd.setToolTip(QCoreApplication.translate("DockWidget", u"Add marker", None))
#endif // QT_CONFIG(tooltip)
        self.pushAdd.setText(QCoreApplication.translate("DockWidget", u"Add", None))
#if QT_CONFIG(shortcut)
        self.pushAdd.setShortcut(QCoreApplication.translate("DockWidget", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushCancelEdit.setText(QCoreApplication.translate("DockWidget", u"Cancel", None))
        self.tabCustom.setProperty("markerCategory", QCoreApplication.translate("DockWidget", u"Custom", None))
        self.label_167.setText(QCoreApplication.translate("DockWidget", u"Expression:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCustom), QCoreApplication.translate("DockWidget", u"Custom", None))
        self.tabStationary.setProperty("markerCategory", QCoreApplication.translate("DockWidget", u"Stationary", None))
        self.label_163.setText(QCoreApplication.translate("DockWidget", u"Tolerance:", None))
        self.spinBoxStatTolerance.setProperty("markerCategory", QCoreApplication.translate("DockWidget", u"Stationary", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStationary), QCoreApplication.translate("DockWidget", u"Stationary", None))
    # retranslateUi

