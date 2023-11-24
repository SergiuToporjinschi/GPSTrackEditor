import sys
import Utils
import gpstracker_rc

from mainGui import mainGUI
from PySide6.QtCore import Qt, QSettings, QByteArray, QRect
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor, QColorConstants, QIcon, QSessionManager
from config import *

from PySide6.QtGui import QScreen

def closing(window: mainGUI):
    Config.setValueG(ConfigGroup.MainWindow, ConfigAttribute.Geometry, window.saveGeometry())
    Config.setValueG(ConfigGroup.MainWindow, ConfigAttribute.State, window.saveState())
    window.restoreDockWidget
    print("saved!")


def main():
    app = QApplication(sys.argv)
    gui = mainGUI(app)
    app.setStyle("Fusion")
    app.lastWindowClosed.connect(lambda: closing(gui))

    gui.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowSystemMenuHint | Qt.WindowType.WindowMinMaxButtonsHint | Qt.WindowType.WindowCloseButtonHint)

    # gui.setGeometry(Config.valueG(ConfigGroup.MainWindow, ConfigAttribute.Geometry, Utils.defaultGeometry()))
    gui.restoreState(Config.valueG(ConfigGroup.MainWindow, ConfigAttribute.State, None))
    gui.restoreGeometry(Config.valueG(ConfigGroup.MainWindow, ConfigAttribute.Geometry, None))
    gui.show()

    palette = app.palette()
    palette.setColor(QPalette.ColorRole.WindowText, QColorConstants.White)
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColorConstants.White)
    palette.setColor(QPalette.ColorRole.ToolTipText, QColorConstants.White)
    palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, QColorConstants.White)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, QColorConstants.White)
    palette.setColor(QPalette.ColorRole.BrightText, QColorConstants.Red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColorConstants.White)

    QIcon.setThemeSearchPaths(["resources/icon_theme"])
    QIcon.setThemeName("icon-theme")

    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(170, 170, 170))
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(170, 170, 170))

    app.setPalette(palette)

    sys.exit(app.exec())



if __name__ == '__main__':
    main()