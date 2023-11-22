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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDockWidget, QHeaderView,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(482, 656)
        DockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableStatistics = QTableView(self.dockWidgetContents)
        self.tableStatistics.setObjectName(u"tableStatistics")
        self.tableStatistics.setAlternatingRowColors(True)
        self.tableStatistics.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableStatistics.horizontalHeader().setStretchLastSection(True)
        self.tableStatistics.verticalHeader().setMinimumSectionSize(24)
        self.tableStatistics.verticalHeader().setDefaultSectionSize(24)

        self.verticalLayout.addWidget(self.tableStatistics)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Statistics", None))
    # retranslateUi

