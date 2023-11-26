from typing import Union
from delegates import ExtRoles
from .ColumnModel import ColumnModel

from PySide6.QtCore import Qt, QObject, QModelIndex, QPersistentModelIndex, QSize
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QStyledItemDelegate, QColorDialog,QStyleOptionViewItem

class MarkerListDelegate(QStyledItemDelegate):
    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        pass

    def createEditor(self, parent, option, index):
        colModel: ColumnModel = index.model().data(index, ExtRoles.ColModel)
        value = index.model().data(index, Qt.ItemDataRole.EditRole)
        if colModel.editControl == QColorDialog:
            colorDialog = QColorDialog(parent)
            colorDialog.setCurrentColor(QColor(value))
            return colorDialog
        return super().createEditor(parent, option, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QColorDialog):
            value = editor.selectedColor().name()
            model.setData(index, value, Qt.ItemDataRole.EditRole)
        else:
            return super().setModelData(editor, model, index)
