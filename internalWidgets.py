# https://pyapp-kit.github.io/superqt/widgets/

from qtpy.QtCore import Signal
from superqt import QRangeSlider

from abstracts import AbstractModelWidget

from gui.slider_filter_ui import Ui_SliderFilter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame

class QtSliderFilterWidgetPlugin(AbstractModelWidget, QFrame, Ui_SliderFilter):
    trimmerChanged = Signal(tuple) #spinner changed or slider changed in any way or any cain

    selectionCountChanged = Signal(int) #When selection in slider changed
    selectionCnt = 0

    mainSeriesMin: 1 # min value on current main series
    mainSeriesMax: 1 # max value on current main series

    _min = 1 # current min value
    _max = 1 # current max value

    def _setupUi(self) -> None:
        self._insertRangeSlider()
        self._min = 1
        self._max = 1
        self.trimmerChanged.connect(self.model.trimRows)
        self.model.mainSeriesLengthChanged.connect(lambda value: self.setMainRange(1, value))

    def _insertRangeSlider(self):
        self.setEnabled(False)
        self.sliderFilter = QRangeSlider(self)
        self.sliderFilter.setOrientation(Qt.Orientation.Horizontal)
        self.sliderFilter.setObjectName("verticalSlider")
        self.sliderFilter.setRange(1, 2)
        self.sliderFilter.applyMacStylePatch()
        self.sliderFilter.setSliderPosition([self._max, self._min])
        self.spinBoxRangeMax.setValue(self._max)
        self.spinBoxRangeMin.setValue(self._min)
        self.horizontalLayout.insertWidget(1, self.sliderFilter, 1)

        self.spinBoxRangeMax.valueChanged.connect(self.maxSpinnerChanged)
        self.spinBoxRangeMin.valueChanged.connect(self.minSpinnerChanged)
        self.sliderFilter.valueChanged.connect(self.sliderValueChanged)

    def setMainRange(self, min:int, max:int):
        if min > max: raise ValueError("Value error for setting range Max < Min!!!")
        if min == self._min and max == self._max: return

        self.mainSeriesMin = min
        self.mainSeriesMax = max
        self._min = min
        self._max = max

        self._blockAllSignals(True)
        self.spinBoxRangeMin.setRange(min, max - 1)
        self.spinBoxRangeMax.setRange(min + 1, max)

        self.sliderFilter.setRange(min, max if max > min else min + 1)

        self.spinBoxRangeMin.setValue(min)
        self.spinBoxRangeMax.setValue(max)

        self.sliderFilter.setSliderPosition([min, max])
        self._blockAllSignals(False)
        self._trimmerChanged()
        self.setEnabled(self._max - self._min > 1)

    def sliderValueChanged(self, tuple):
        min, max = tuple
        self._blockAllSignals(True)
        if self.spinBoxRangeMin.value() != int(min):
            self.spinBoxRangeMin.setValue(int(min))
            self.spinBoxRangeMax.setRange(int(min) + 1, self.mainSeriesMax)

        if self.spinBoxRangeMax.value() != int(max):
            self.spinBoxRangeMax.setValue(int(max))
            self.spinBoxRangeMin.setRange(self.mainSeriesMin, int(max) - 1)
        self._blockAllSignals(False)
        self._trimmerChanged()
        pass

    def minSpinnerChanged(self, value):
        self._blockAllSignals(True)
        self.sliderFilter.setSliderPosition((value, self._max))
        self.spinBoxRangeMax.setRange(value + 1, self.mainSeriesMax)
        self._blockAllSignals(False)
        self._trimmerChanged()
        pass

    def maxSpinnerChanged(self, value):
        self._blockAllSignals(True)
        self.sliderFilter.setSliderPosition((self._min, value))
        self.spinBoxRangeMin.setRange(self.mainSeriesMin, value-1)
        self._blockAllSignals(False)
        self._trimmerChanged()
        pass

    def _trimmerChanged(self):
        if (self.spinBoxRangeMin.value() != int(self._min) or
            self.spinBoxRangeMax.value() != int(self._max)):
            self._min = self.spinBoxRangeMin.value()
            self._max = self.spinBoxRangeMax.value()
            self.trimmerChanged.emit((self._min, self._max))
            pass

    def _blockAllSignals(self, isBlocked: bool):
        self.spinBoxRangeMax.blockSignals(isBlocked)
        self.spinBoxRangeMin.blockSignals(isBlocked)
        self.sliderFilter.blockSignals(isBlocked)