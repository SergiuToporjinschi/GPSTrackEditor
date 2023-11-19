from qtpy.QtCore import Signal
from typing import Any
import json
from JSONTree import JSONTreeItem
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt, QPersistentModelIndex
from PySide6.QtWidgets import QLabel
from Delegates import ExtRoles

class JsonTreeModel(QAbstractItemModel):
    configChanged = Signal(str)
    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)

        self._headers = ("Property", "Value")
        self._rootItem = JSONTreeItem()

    def clear(self):
        self.load({})

    def load(self, document: dict):
        self.beginResetModel()
        self._rootItem = JSONTreeItem.load(document)
        self._rootItem.valueType = type(document)
        self.endResetModel()
        self.configChanged.emit(self.toJSONString())
        return True

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return self._attributeToTitle(item.attribute)
            if index.column() == 1:
                return item.value
        elif role == Qt.ItemDataRole.EditRole:
            if index.column() == 1:
                return item.value
        elif role == ExtRoles.ValueType:
            return item.valueType
        elif role == ExtRoles.Item:
            return item

    def setData(self, index: QModelIndex | QPersistentModelIndex, value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 1:
                item = index.internalPointer()
                item.value = value
                self.dataChanged.emit(index, index, [Qt.ItemDataRole.EditRole])
                self.configChanged.emit(self.toJSONString())
                return True

        return False

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return 2

    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

    def index(self, row: int, column: int, parent=QModelIndex()) -> QModelIndex:
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index: QModelIndex) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self._rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def flags(self, index: QModelIndex | QPersistentModelIndex) -> Qt.ItemFlag:
        flags = super(JsonTreeModel, self).flags(index)
        item = self.data(index, ExtRoles.Item)
        if index.column() == 1 and item.childCount() <= 0:
            return Qt.ItemFlag.ItemIsEditable | flags
        else:
            return flags

    def _attributeToTitle(self, value: str):
        transformedValue = ''
        for char in value:
            if char.isupper() and transformedValue:
                transformedValue += ' ' + char
            else:
                transformedValue += char
        return transformedValue.capitalize()

    def toJSONString(self, item=None):
        return json.dumps(self.toJSON())

    def toJSON(self, item=None):
        if item is None:
            item = self._rootItem

        childCount = item.childCount()

        if item.valueType is dict:
            document = {}
            for i in range(childCount):
                ch = item.child(i)
                document[ch.attribute] = self.toJSON(ch)
            return document

        elif item.valueType == list:
            document = []
            for i in range(childCount):
                ch = item.child(i)
                document.append(self.toJSON(ch))
            return document

        else:
            return item.value
