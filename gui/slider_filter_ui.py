# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slider_filter.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QSizePolicy, QSpinBox, QWidget)
import gpstracker_rc

class Ui_SliderFilter(object):
    def setupUi(self, SliderFilter):
        if not SliderFilter.objectName():
            SliderFilter.setObjectName(u"SliderFilter")
        SliderFilter.resize(224, 22)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SliderFilter.sizePolicy().hasHeightForWidth())
        SliderFilter.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(SliderFilter)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.spinBoxRangeMin = QSpinBox(SliderFilter)
        self.spinBoxRangeMin.setObjectName(u"spinBoxRangeMin")
        self.spinBoxRangeMin.setMinimumSize(QSize(70, 0))
        self.spinBoxRangeMin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBoxRangeMin.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBoxRangeMin.setMinimum(0)
        self.spinBoxRangeMin.setMaximum(999999)
        self.spinBoxRangeMin.setValue(0)

        self.horizontalLayout.addWidget(self.spinBoxRangeMin)

        self.spinBoxRangeMax = QSpinBox(SliderFilter)
        self.spinBoxRangeMax.setObjectName(u"spinBoxRangeMax")
        self.spinBoxRangeMax.setMinimumSize(QSize(70, 0))
        self.spinBoxRangeMax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBoxRangeMax.setMinimum(0)
        self.spinBoxRangeMax.setMaximum(999999)
        self.spinBoxRangeMax.setValue(0)

        self.horizontalLayout.addWidget(self.spinBoxRangeMax)


        self.retranslateUi(SliderFilter)

        QMetaObject.connectSlotsByName(SliderFilter)
    # setupUi

    def retranslateUi(self, SliderFilter):
        SliderFilter.setWindowTitle(QCoreApplication.translate("SliderFilter", u"SliderFilter", None))
#if QT_CONFIG(accessibility)
        SliderFilter.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

