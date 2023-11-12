from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStyleOptionViewItem, QStyledItemDelegate, QWidget
import datetime
import pytz

from typing import Any
class DateTimeDelegate(QStyledItemDelegate):
    def __init__(self, editFormat: str, displayFormat: str) -> None:
        super().__init__()
        self.editFormat = editFormat
        self.displayFormat = displayFormat

    def initStyleOption(self, option: QStyleOptionViewItem, index: QtCore.QModelIndex) -> None:
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter
        super().initStyleOption(option, index)

    def createEditor(self,  parent: QWidget, option: QStyleOptionViewItem, index: QtCore.QModelIndex):
        dateTimeEdit = QtWidgets.QDateTimeEdit(parent)
        dateTimeEdit.setMinimumSize(QtCore.QSize(196, 0))
        dateTimeEdit.setMaximumSize(QtCore.QSize(167, 16777215))
        dateTimeEdit.setCalendarPopup(True)
        dateTimeEdit.setTimeSpec(QtCore.Qt.TimeSpec.UTC)
        dateTimeEdit.setObjectName("dateTimeEdit")
        dateTimeEdit.setDisplayFormat(self.editFormat)
        return dateTimeEdit

    def setEditorData(self, editor, index):
        if isinstance(editor, QtWidgets.QDateTimeEdit):
            value = index.model().data(index, Qt.ItemDataRole.EditRole)
            editor.setDateTime(value)
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QtWidgets.QDateTimeEdit):
            value = editor.dateTime().toPyDateTime().replace(tzinfo=pytz.UTC)
            model.setData(index, value, Qt.ItemDataRole.EditRole)
        else:
            super().setModelData(editor, model, index)

    def displayText(self, value: Any, locale: QtCore.QLocale):
        if isinstance(value, datetime.datetime):
            return value.strftime(self.displayFormat)
        return super().displayText(value, locale)

class FloatDelegate(QStyledItemDelegate):
    def __init__(self, min:int, max:int, dec:int) -> None:
        super().__init__()
        self.min = min
        self.max = max
        self.dec = dec

    def initStyleOption(self, option: QStyleOptionViewItem, index: QtCore.QModelIndex) -> None:
        option.displayAlignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        super().initStyleOption(option, index)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QtCore.QModelIndex) -> QWidget:
        spinner = QtWidgets.QDoubleSpinBox(parent)
        spinner.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        spinner.setMinimum(self.min)
        spinner.setMaximum(self.max)
        spinner.setDecimals(self.dec)
        if self.dec is None or self.dec == 0:
            spinner.setSingleStep(1)
            spinner.setStepType(QtWidgets.QAbstractSpinBox.StepType.DefaultStepType)
        else:
            spinner.setSingleStep(10**self.dec)
        return spinner

    def displayText(self, value: Any, locale: QtCore.QLocale) -> str:
            #         value = self.trackPoints[index.row()].getValueByColumnIndex(index.column())
            # if isinstance(value, (float, int)):
            #     return '{:,}'.format(value).replace(',', ' ')
            # else:
            #     return value

        if isinstance(value, float):
            noOfDec = self.dec
            return f"{value:,.{noOfDec}f}".replace(',', ' ') if value is not None else None
        return super().displayText(value, locale)

class ListOfValuesDelegate(QStyledItemDelegate):
    def __init__(self, *values:str) -> None:
        super().__init__()
        self.values = values

    def initStyleOption(self, option: QStyleOptionViewItem, index: QtCore.QModelIndex) -> None:
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter
        super().initStyleOption(option, index)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QtCore.QModelIndex) -> QWidget:
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

    def displayText(self, value: Any, locale: QtCore.QLocale) -> str:
        if isinstance(value, str):
            for index, display in self.values:
                if index == value:
                    return display
        return super().displayText(value, locale)
