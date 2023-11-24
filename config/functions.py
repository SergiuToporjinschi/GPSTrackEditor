from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QRect, QCoreApplication, Qt
from PySide6.QtGui import QCursor, QScreen


def defaultGeometry(width: int = 2000, height: int = 1100) -> QRect:
    rr:QCoreApplication = QApplication.instance()
    scr:QScreen = rr.screenAt(QCursor.pos())
    screenGeometry = scr.geometry()
    if scr.orientation() in  (Qt.ScreenOrientation.InvertedPortraitOrientation, Qt.ScreenOrientation.PortraitOrientation):
        height = height + 200
        x = screenGeometry.x() + (screenGeometry.width() - height) / 2
        y = screenGeometry.y() + (screenGeometry.height() - width) / 2
        return QRect(x, y, height, width)

    if scr.orientation() in (Qt.ScreenOrientation.LandscapeOrientation, Qt.ScreenOrientation.InvertedLandscapeOrientation):
        x = screenGeometry.x() + (screenGeometry.width() - width) / 2
        y = screenGeometry.y() + (screenGeometry.height() - height) / 2
        return QRect(x, y, width, height)
