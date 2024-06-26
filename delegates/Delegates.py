import pytz, enum, numpy
from datetime import datetime
from typing import Any

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QModelIndex, QSize, QLocale, QObject, QPersistentModelIndex
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QStyleOptionViewItem, QStyledItemDelegate, QWidget, QComboBox, QSpinBox, QColorDialog, QTableView

class ExtRoles(enum.Enum):
    ValueType = Qt.ItemDataRole.UserRole + 1
    Item = ValueType + 1
    ColModel = Item + 1
    pass



class DateTimeDelegate(QStyledItemDelegate):
    def __init__(self, editFormat: str, displayFormat: str, parent:QTableView = None) -> None:
        super().__init__(parent=parent)
        self.editFormat = editFormat
        self.displayFormat = displayFormat

    def initStyleOption(self, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter
        super().initStyleOption(option, index)

    def createEditor(self,  parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        dateTimeEdit = QtWidgets.QDateTimeEdit(parent)
        dateTimeEdit.setMinimumSize(QSize(196, 0))
        dateTimeEdit.setMaximumSize(QSize(167, 16777215))
        dateTimeEdit.setCalendarPopup(True)
        dateTimeEdit.setTimeSpec(Qt.TimeSpec.UTC)
        dateTimeEdit.setObjectName("dateTimeEdit")
        dateTimeEdit.setDisplayFormat(self.editFormat)
        return dateTimeEdit

    def setEditorData(self, editor:QtWidgets.QDateTimeEdit, index: QModelIndex | QPersistentModelIndex):
        if isinstance(editor, QtWidgets.QDateTimeEdit):
            value = index.data(Qt.ItemDataRole.EditRole)
            editor.setDateTime(value)
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QtWidgets.QDateTimeEdit):
            value = editor.dateTime().toPyDateTime().replace(tzinfo=pytz.UTC)
            model.setData(index, value, Qt.ItemDataRole.EditRole)
        else:
            super().setModelData(editor, model, index)

    def displayText(self, value: Any, locale: QLocale):
        if isinstance(value, datetime):
            return value.strftime(self.displayFormat)
        return super().displayText(value, locale)



class FloatDelegate(QStyledItemDelegate):
    def __init__(self, min:int, max:int, dec:int, parent:QTableView = None) -> None:
        super().__init__(parent=parent)
        self.min = min
        self.max = max
        self.dec = dec

    def initStyleOption(self, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        option.displayAlignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        super().initStyleOption(option, index)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        self.spinner = QtWidgets.QDoubleSpinBox(parent)
        self.spinner.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.spinner.setMinimum(self.min)
        self.spinner.setMaximum(self.max)
        self.spinner.setDecimals(self.dec)
        if self.dec is None or self.dec == 0:
            self.spinner.setSingleStep(1)
            self.spinner.setStepType(QtWidgets.QAbstractSpinBox.StepType.DefaultStepType)
        else:
            self.spinner.setSingleStep(10**self.dec)
        return self.spinner

    def setEditorData(self, editor: QtWidgets.QDoubleSpinBox, index: QModelIndex | QPersistentModelIndex) -> None:
        if isinstance(editor, QtWidgets.QDoubleSpinBox):
            editor.setValue(index.data(Qt.ItemDataRole.EditRole))
        else:
            super().setEditorData(editor, index)

    def displayText(self, value: Any, locale: QLocale) -> str:
        if isinstance(value, float):
            noOfDec = self.dec
            return f"{value:,.{noOfDec}f}".replace(',', ' ') if value is not None else None
        return super().displayText(value, locale)

class IntDelegate(QStyledItemDelegate):
    def __init__(self, min:int, max:int, parent:QTableView = None) -> None:
        super().__init__(parent)
        self.min = min
        self.max = max

    def initStyleOption(self, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        option.displayAlignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        super().initStyleOption(option, index)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        spinner = QtWidgets.QSpinBox(parent)
        spinner.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        spinner.setMinimum(self.min)
        spinner.setMaximum(self.max)
        spinner.setSingleStep(1)
        spinner.setStepType(QtWidgets.QAbstractSpinBox.StepType.DefaultStepType)
        return spinner

    def setEditorData(self, editor: QtWidgets.QSpinBox, index: QModelIndex | QPersistentModelIndex) -> None:
        if isinstance(editor, QtWidgets.QSpinBox):
            editor.setValue(index.data(Qt.ItemDataRole.EditRole))
        else:
            super().setEditorData(editor, index)

    def displayText(self, value: Any, locale: QLocale) -> str:
        if isinstance(value, numpy.int64):
            return f"{value}".replace(',', ' ') if value is not None else None
        return super().displayText(value, locale)

class ListOfValuesDelegate(QStyledItemDelegate):
    def __init__(self, *values:str, parent:QTableView = None) -> None:
        super().__init__(parent=parent)
        self.values = values

    def initStyleOption(self, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter
        super().initStyleOption(option, index)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        combo = QtWidgets.QComboBox(parent)
        for value, display in self.values:
            combo.addItem(display)
        return combo

    def setModelData(self, editor, model, index):
        if isinstance(editor, QtWidgets.QComboBox):
            value = editor.currentText()
            for i, display in self.values:
                if display == value:
                    model.setData(index, i, Qt.ItemDataRole.EditRole)
                    break
        super().setModelData(editor, model, index)

    def displayText(self, value: Any, locale: QLocale) -> str:
        if isinstance(value, str):
            for index, display in self.values:
                if index == value:
                    return display
        return super().displayText(value, locale)


class MapSettingsDelegate(QStyledItemDelegate):
    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
    pass

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex) -> QSize:
        size = super().sizeHint(option, index)
        size.setHeight(22)
        return size

    def createEditor(self, parent, option, index):
        dataType = index.model().data(index, ExtRoles.ValueType)
        value = index.model().data(index, Qt.ItemDataRole.EditRole)
        jsonNode = index.internalPointer()
        if jsonNode.attribute == 'color':
            colorDialog = QColorDialog(parent)
            colorDialog.setCurrentColor(QColor(value))
            return colorDialog
        elif dataType == str:
            editor = QComboBox(parent)
            editor.addItems(["red", "blue", "green", "yellow"])
            return editor
        elif dataType == int:
            editor = QSpinBox(parent)
            editor.setValue(value)
            return editor
        return super().createEditor(parent, option, index)

    def setEditorData(self, editor: QWidget, index: QModelIndex | QPersistentModelIndex) -> None:
        dataType = index.model().data(index, ExtRoles.ValueType)
        value = index.model().data(index, Qt.ItemDataRole.EditRole)
        if isinstance(dataType, str):
            editor.setCurrentText(value)
        elif isinstance(dataType, int):
            editor.setValue(int(value))
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QColorDialog):
            value = editor.selectedColor().name()
        elif isinstance(editor, QComboBox):
            # editor.children()[0].text()
            value = editor.currentText()
        elif isinstance(editor, QSpinBox):
            value = editor.value()
        else:
            return super().setModelData(editor, model, index)
        model.setData(index, value, Qt.ItemDataRole.EditRole)

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex) -> None:
        item = index.internalPointer()
        if index.column() == 1 and item.attribute == 'color':  # Assuming you want to set the background color in the second column (column index 1)
            painter.fillRect(option.rect, QColor(item.value))
            QStyledItemDelegate.paint(self, painter, option, index)
        return super().paint(painter, option, index)

    def displayText(self, value: Any, locale: QLocale ) -> str:
        return super().displayText(value, locale)

class DisplayCalculatedColumn(QStyledItemDelegate):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)

    def displayText(self, value: Any, locale: QLocale) -> str:
        if type(value) in (float, numpy.float16, numpy.float32, numpy.float64):
            return f"{value:,.{2}f}".replace(',', ' ') if value is not None else None
        elif type(value) in (int, numpy.int64, numpy.int16, numpy.int32, numpy.int64):
            return f"{value}".replace(',', ' ') if value is not None else None
        else:
            return super().displayText(value, locale)
