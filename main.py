import sys
from mainGui import mainGUI
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor, QColorConstants, QIcon
import gpstracker_rc

def main():
    app = QApplication(sys.argv)
    gui = mainGUI(app)
    app.setStyle("Fusion")

    screens = app.screens()
    geom = screens[2].geometry()

    gui.setGeometry(geom.x(), geom.y(), 2300, 1000)
    gui.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowSystemMenuHint | Qt.WindowType.WindowMinMaxButtonsHint | Qt.WindowType.WindowCloseButtonHint)
    gui.show()

    palette = app.palette()
    # palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
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