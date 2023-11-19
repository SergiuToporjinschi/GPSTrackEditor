from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QColorDialog, QWidget, QLineEdit
from PySide6.QtGui import QPalette, QColor, QColorConstants, QKeyEvent, QMouseEvent
from typing import Any, ClassVar, Dict, Iterable, List, Optional, Sequence, Text, Tuple, Type, Union, overload
from PySide6.QtCore import Signal, SignalInstance

class ColorSelectorWidget(QWidget):
    activated                : Signal
    currentIndexChanged      : Signal
    currentTextChanged       = Signal(str)
    editTextChanged          = Signal(str)
    highlighted              : Signal
    textActivated            : Signal
    textHighlighted          : Signal
    def __init__(self, text, parent=None):
        super().__init__(None)
        self.edit = QLineEdit(text)
        # self.edit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.edit.setAutoFillBackground(True)
        self.mousePressEvent = lambda event: self.openColorDialog(self.edit)

        self.value = '#000'
        # self.clicked.connect(lambda _: self._onClicked())

    def openColorDialog(self, line_edit):
        color_dialog = QColorDialog()
        color = color_dialog.getColor()

        if color.isValid():
            self.value = color.name()
        self.editTextChanged.emit(self.value)
        self.currentTextChanged.emit(self.value)
            # line_edit.setText(color.name())

    def getValue(self) ->QColor:
        return self.value

    # clicked                  : ClassVar[Signal] = ... # clicked()
    # pressed                  : ClassVar[Signal] = ... # pressed()
    # released                 : ClassVar[Signal] = ... # released()
    # toggled                  : ClassVar[Signal] = ... # toggled(bool)
    # def click(self) -> None:
    #     return super().click()

    # def mousePressEvent(self, e: QMouseEvent) -> None:
    #     color = QColorDialog.getColor()
    #     if color.isValid():
    #         pal = QPalette()
    #         pal.setColor(QPalette.ColorRole.Button, color)
    #     # return super().mousePressEvent(e)

    # def mouseReleaseEvent(self, e: QMouseEvent) -> None:
    #     return super().mouseReleaseEvent(e)

    # def _onClicked(self):
    #     color = QColorDialog.getColor()
    #     if color.isValid():
    #         pal = QPalette()
    #         pal.setColor(QPalette.ColorRole.Button, color)
    #         self.setPalette(pal)
    #     pass

