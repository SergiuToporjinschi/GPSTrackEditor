# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics_dock.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QGroupBox, QLabel, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(400, 763)
        DockWidget.setFloating(False)
        DockWidget.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        DockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_2 = QScrollArea(self.dockWidgetContents)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 365, 1171))
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

        self.verticalLayout.addWidget(self.scrollArea_2)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Statistics", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("DockWidget", u"Calculated distance", None))
        self.label_151.setText(QCoreApplication.translate("DockWidget", u"Avg:", None))
        self.labelCalculatedDistanceMaxM.setText("")
        self.label_152.setText(QCoreApplication.translate("DockWidget", u"Min:", None))
        self.label_153.setText(QCoreApplication.translate("DockWidget", u"Max:", None))
        self.label_154.setText(QCoreApplication.translate("DockWidget", u"km", None))
        self.label_155.setText(QCoreApplication.translate("DockWidget", u"m", None))
        self.labelCalculatedDistanceAvgM.setText("")
        self.labelCalculatedDistanceMinM.setText("")
        self.labelCalculatedDistanceAvgKM.setText("")
        self.labelCalculatedDistanceMaxKM.setText("")
        self.labelCalculatedDistanceMinKM.setText("")
        self.label_156.setText(QCoreApplication.translate("DockWidget", u"Missing:", None))
        self.labelCalculatedDistanceMissing.setText("")
        self.groupBox_26.setTitle(QCoreApplication.translate("DockWidget", u"Distance", None))
        self.label_145.setText(QCoreApplication.translate("DockWidget", u"m", None))
        self.labelDistanceMissing.setText("")
        self.labelDistanceMaxKM.setText("")
        self.label_146.setText(QCoreApplication.translate("DockWidget", u"Avg:", None))
        self.labelDistanceMinKM.setText("")
        self.labelDistanceAvgM.setText("")
        self.labelDistanceMaxM.setText("")
        self.label_147.setText(QCoreApplication.translate("DockWidget", u"Min:", None))
        self.labelDistanceAvgKM.setText("")
        self.label_148.setText(QCoreApplication.translate("DockWidget", u"Max:", None))
        self.label_149.setText(QCoreApplication.translate("DockWidget", u"km", None))
        self.labelDistanceMinM.setText("")
        self.label_150.setText(QCoreApplication.translate("DockWidget", u"Missing:", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("DockWidget", u"Calculated speed", None))
        self.label_139.setText(QCoreApplication.translate("DockWidget", u"m/h", None))
        self.label_140.setText(QCoreApplication.translate("DockWidget", u"Max:", None))
        self.labelCalculatedSpeedMissing.setText("")
        self.labelCalculatedSpeedMaxKMPH.setText("")
        self.label_141.setText(QCoreApplication.translate("DockWidget", u"Min:", None))
        self.label_142.setText(QCoreApplication.translate("DockWidget", u"km/h", None))
        self.label_143.setText(QCoreApplication.translate("DockWidget", u"Missing:", None))
        self.labelCalculatedSpeedAvgMPH.setText("")
        self.labelCalculatedSpeedMinMPH.setText("")
        self.labelCalculatedSpeedMinKMPH.setText("")
        self.labelCalculatedSpeedAvgKMPH.setText("")
        self.label_144.setText(QCoreApplication.translate("DockWidget", u"Avg:", None))
        self.labelCalculatedSpeedMaxMPH.setText("")
        self.groupBox_24.setTitle(QCoreApplication.translate("DockWidget", u"Speed", None))
        self.labelSpeedAvgKMPH.setText("")
        self.labelSpeedMinKMPH.setText("")
        self.label_133.setText(QCoreApplication.translate("DockWidget", u"m/h", None))
        self.label_134.setText(QCoreApplication.translate("DockWidget", u"Max:", None))
        self.labelSpeedMaxKMPH.setText("")
        self.labelSpeedAvgMPH.setText("")
        self.label_135.setText(QCoreApplication.translate("DockWidget", u"Min:", None))
        self.labelSpeedMaxMPH.setText("")
        self.labelSpeedMinMPH.setText("")
        self.label_136.setText(QCoreApplication.translate("DockWidget", u"Avg:", None))
        self.label_137.setText(QCoreApplication.translate("DockWidget", u"km/h", None))
        self.label_138.setText(QCoreApplication.translate("DockWidget", u"Missing:", None))
        self.labelSpeedMissing.setText("")
        self.groupBox_23.setTitle(QCoreApplication.translate("DockWidget", u"Altitude", None))
        self.label_127.setText(QCoreApplication.translate("DockWidget", u"Avg:", None))
        self.label_128.setText("")
        self.labelAltitudeMin.setText("")
        self.labelAltitudeMax.setText("")
        self.label_129.setText(QCoreApplication.translate("DockWidget", u"Min:", None))
        self.labelAltitudeAvg.setText("")
        self.label_130.setText(QCoreApplication.translate("DockWidget", u"m", None))
        self.label_131.setText(QCoreApplication.translate("DockWidget", u"Max:", None))
        self.label_132.setText(QCoreApplication.translate("DockWidget", u"Missing:", None))
        self.labelAltitudeMissing.setText("")
        self.groupBox_22.setTitle(QCoreApplication.translate("DockWidget", u"Longitude", None))
        self.label_121.setText(QCoreApplication.translate("DockWidget", u"Avg:", None))
        self.label_122.setText("")
        self.labelLongitudeMin.setText("")
        self.labelLongitudeMax.setText("")
        self.label_123.setText(QCoreApplication.translate("DockWidget", u"Min:", None))
        self.labelLongitudeAvg.setText("")
        self.label_124.setText(QCoreApplication.translate("DockWidget", u"degree", None))
        self.label_125.setText(QCoreApplication.translate("DockWidget", u"Max:", None))
        self.label_126.setText(QCoreApplication.translate("DockWidget", u"Missing:", None))
        self.labelLongitudeMissing.setText("")
        self.groupBox_21.setTitle(QCoreApplication.translate("DockWidget", u"Latitude", None))
        self.label_115.setText(QCoreApplication.translate("DockWidget", u"Avg:", None))
        self.label_116.setText("")
        self.labelLatitudeMin.setText("")
        self.labelLatitudeMax.setText("")
        self.label_117.setText(QCoreApplication.translate("DockWidget", u"Min:", None))
        self.labelLatitudeAvg.setText("")
        self.label_118.setText(QCoreApplication.translate("DockWidget", u"degree", None))
        self.label_119.setText(QCoreApplication.translate("DockWidget", u"Max:", None))
        self.label_120.setText(QCoreApplication.translate("DockWidget", u"Missing:", None))
        self.labelLatitudeMissing.setText("")
        self.groupBox_20.setTitle(QCoreApplication.translate("DockWidget", u"Hart rate", None))
        self.label_109.setText(QCoreApplication.translate("DockWidget", u"Avg:", None))
        self.label_110.setText("")
        self.labelHartRateMin.setText("")
        self.labelHartRateMax.setText("")
        self.label_111.setText(QCoreApplication.translate("DockWidget", u"Min:", None))
        self.labelHartRateAvg.setText("")
        self.label_112.setText(QCoreApplication.translate("DockWidget", u"bpm", None))
        self.label_113.setText(QCoreApplication.translate("DockWidget", u"Max:", None))
        self.label_114.setText(QCoreApplication.translate("DockWidget", u"Missing:", None))
        self.labelHartRateMissing.setText("")
    # retranslateUi

