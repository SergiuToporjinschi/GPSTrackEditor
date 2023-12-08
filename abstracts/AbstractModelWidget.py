import typing
import enum
from abc import abstractmethod

from qtpy.QtCore import Signal, QObject
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QAction, QContextMenuEvent
from PySide6.QtWidgets import QWidget, QDockWidget, QMenu

from models import TrackPointsModel
from StatusMessage import StatusMessage

class FrameState(enum.Enum):
    View = 1
    Edit = 2

class AbstractNotificationWidget:
    startProcessing = Signal()            # before processing data (to clear the status maybe)
    statusMessage = Signal(StatusMessage) # sending messages for status bar (text, time, color)
    updateProgress = Signal(int)          # incrementing the progress bar
    finishedProcessing = Signal()         # processing finished (for resetting the status bar maybe)
    stateChanged = Signal(FrameState)

    _state: FrameState = FrameState.View

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: FrameState):
        self._state = state
        self.stateChanged.emit(state)
        self._refreshWidget()

    def setState(self, state: FrameState):
        self.state = state

    def isEditMode(self) -> bool:
        return self._state == FrameState.Edit

    def isViewMode(self) -> bool:
        return self._state == FrameState.View

    def _refreshWidget(self):
        for i in vars(self):
            obj:QObject = vars(self)[i]
            if isinstance(obj, QWidget) and obj.property('activeOnState') is not None:
                obj.setEnabled(obj.property('activeOnState') == self._state.value)


class AbstractModelWidget(AbstractNotificationWidget):
    def __init__(self, parent: typing.Optional[QWidget] = ..., model:typing.Optional[TrackPointsModel]=...) -> None:
        super().__init__()
        self.model = model
        self.setupUi(self)
        self._setupUi()

    @abstractmethod
    def _setupUi(self):
        pass

class AbstractWidgetMaximizeable(QDockWidget):

    def contextMenuEvent(self, event: QContextMenuEvent):
        context_menu = QMenu(self)
        # Connect actions to functions

        action1 = QAction("Normalize" if self.isMaximized() else "Maximize", self)

        action1.triggered.connect(self.maximize)

        context_menu.addAction(action1)
        context_menu.exec_(event.globalPos())

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()