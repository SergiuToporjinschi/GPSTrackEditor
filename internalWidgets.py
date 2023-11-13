import typing, os, json
from qtpy.QtCore import Signal, QUrl
from superqt import QRangeSlider

from gui.slider_filter_ui import Ui_SliderFilter
from gui.status_bar_ui import Ui_GroupBox
from gui.map_dock_ui import Ui_DockWidget

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QFrame, QWidget, QDockWidget
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

class StatusBarGroupBox(QFrame, Ui_GroupBox):
    updateProgress = Signal(int)
    updateSelection = Signal(int)
    updateTackPoints = Signal(int)
    updateTimerMessage = Signal(str)
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.timerClear =  QTimer(self)
        self.timerClear.setInterval(5000)
        self.timerClear.setSingleShot(False)
        self.timerClear.setTimerType(Qt.TimerType.CoarseTimer)
        self.timerClear.start()
        self.timerClear.timeout.connect(lambda: self.updateTimerMessage.emit(''))
        self.timerClear.timeout.connect(lambda: self.updateProgress.emit(0))

class QtSliderFilterWidgetPlugin(QFrame, Ui_SliderFilter):
    selectedIntervalChanged = Signal(tuple) #spinner changed or slider changed in any way or any cain
    selectedMinIntervalChanged = Signal(int) #min spinner changed
    selectedMaxIntervalChanged = Signal(int) #max spinner changed

    selectionCountChanged = Signal(int) #When selection in slider changed
    selectionCnt = 0

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._insertRangeSlider()
        self.min = 0
        self.max = 0

    def _insertRangeSlider(self):
        self.sliderFilter = QRangeSlider(self)
        self.sliderFilter.setOrientation(Qt.Orientation.Horizontal)
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

    def setMainRange(self, min:int, max:int):
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

