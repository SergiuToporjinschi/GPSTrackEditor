import enum

from qtpy.QtCore import Signal

from gui.status_bar_ui import Ui_GroupBox
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QFrame

class StatusMessage:
    class MsgType(enum.Enum):
        reset = None

    _message: str = ''
    _time: int = None
    _color: QColor = None
    def __init__(self, msg: str=None, time: int=None, color: QColor=None) -> None:
        self._message = msg
        self._time = time
        self._color = color
        pass

    @property
    def message(self):
        return self._message

    @property
    def time(self):
        return self._time

    @property
    def color(self):
        return self._color

    def __str__(self) -> str:
        return f"{self._message} [{self._time, self._color}]"


class StatusBarGroupBox(QFrame, Ui_GroupBox):
    updateProgress = Signal(int)                  # connected to progress bar (value to display)
    updateTrimmerLen = Signal(int)                # connected to Trim (value to display)
    updateTackLen = Signal(int)                   # update track length (value to display)
    updateMessage = Signal(StatusMessage)         # sets a message which will disappear a after a time

    _whiteColor = QColor('white')
    _timer = QTimer()
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._timer.setSingleShot(True)
        self._timer.setTimerType(Qt.TimerType.CoarseTimer)
        self._timer.timeout.connect(lambda: self.updateProgress.emit(0))

        self.updateMessage.connect(self._updateMessage)

    def _updateMessage(self, msg: StatusMessage):
        if msg is None:
            self._clearMessage()
            return
        self.labelMessage.setText(msg.message if msg != None else '')
        color = msg.color if msg is not None and msg.color != None else self._whiteColor
        self.labelMessage.setStyleSheet(f"color: {color.name()}")
        if msg.time is not None:
            self._timer.start(msg.time)
        else:
            self._timer.stop()

    def _clearMessage(self):
        self.labelMessage.setText('')
        self.labelMessage.setStyleSheet(f"color: {self._whiteColor.name()}")
        self._timer.stop()

