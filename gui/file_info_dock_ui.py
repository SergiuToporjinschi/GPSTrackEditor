# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_info_dock.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFormLayout, QFrame,
    QLabel, QLineEdit, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(525, 280)
        DockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 507, 238))
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

        self.inputFilePath = QLineEdit(self.scrollAreaWidgetContents)
        self.inputFilePath.setObjectName(u"inputFilePath")
        self.inputFilePath.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputFilePath)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(6, QFormLayout.FieldRole, self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        DockWidget.setWidget(self.dockWidgetContents)
#if QT_CONFIG(shortcut)
        self.labelSport.setBuddy(self.inputSport)
        self.lableFile.setBuddy(self.inputFilePath)
        self.labelLapsNo.setBuddy(self.inputLaps)
        self.labelID.setBuddy(self.inputId)
        self.labelTrackPointsNo.setBuddy(self.inputTrackPoints)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"File info", None))
        self.labelSport.setText(QCoreApplication.translate("DockWidget", u"Sport", None))
#if QT_CONFIG(tooltip)
        self.inputSport.setToolTip(QCoreApplication.translate("DockWidget", u"Sport", None))
#endif // QT_CONFIG(tooltip)
        self.lableFile.setText(QCoreApplication.translate("DockWidget", u"File", None))
        self.labelLapsNo.setText(QCoreApplication.translate("DockWidget", u"Laps", None))
#if QT_CONFIG(tooltip)
        self.inputLaps.setToolTip(QCoreApplication.translate("DockWidget", u"Number of laps", None))
#endif // QT_CONFIG(tooltip)
        self.labelID.setText(QCoreApplication.translate("DockWidget", u"ID:", None))
        self.labelTrackPointsNo.setText(QCoreApplication.translate("DockWidget", u"Track points:", None))
#if QT_CONFIG(tooltip)
        self.inputTrackPoints.setToolTip(QCoreApplication.translate("DockWidget", u"Number of track points", None))
#endif // QT_CONFIG(tooltip)
        self.labelNotes.setText(QCoreApplication.translate("DockWidget", u"Notes:", None))
    # retranslateUi

