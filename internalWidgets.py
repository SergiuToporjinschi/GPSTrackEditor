import typing, os
from PyQt6.QtWidgets import QFrame, QWidget
from PyQt6 import QtCore
from qtpy.QtCore import Signal, QUrl
from superqt import QRangeSlider
from gui.slider_filter_ui import Ui_SliderFilter
from gui.status_bar_ui import Ui_GroupBox
from PyQt6.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt6.QtWidgets import  QMainWindow, QDockWidget
from gui.map_dock_map_ui import Ui_DockWidget
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings, QWebEngineScript
from PyQt6.QtWebChannel import QWebChannel, QWebChannelAbstractTransport
import json

class StatusBarGroupBox(QFrame, Ui_GroupBox):
    updateProgress = Signal(int)
    updateSelection = Signal(int)
    updateTackPoints = Signal(int)
    updateTimerMessage = Signal(str)
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

class QtSliderFilterWidgetPlugin(QFrame, Ui_SliderFilter, QPyDesignerCustomWidgetPlugin):
    selectedIntervalChanged = Signal(tuple)
    selectedMinIntervalChanged = Signal(int)
    selectedMaxIntervalChanged = Signal(int)

    selectionCountChanged = Signal(int)
    selectionCnt = 0

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._insertRangeSlider()
        self.min = 0
        self.max = 0

    def _insertRangeSlider(self):
        self.horizontalLayout.removeWidget(self.sliderFilter)
        self.sliderFilter = QRangeSlider(self)
        self.sliderFilter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sliderFilter.setObjectName("verticalSlider")
        self.sliderFilter.setRange(1, 2)
        self.sliderFilter.applyMacStylePatch()
        self.sliderFilter.setSliderPosition([1, 1])
        self.horizontalLayout.insertWidget(1, self.sliderFilter, 1)
        self.sliderFilter.valueChanged.connect(self.sliderChanged)
        self.sliderFilter.valueChanged.connect(self.selectedIntervalChanged)

        self.spinBoxRangeMax.valueChanged.connect(self.maxSpinnerChanged)
        self.spinBoxRangeMax.valueChanged.connect(self.selectedMaxIntervalChanged)

        self.spinBoxRangeMin.valueChanged.connect(self.minSpinnerChanged)
        self.spinBoxRangeMin.valueChanged.connect(self.selectedMinIntervalChanged)

    def setRange(self, min:int, max:int):
        if min > max: raise ValueError("Value error for setting range Max < Min!!!")
        if min == self.min and max == self.max: return
        self.min = min
        self.max = max
        self.spinBoxRangeMin.setRange(min, max)
        self.spinBoxRangeMax.setRange(min, max)
        self.sliderFilter.setRange(min, max if max != min else min + 1)

        self.spinBoxRangeMin.setValue(min)
        self.spinBoxRangeMax.setValue(max)
        self.sliderFilter.setSliderPosition([min, max])
        self._updateSelectionCnt(max-min)
        self.setEnabled(self.selectionCnt > 1)

    def minSpinnerChanged(self, value):
        min, max = self.sliderFilter.sliderPosition()
        min = int(min)
        max = int(max)
        self.sliderFilter.setSliderPosition((value, max))
        self._updateSelectionCnt(max - value)

    def maxSpinnerChanged(self, value):
        min, max = self.sliderFilter.sliderPosition()
        min = int(min)
        max = int(max)
        self.sliderFilter.setSliderPosition((min, value))
        self._updateSelectionCnt(value - min)

    def sliderChanged(self, val):
        min, max = val
        if self.spinBoxRangeMin.value() != int(min):
            self.spinBoxRangeMin.setValue(int(min))

        if self.spinBoxRangeMax.value() != int(max):
            self.spinBoxRangeMax.setValue(int(max))

    def _updateSelectionCnt(self, val):
        val = val + 1
        if self.selectionCnt != val:
            self.selectionCnt = val
            self.selectionCountChanged.emit(val)

class MapWindow(QDockWidget, Ui_DockWidget):
    entireTrackCoordinates = Signal(str)
    markPoint = Signal(str)
    def __init__(self, parent: typing.Optional[QWidget] = ...):
        super().__init__(parent=parent,flags=QtCore.Qt.WindowType.FramelessWindowHint)
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "resources/index.html"))
        self.setupUi(self)
        self._loadMap()

    def _loadMap(self):
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)

        self.channel = QWebChannel()
        self.channel.registerObject("backEnd", self)

        self.browser.page().setWebChannel(self.channel)
        self.browser.setUrl(QUrl.fromLocalFile(self.file_path))
        self.browser.show()
        self.pushButton.clicked.connect(self.sendNewCoordinates)

    def sendMarkPoint(self, coordinates):
        self.markPoint.emit(json.dumps(coordinates))

    def sendNewCoordinates(self, coordinates):
        # coordinates = [
        #     [24.19399667, 45.81218000],
        #     [24.19401500, 45.81217000],
        #     [24.19403167, 45.81216000]
        # ]
        self.entireTrackCoordinates.emit(json.dumps(coordinates))
