import enum

from PySide6.QtGui import QColor

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