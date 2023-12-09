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
        self.frameTop.setFrameShape(QFrame.NoFrame)
        self.frameTop.setFrameShadow(QFrame.Plain)
        self.frameTop.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frameTop)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolDelete = QToolButton(self.frameTop)
        self.toolDelete.setObjectName(u"toolDelete")
        icon = QIcon()
        icon.addFile(u":/resources/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolDelete.setIcon(icon)
        self.toolDelete.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.toolDelete)

        self.toolActivate = QToolButton(self.frameTop)
        self.toolActivate.setObjectName(u"toolActivate")
        self.toolActivate.setMinimumSize(QSize(45, 0))
        icon1 = QIcon()
        icon1.addFile(u":/resources/icons/apply.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolActivate.setIcon(icon1)
        self.toolActivate.setCheckable(True)
        self.toolActivate.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.toolActivate)

        self.toolActivateAll = QToolButton(self.frameTop)
        self.toolActivateAll.setObjectName(u"toolActivateAll")
        icon2 = QIcon()
        icon2.addFile(u":/resources/icons/apply-all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolActivateAll.setIcon(icon2)
        self.toolActivateAll.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.toolActivateAll)

        self.toolClearAll = QToolButton(self.frameTop)
        self.toolClearAll.setObjectName(u"toolClearAll")
        icon3 = QIcon()
        icon3.addFile(u":/resources/icons/clear-all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolClearAll.setIcon(icon3)
        self.toolClearAll.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.toolClearAll)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.treeViewMarker = QTreeView(self.frameTop)
        self.treeViewMarker.setObjectName(u"treeViewMarker")
        self.treeViewMarker.setAlternatingRowColors(True)
        self.treeViewMarker.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.treeViewMarker.setUniformRowHeights(True)
        self.treeViewMarker.setAnimated(True)

        self.verticalLayout_3.addWidget(self.treeViewMarker)

        self.splitter_2.addWidget(self.frameTop)
        self.frameBottom = QFrame(self.splitter_2)
        self.frameBottom.setObjectName(u"frameBottom")
        self.frameBottom.setFrameShape(QFrame.NoFrame)
        self.frameBottom.setFrameShadow(QFrame.Plain)
        self.frameBottom.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frameBottom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayoutTemplateToolbar = QHBoxLayout()
        self.horizontalLayoutTemplateToolbar.setObjectName(u"horizontalLayoutTemplateToolbar")
        self.horizontalLayoutTemplateToolbar.setContentsMargins(0, -1, -1, -1)
        self.label_169 = QLabel(self.frameBottom)
        self.label_169.setObjectName(u"label_169")

        self.horizontalLayoutTemplateToolbar.addWidget(self.label_169)

        self.editMarkerName = QLineEdit(self.frameBottom)
        self.editMarkerName.setObjectName(u"editMarkerName")

        self.horizontalLayoutTemplateToolbar.addWidget(self.editMarkerName)

        self.pushAdd = QPushButton(self.frameBottom)
        self.pushAdd.setObjectName(u"pushAdd")

        self.horizontalLayoutTemplateToolbar.addWidget(self.pushAdd)


        self.verticalLayout_2.addLayout(self.horizontalLayoutTemplateToolbar)

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

        self.editAttrAltitude = QLineEdit(self.tabCustom)
        self.editAttrAltitude.setObjectName(u"editAttrAltitude")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editAttrAltitude)

        self.label_164 = QLabel(self.tabCustom)
        self.label_164.setObjectName(u"label_164")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_164)

        self.editAttrTime = QLineEdit(self.tabCustom)
        self.editAttrTime.setObjectName(u"editAttrTime")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editAttrTime)

        self.label_168 = QLabel(self.tabCustom)
        self.label_168.setObjectName(u"label_168")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_168)

        self.editAttrHartRate = QLineEdit(self.tabCustom)
        self.editAttrHartRate.setObjectName(u"editAttrHartRate")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editAttrHartRate)

        self.label_162 = QLabel(self.tabCustom)
        self.label_162.setObjectName(u"label_162")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_162)

        self.editAttrSensorState = QLineEdit(self.tabCustom)
        self.editAttrSensorState.setObjectName(u"editAttrSensorState")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.editAttrSensorState)

        self.label_165 = QLabel(self.tabCustom)
        self.label_165.setObjectName(u"label_165")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_165)

        self.editAttrLatitude = QLineEdit(self.tabCustom)
        self.editAttrLatitude.setObjectName(u"editAttrLatitude")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.editAttrLatitude)

        self.label_166 = QLabel(self.tabCustom)
        self.label_166.setObjectName(u"label_166")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_166)

        self.editAttrLongitude = QLineEdit(self.tabCustom)
        self.editAttrLongitude.setObjectName(u"editAttrLongitude")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.editAttrLongitude)

        self.label_158 = QLabel(self.tabCustom)
        self.label_158.setObjectName(u"label_158")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_158)

        self.editAttrDistance = QLineEdit(self.tabCustom)
        self.editAttrDistance.setObjectName(u"editAttrDistance")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.editAttrDistance)

        self.label_159 = QLabel(self.tabCustom)
        self.label_159.setObjectName(u"label_159")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_159)

        self.editAttrCalculatedDistance = QLineEdit(self.tabCustom)
        self.editAttrCalculatedDistance.setObjectName(u"editAttrCalculatedDistance")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.editAttrCalculatedDistance)

        self.label_160 = QLabel(self.tabCustom)
        self.label_160.setObjectName(u"label_160")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_160)

        self.editAttrSpeed = QLineEdit(self.tabCustom)
        self.editAttrSpeed.setObjectName(u"editAttrSpeed")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.editAttrSpeed)

        self.label_161 = QLabel(self.tabCustom)
        self.label_161.setObjectName(u"label_161")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_161)

        self.editAttrCalculatedSpeed = QLineEdit(self.tabCustom)
        self.editAttrCalculatedSpeed.setObjectName(u"editAttrCalculatedSpeed")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.editAttrCalculatedSpeed)

        self.tabWidget.addTab(self.tabCustom, "")
        self.tabStationary = QWidget()
        self.tabStationary.setObjectName(u"tabStationary")
        self.formLayout_2 = QFormLayout(self.tabStationary)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_163 = QLabel(self.tabStationary)
        self.label_163.setObjectName(u"label_163")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy)
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
        self.label_169.setBuddy(self.editAttrAltitude)
        self.label_167.setBuddy(self.editAttrAltitude)
        self.label_164.setBuddy(self.editAttrTime)
        self.label_168.setBuddy(self.editAttrHartRate)
        self.label_162.setBuddy(self.editAttrSensorState)
        self.label_165.setBuddy(self.editAttrLatitude)
        self.label_166.setBuddy(self.editAttrLongitude)
        self.label_158.setBuddy(self.editAttrDistance)
        self.label_159.setBuddy(self.editAttrCalculatedDistance)
        self.label_160.setBuddy(self.editAttrSpeed)
        self.label_161.setBuddy(self.editAttrCalculatedSpeed)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.toolDelete, self.toolActivate)
        QWidget.setTabOrder(self.toolActivate, self.treeViewMarker)
        QWidget.setTabOrder(self.treeViewMarker, self.pushAdd)
        QWidget.setTabOrder(self.pushAdd, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.scrollArea_4)
        QWidget.setTabOrder(self.scrollArea_4, self.spinBoxStatTolerance)

        self.retranslateUi(DockWidget)

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
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("DockWidget", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("DockWidget", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.toolActivate.setToolTip(QCoreApplication.translate("DockWidget", u"Apply", None))
#endif // QT_CONFIG(tooltip)
        self.toolActivate.setText(QCoreApplication.translate("DockWidget", u"Apply", None))
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
        self.pushAdd.setText(QCoreApplication.translate("DockWidget", u"Add", None))
        self.tabCustom.setProperty("markerCategory", QCoreApplication.translate("DockWidget", u"Custom", None))
        self.label_167.setText(QCoreApplication.translate("DockWidget", u"Altitude:", None))
        self.label_164.setText(QCoreApplication.translate("DockWidget", u"Time:", None))
        self.label_168.setText(QCoreApplication.translate("DockWidget", u"Hart rate:", None))
        self.label_162.setText(QCoreApplication.translate("DockWidget", u"Sensor state", None))
        self.label_165.setText(QCoreApplication.translate("DockWidget", u"Latitude:", None))
        self.label_166.setText(QCoreApplication.translate("DockWidget", u"Longitude:", None))
        self.label_158.setText(QCoreApplication.translate("DockWidget", u"Distance:", None))
        self.label_159.setText(QCoreApplication.translate("DockWidget", u"Calculated distance:", None))
        self.label_160.setText(QCoreApplication.translate("DockWidget", u"Speed:", None))
        self.label_161.setText(QCoreApplication.translate("DockWidget", u"Calculated speed:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCustom), QCoreApplication.translate("DockWidget", u"Custom", None))
        self.tabStationary.setProperty("markerCategory", QCoreApplication.translate("DockWidget", u"Stationary", None))
        self.label_163.setText(QCoreApplication.translate("DockWidget", u"Tolerance:", None))
        self.spinBoxStatTolerance.setProperty("markerCategory", QCoreApplication.translate("DockWidget", u"Stationary", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStationary), QCoreApplication.translate("DockWidget", u"Stationary", None))
    # retranslateUi

