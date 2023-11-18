import typing
from abc import abstractmethod

from qtpy.QtCore import Signal
from PySide6.QtWidgets import QWidget

from TCXModel import TrackPointsModel
from StatusBar import StatusMessage

class AbstractNotificationWidget:
    startProcessing = Signal()            # before processing data (to clear the status maybe)
    statusMessage = Signal(StatusMessage) # sending messages for status bar (text, time, color)
    updateProgress = Signal(int)          # incrementing the progress bar
    finishedProcessing = Signal()         # processing finished (for resetting the status bar maybe)

class AbstractModelWidget(AbstractNotificationWidget):
    def __init__(self, parent: typing.Optional[QWidget] = ..., model:typing.Optional[TrackPointsModel]=...) -> None:
        super().__init__()
        self.model = model
        self.setupUi(self)
        self._setupUi()

    @abstractmethod
    def _setupUi(self):
        pass