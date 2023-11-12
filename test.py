import sys
import typing
from PyQt6.QtCore import QUrl, QObject
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings, QWebEngineScript
from PyQt6.QtWebChannel import QWebChannel, QWebChannelAbstractTransport
import os
from qtpy.QtCore import Signal, Slot


class MyObject(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    textChanged = Signal(str)

    @Slot(result=str)
    def getMessage(self):
        return '{"test":"test"}'

    def sendData(self, data):
        print(f"Received from JS: {data}")

    def doUpdate(self):
        self.textChanged.emit("somethig")

class WebViewExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QtWebEngine Example")
        self.setGeometry(100, 100, 800, 600)
        self.browser = QWebEngineView(self)
        pushButton = QtWidgets.QPushButton()
        pushButton.setText("PyButton")
        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        layout.addWidget(pushButton)
        container = QWidget(self)
        container.setLayout(layout)
        self.setCentralWidget(container)

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "resources/index.html"))
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)

        self.myObj = MyObject()
        self.channel = QWebChannel()
        self.channel.registerObject("content",self.myObj)

        self.browser.page().setWebChannel(self.channel)
        self.browser.setUrl(QUrl.fromLocalFile(file_path))
        self.browser.show()

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebViewExample()
    sys.exit(app.exec())