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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDockWidget, QFrame,
    QGridLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(400, 300)
        DockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_3 = QScrollArea(self.dockWidgetContents)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 382, 258))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, 9, 0)
        self.label_171 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_171.setObjectName(u"label_171")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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

        self.buttonShiftTime = QPushButton(self.scrollAreaWidgetContents_3)
        self.buttonShiftTime.setObjectName(u"buttonShiftTime")

        self.gridLayout_2.addWidget(self.buttonShiftTime, 2, 2, 1, 1)

        self.buttonCalculateDistance = QPushButton(self.scrollAreaWidgetContents_3)
        self.buttonCalculateDistance.setObjectName(u"buttonCalculateDistance")

        self.gridLayout_2.addWidget(self.buttonCalculateDistance, 3, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea_3)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Processing", None))
        self.label_171.setText(QCoreApplication.translate("DockWidget", u"Calculate", None))
        self.buttonCalculateSpeed.setText(QCoreApplication.translate("DockWidget", u"Speed", None))
        self.startDateTime_2.setDisplayFormat(QCoreApplication.translate("DockWidget", u"dd-MM-yyyy HH:mm:ss.zzz t", None))
        self.buttonShiftTime.setText(QCoreApplication.translate("DockWidget", u"Shift time", None))
        self.buttonCalculateDistance.setText(QCoreApplication.translate("DockWidget", u"Distance", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Time shifting", None))
    # retranslateUi

