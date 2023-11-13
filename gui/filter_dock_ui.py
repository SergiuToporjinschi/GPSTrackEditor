# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_dock.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QDockWidget, QDoubleSpinBox, QFrame,
    QGridLayout, QLabel, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

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
        self.scrollArea_5 = QScrollArea(self.dockWidgetContents)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setFrameShadow(QFrame.Plain)
        self.scrollArea_5.setLineWidth(0)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 485, 320))
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

        self.verticalLayout.addWidget(self.scrollArea_5)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Filter", None))
        self.doubleSpinBox_31.setSpecialValueText("")
        self.checkBox_2.setText(QCoreApplication.translate("DockWidget", u"Time", None))
        self.label_169.setText(QCoreApplication.translate("DockWidget", u"From", None))
        self.doubleSpinBox_25.setSpecialValueText("")
        self.doubleSpinBox_16.setSpecialValueText("")
        self.doubleSpinBox_22.setSpecialValueText("")
        self.checkBox_3.setText(QCoreApplication.translate("DockWidget", u"Calculated distance", None))
        self.checkBox_10.setText(QCoreApplication.translate("DockWidget", u"Longitude", None))
        self.checkBox_7.setText(QCoreApplication.translate("DockWidget", u"Calculated speed", None))
        self.dateTimeEdit_4.setSpecialValueText("")
        self.dateTimeEdit_4.setDisplayFormat(QCoreApplication.translate("DockWidget", u"dd-MM-yyyy HH:mm:ss.zzz t", None))
        self.doubleSpinBox_27.setSpecialValueText("")
        self.checkBox_9.setText(QCoreApplication.translate("DockWidget", u"Hart rate", None))
        self.doubleSpinBox_28.setSpecialValueText("")
        self.doubleSpinBox_24.setSpecialValueText("")
        self.doubleSpinBox_29.setSpecialValueText("")
        self.checkBox_8.setText(QCoreApplication.translate("DockWidget", u"Altitude", None))
        self.checkBox_4.setText(QCoreApplication.translate("DockWidget", u"Sensor state", None))
        self.doubleSpinBox_26.setSpecialValueText("")
        self.doubleSpinBox_18.setSpecialValueText("")
        self.doubleSpinBox_32.setSpecialValueText("")
        self.label_170.setText(QCoreApplication.translate("DockWidget", u"To", None))
        self.checkBox_6.setText(QCoreApplication.translate("DockWidget", u"Speed", None))
        self.doubleSpinBox_15.setSpecialValueText("")
        self.checkBox.setText(QCoreApplication.translate("DockWidget", u"Distance", None))
        self.doubleSpinBox_30.setSpecialValueText("")
        self.doubleSpinBox_17.setSpecialValueText("")
        self.checkBox_5.setText(QCoreApplication.translate("DockWidget", u"Latitude", None))
        self.doubleSpinBox_21.setSpecialValueText("")
        self.dateTimeEdit_3.setSpecialValueText("")
        self.dateTimeEdit_3.setDisplayFormat(QCoreApplication.translate("DockWidget", u"dd-MM-yyyy HH:mm:ss.zzz t", None))
        self.doubleSpinBox_23.setSpecialValueText("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.setItemText(1, QCoreApplication.translate("DockWidget", u"None", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("DockWidget", u"Absent", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("DockWidget", u"Present", None))

    # retranslateUi

