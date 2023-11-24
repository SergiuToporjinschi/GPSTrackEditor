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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QDoubleSpinBox, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(676, 767)
        DockWidget.setFloating(False)
        DockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_4 = QScrollArea(self.dockWidgetContents)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QFrame.Plain)
        self.scrollArea_4.setLineWidth(0)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 658, 725))
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

        self.editFindByLatitude = QLineEdit(self.frameFilders1_2)
        self.editFindByLatitude.setObjectName(u"editFindByLatitude")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.editFindByLatitude)

        self.label_166 = QLabel(self.frameFilders1_2)
        self.label_166.setObjectName(u"label_166")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_166)

        self.editFindByLongitude = QLineEdit(self.frameFilders1_2)
        self.editFindByLongitude.setObjectName(u"editFindByLongitude")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.editFindByLongitude)

        self.label_164 = QLabel(self.frameFilders1_2)
        self.label_164.setObjectName(u"label_164")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_164)

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

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.pushCustomMarkSelColor = QPushButton(self.frameFilders1_2)
        self.pushCustomMarkSelColor.setObjectName(u"pushCustomMarkSelColor")
        self.pushCustomMarkSelColor.setFocusPolicy(Qt.NoFocus)
        self.pushCustomMarkSelColor.setAutoFillBackground(True)
        self.pushCustomMarkSelColor.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushCustomMarkSelColor)

        self.pushCustomMark = QPushButton(self.frameFilders1_2)
        self.pushCustomMark.setObjectName(u"pushCustomMark")

        self.horizontalLayout_3.addWidget(self.pushCustomMark)

        self.pushCustomMarkClear = QPushButton(self.frameFilders1_2)
        self.pushCustomMarkClear.setObjectName(u"pushCustomMarkClear")

        self.horizontalLayout_3.addWidget(self.pushCustomMarkClear)


        self.formLayout_6.setLayout(10, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.verticalLayout_14.addWidget(self.frameFilders1_2)

        self.groupBox_28 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_28.setObjectName(u"groupBox_28")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_28.sizePolicy().hasHeightForWidth())
        self.groupBox_28.setSizePolicy(sizePolicy)
        self.groupBox_28.setFlat(True)
        self.formLayout = QFormLayout(self.groupBox_28)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 9, -1, 0)
        self.label_163 = QLabel(self.groupBox_28)
        self.label_163.setObjectName(u"label_163")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy1)
        self.label_163.setMinimumSize(QSize(106, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_163)

        self.spinBoxMarkStatTolerance = QDoubleSpinBox(self.groupBox_28)
        self.spinBoxMarkStatTolerance.setObjectName(u"spinBoxMarkStatTolerance")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBoxMarkStatTolerance)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.pushStatMarkSelColor = QPushButton(self.groupBox_28)
        self.pushStatMarkSelColor.setObjectName(u"pushStatMarkSelColor")
        self.pushStatMarkSelColor.setFocusPolicy(Qt.NoFocus)
        self.pushStatMarkSelColor.setAutoFillBackground(True)
        self.pushStatMarkSelColor.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushStatMarkSelColor)

        self.pushStatMark = QPushButton(self.groupBox_28)
        self.pushStatMark.setObjectName(u"pushStatMark")

        self.horizontalLayout_2.addWidget(self.pushStatMark)

        self.pushStatMarkClear = QPushButton(self.groupBox_28)
        self.pushStatMarkClear.setObjectName(u"pushStatMarkClear")

        self.horizontalLayout_2.addWidget(self.pushStatMarkClear)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout_14.addWidget(self.groupBox_28)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.scrollArea_4)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Marking", None))
        self.label_167.setText(QCoreApplication.translate("DockWidget", u"Altitude:", None))
        self.label_168.setText(QCoreApplication.translate("DockWidget", u"Hart rate:", None))
        self.label_165.setText(QCoreApplication.translate("DockWidget", u"Latitude:", None))
        self.label_166.setText(QCoreApplication.translate("DockWidget", u"Longitude:", None))
        self.label_164.setText(QCoreApplication.translate("DockWidget", u"Time:", None))
        self.label_158.setText(QCoreApplication.translate("DockWidget", u"Distance:", None))
        self.label_159.setText(QCoreApplication.translate("DockWidget", u"Calculated distance:", None))
        self.label_160.setText(QCoreApplication.translate("DockWidget", u"Speed:", None))
        self.label_161.setText(QCoreApplication.translate("DockWidget", u"Calculated speed:", None))
        self.label_162.setText(QCoreApplication.translate("DockWidget", u"Sensor state", None))
        self.pushCustomMarkSelColor.setText(QCoreApplication.translate("DockWidget", u"Color", None))
        self.pushCustomMark.setText(QCoreApplication.translate("DockWidget", u"Mark", None))
        self.pushCustomMarkClear.setText(QCoreApplication.translate("DockWidget", u"Clear", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("DockWidget", u"Mark stationary", None))
        self.label_163.setText(QCoreApplication.translate("DockWidget", u"Tolerance:", None))
        self.pushStatMarkSelColor.setText(QCoreApplication.translate("DockWidget", u"Color", None))
        self.pushStatMark.setText(QCoreApplication.translate("DockWidget", u"Mark ", None))
        self.pushStatMarkClear.setText(QCoreApplication.translate("DockWidget", u"Clear", None))
    # retranslateUi

