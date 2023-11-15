# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'status_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QProgressBar, QSizePolicy, QWidget)

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        if not GroupBox.objectName():
            GroupBox.setObjectName(u"GroupBox")
        GroupBox.resize(443, 24)
        GroupBox.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(GroupBox)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.separator3 = QLabel(GroupBox)
        self.separator3.setObjectName(u"separator3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.separator3.sizePolicy().hasHeightForWidth())
        self.separator3.setSizePolicy(sizePolicy)
        self.separator3.setMinimumSize(QSize(5, 0))
        self.separator3.setMaximumSize(QSize(5, 16777215))

        self.horizontalLayout.addWidget(self.separator3)

        self.labelMessage = QLabel(GroupBox)
        self.labelMessage.setObjectName(u"labelMessage")

        self.horizontalLayout.addWidget(self.labelMessage)

        self.separator2 = QLabel(GroupBox)
        self.separator2.setObjectName(u"separator2")
        sizePolicy.setHeightForWidth(self.separator2.sizePolicy().hasHeightForWidth())
        self.separator2.setSizePolicy(sizePolicy)
        self.separator2.setMinimumSize(QSize(5, 0))
        self.separator2.setMaximumSize(QSize(5, 16777215))

        self.horizontalLayout.addWidget(self.separator2)

        self.horizontalLayoutCounts = QHBoxLayout()
        self.horizontalLayoutCounts.setSpacing(0)
        self.horizontalLayoutCounts.setObjectName(u"horizontalLayoutCounts")
        self.labelSelectionCntText = QLabel(GroupBox)
        self.labelSelectionCntText.setObjectName(u"labelSelectionCntText")
        self.labelSelectionCntText.setMinimumSize(QSize(70, 0))
        self.labelSelectionCntText.setScaledContents(True)
        self.labelSelectionCntText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayoutCounts.addWidget(self.labelSelectionCntText)

        self.labelSelectionCntVal = QLabel(GroupBox)
        self.labelSelectionCntVal.setObjectName(u"labelSelectionCntVal")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelSelectionCntVal.sizePolicy().hasHeightForWidth())
        self.labelSelectionCntVal.setSizePolicy(sizePolicy1)
        self.labelSelectionCntVal.setMinimumSize(QSize(40, 0))
        self.labelSelectionCntVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelSelectionCntVal.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayoutCounts.addWidget(self.labelSelectionCntVal)

        self.label = QLabel(GroupBox)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayoutCounts.addWidget(self.label)

        self.labelTotalCntVal = QLabel(GroupBox)
        self.labelTotalCntVal.setObjectName(u"labelTotalCntVal")
        sizePolicy1.setHeightForWidth(self.labelTotalCntVal.sizePolicy().hasHeightForWidth())
        self.labelTotalCntVal.setSizePolicy(sizePolicy1)
        self.labelTotalCntVal.setMinimumSize(QSize(40, 0))
        self.labelTotalCntVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelTotalCntVal.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayoutCounts.addWidget(self.labelTotalCntVal)


        self.horizontalLayout.addLayout(self.horizontalLayoutCounts)

        self.separator1 = QLabel(GroupBox)
        self.separator1.setObjectName(u"separator1")
        sizePolicy.setHeightForWidth(self.separator1.sizePolicy().hasHeightForWidth())
        self.separator1.setSizePolicy(sizePolicy)
        self.separator1.setMinimumSize(QSize(5, 0))
        self.separator1.setMaximumSize(QSize(5, 16777215))

        self.horizontalLayout.addWidget(self.separator1)

        self.progressBar = QProgressBar(GroupBox)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setMaximumSize(QSize(100, 19))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar)


        self.retranslateUi(GroupBox)
        GroupBox.updateProgress.connect(self.progressBar.setValue)
        GroupBox.updateTrimmerLen.connect(self.labelSelectionCntVal.setNum)
        GroupBox.updateTackLen.connect(self.labelTotalCntVal.setNum)

        QMetaObject.connectSlotsByName(GroupBox)
    # setupUi

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QCoreApplication.translate("GroupBox", u"GroupBox", None))
        self.separator3.setText("")
        self.labelMessage.setText("")
        self.separator2.setText("")
        self.labelSelectionCntText.setText(QCoreApplication.translate("GroupBox", u"Trim: ", None))
        self.labelSelectionCntVal.setText(QCoreApplication.translate("GroupBox", u"0", None))
        self.label.setText(QCoreApplication.translate("GroupBox", u"Points: ", None))
        self.labelTotalCntVal.setText(QCoreApplication.translate("GroupBox", u"0", None))
        self.separator1.setText("")
    # retranslateUi

