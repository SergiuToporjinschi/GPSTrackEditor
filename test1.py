# main.py
import sys, os
from PyQt6.QtCore import QUrl, QObject, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWebChannel import QWebChannel
from qtpy.QtCore import Signal, Slot
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
class MyObject(QObject):
    @Slot(str, result=str)
    def greet(self, name):
        return f"Hello, {name} from PyQt!"

class WebEnginePage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        print(f"Console Message ({level}): {message} at line {lineNumber}")

class WebViewExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setPage(WebEnginePage())

        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.AllowWindowActivationFromJavaScript, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.DnsPrefetchEnabled, True)
        self.browser.settings().setUnknownUrlSchemePolicy(QWebEngineSettings.UnknownUrlSchemePolicy.AllowAllUnknownUrlSchemes)

        # Step 2: Create an instance of the QObject
        self.my_object = MyObject()

        # Step 2: Create a QWebChannel and register the QObject
        self.channel = QWebChannel()
        self.channel.registerObject("myObject", self.my_object)

        # Step 2: Set the channel on the page
        self.browser.page().setWebChannel(self.channel)

        # Step 3: Load the HTML file
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "resources/test.html"))
        self.browser.setUrl(QUrl.fromLocalFile(file_path))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebViewExample()
    sys.exit(app.exec())