import typing
from abc import abstractmethod

from qtpy.QtCore import Signal
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPalette, QColor, QColorConstants, QMouseEvent, QAction, QContextMenuEvent
from PySide6.QtWidgets import QWidget, QDockWidget, QColorDialog, QHeaderView, QStyledItemDelegate,  QMenu
from models import TrackPointsModel
from StatusMessage import StatusMessage

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