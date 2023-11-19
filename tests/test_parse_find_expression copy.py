# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import json
import sys, enum
from typing import Any, List, Dict, Optional, Union
from JSONTree import JSONTreeItem
from PySide6.QtWidgets import QTreeView, QApplication, QHeaderView, QAbstractItemDelegate, QStyleOptionViewItem, QWidget, QStyledItemDelegate, QComboBox, QSpinBox
from PySide6.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt, QFileInfo, QPersistentModelIndex, QSize, QJsonDocument, QLocale

from Delegates import MapSettingsDelegate
from JSONTreeModel import ExtRoles


class JsonModel(QAbstractItemModel):

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
        flags = super(JsonModel, self).flags(index)
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

class x(QStyledItemDelegate):
    def __init__(self, parent: QObject =None) -> None:
        super().__init__(parent)
    pass


    def createEditor(self, parent, option, index):
        dataType = index.model().data(index, ExtRoles.ValueType)
        value = index.model().data(index, Qt.ItemDataRole.EditRole)
        if dataType == str:
            editor = QComboBox(parent)
            editor.addItems(["red", "blue", "green", "yellow"])
            return editor
        elif dataType == int:
            editor = QSpinBox(parent)
            editor.setValue(value)
            return editor

        return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        dataType = index.model().data(index, ExtRoles.ValueType)
        value = index.model().data(index, Qt.ItemDataRole.EditRole)
        if isinstance(dataType, str):
            editor.setCurrentText(value)
        elif isinstance(dataType, int):
            editor.setValue(int(value))
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QComboBox):
            value = editor.currentText()
        elif isinstance(editor, QSpinBox):
            value = editor.value()
        else:
            return super().setModelData(editor, model, index)
        model.setData(index, value, Qt.ItemDataRole.EditRole)

    def displayText(self, value: Any, locale: QLocale ) -> str:
        return super().displayText(value, locale)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    view = QTreeView()
    model = JsonModel()

    view.setModel(model)
    json_data = {
        "mainTrack": {"stroke": {"color": 'gray', "width": 4}},
        "currentPositionPoint": {
            "radius": 6,
            "fill": {"color": 'red'},
            "stroke": {"color": 'white', "width": 2}
        },
        "trimmedTrack": {"stroke": {"color": 'lightgray', "width": 4}},
        "stationaryMarker": {"stroke": {"color": 'red', "width": 4}},
        "customMarker": {"stroke": {"color": 'yellow', "width": 4}},
    }

    json_path = QFileInfo(__file__).absoluteDir().filePath("example.json")
    model.load(json_data)

    view.expandAll()
    view.setItemDelegate(x())
    view.setItemDelegate(MapSettingsDelegate())

    view.show()
    view.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
    view.setAlternatingRowColors(True)
    view.resize(500, 300)
    app.exec()