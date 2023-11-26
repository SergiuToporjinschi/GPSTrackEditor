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
        DockWidget.resize(676, 657)
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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 676, 633))
        self.scrollAreaWidgetContents_4.setAutoFillBackground(False)
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.scrollAreaWidgetContents_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setHandleWidth(10)
        self.frameTop = QFrame(self.splitter_2)
        self.frameTop.setObjectName(u"frameTop")
        self.frameTop.setFrameShape(QFrame.StyledPanel)
        self.frameTop.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameTop)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolDelete = QToolButton(self.frameTop)
        self.toolDelete.setObjectName(u"toolDelete")
        self.toolDelete.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.toolDelete)

        self.toolActivate = QToolButton(self.frameTop)
        self.toolActivate.setObjectName(u"toolActivate")
        self.toolActivate.setCheckable(True)

        self.horizontalLayout.addWidget(self.toolActivate)

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
        self.frameBottom.setFrameShape(QFrame.StyledPanel)
        self.frameBottom.setFrameShadow(QFrame.Raised)
        self.frameBottom.setLineWidth(10)
        self.verticalLayout_2 = QVBoxLayout(self.frameBottom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.frameBottom)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.East)
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

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBoxStatTolerance)

        self.tabWidget.addTab(self.tabStationary, "")
        self.tabCustom = QWidget()
        self.tabCustom.setObjectName(u"tabCustom")
        self.formLayout = QFormLayout(self.tabCustom)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(9, -1, 9, -1)
        self.label_167 = QLabel(self.tabCustom)
        self.label_167.setObjectName(u"label_167")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_167)

        self.editAltitude = QLineEdit(self.tabCustom)
        self.editAltitude.setObjectName(u"editAltitude")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editAltitude)

        self.label_164 = QLabel(self.tabCustom)
        self.label_164.setObjectName(u"label_164")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_164)

        self.editTime = QLineEdit(self.tabCustom)
        self.editTime.setObjectName(u"editTime")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editTime)

        self.label_168 = QLabel(self.tabCustom)
        self.label_168.setObjectName(u"label_168")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_168)

        self.editHartRate = QLineEdit(self.tabCustom)
        self.editHartRate.setObjectName(u"editHartRate")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editHartRate)

        self.label_162 = QLabel(self.tabCustom)
        self.label_162.setObjectName(u"label_162")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_162)

        self.editSensorState = QLineEdit(self.tabCustom)
        self.editSensorState.setObjectName(u"editSensorState")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.editSensorState)

        self.label_165 = QLabel(self.tabCustom)
        self.label_165.setObjectName(u"label_165")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_165)

        self.editLatitude = QLineEdit(self.tabCustom)
        self.editLatitude.setObjectName(u"editLatitude")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.editLatitude)

        self.label_166 = QLabel(self.tabCustom)
        self.label_166.setObjectName(u"label_166")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_166)

        self.editLongitude = QLineEdit(self.tabCustom)
        self.editLongitude.setObjectName(u"editLongitude")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.editLongitude)

        self.label_158 = QLabel(self.tabCustom)
        self.label_158.setObjectName(u"label_158")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_158)

        self.editDistance = QLineEdit(self.tabCustom)
        self.editDistance.setObjectName(u"editDistance")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.editDistance)

        self.label_159 = QLabel(self.tabCustom)
        self.label_159.setObjectName(u"label_159")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_159)

        self.editCalculatedDistance = QLineEdit(self.tabCustom)
        self.editCalculatedDistance.setObjectName(u"editCalculatedDistance")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.editCalculatedDistance)

        self.label_160 = QLabel(self.tabCustom)
        self.label_160.setObjectName(u"label_160")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_160)

        self.editSpeed = QLineEdit(self.tabCustom)
        self.editSpeed.setObjectName(u"editSpeed")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.editSpeed)

        self.label_161 = QLabel(self.tabCustom)
        self.label_161.setObjectName(u"label_161")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_161)

        self.editCalculatedSpeed = QLineEdit(self.tabCustom)
        self.editCalculatedSpeed.setObjectName(u"editCalculatedSpeed")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.editCalculatedSpeed)

        self.tabWidget.addTab(self.tabCustom, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.pushAdd = QPushButton(self.frameBottom)
        self.pushAdd.setObjectName(u"pushAdd")

        self.verticalLayout_2.addWidget(self.pushAdd)

        self.splitter_2.addWidget(self.frameBottom)

        self.verticalLayout_4.addWidget(self.splitter_2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.scrollArea_4)

        DockWidget.setWidget(self.dockWidgetContents)
#if QT_CONFIG(shortcut)
        self.label_167.setBuddy(self.editAltitude)
        self.label_164.setBuddy(self.editTime)
        self.label_168.setBuddy(self.editHartRate)
        self.label_162.setBuddy(self.editSensorState)
        self.label_165.setBuddy(self.editLatitude)
        self.label_166.setBuddy(self.editLongitude)
        self.label_158.setBuddy(self.editDistance)
        self.label_159.setBuddy(self.editCalculatedDistance)
        self.label_160.setBuddy(self.editSpeed)
        self.label_161.setBuddy(self.editCalculatedSpeed)
#endif // QT_CONFIG(shortcut)

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
        self.toolDelete.setText(QCoreApplication.translate("DockWidget", u"Delete", None))
        self.toolActivate.setText(QCoreApplication.translate("DockWidget", u"Active", None))
        self.label_163.setText(QCoreApplication.translate("DockWidget", u"Tolerance:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStationary), QCoreApplication.translate("DockWidget", u"Stationary", None))
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
        self.pushAdd.setText(QCoreApplication.translate("DockWidget", u"Add", None))
    # retranslateUi

