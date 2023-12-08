import jsonpickle
from typing import Any, Type

from config import *
from dto import CalcColumnDto

from PySide6.QtCore import QModelIndex, QObject, Qt, QPersistentModelIndex, QAbstractTableModel

class ColumnModel:
    def __init__(self, title:str, editable: bool, dtoAttributeType: Type, dtoAttributeName: str) -> None:
        self.title = title
        self.editable = editable
        self.dtoAttributeType = dtoAttributeType
        self.dtoAttributeName = dtoAttributeName
        pass

class CalcColumnModel(QAbstractTableModel):
    _headers: list[ColumnModel] = [
        ColumnModel("Title",      False, str,  'name'),
        ColumnModel("Expression", False, str,  'expression')
    ]
    allColumns:list[CalcColumnDto] = []

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)
        self.dataChanged.connect(self._saveColumns)
        self.rowsInserted.connect(self._saveColumns)
        self.rowsRemoved.connect(self._saveColumns)
        self.allColumns = self._loadColumns()
        pass

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        if not index.isValid(): return None

        elif role in (Qt.ItemDataRole.EditRole, Qt.ItemDataRole.DisplayRole):
            if index.column() == 0:
                return self.allColumns[index.row()].name
            if index.column() == 1:
                return self.allColumns[index.row()].expression

        elif role == Qt.ItemDataRole.UserRole:
            return self.allColumns[index.row()]

        if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
            return Qt.CheckState.Checked if self.allColumns[index.row()].active else Qt.CheckState.Unchecked

    def setData(self, index: QModelIndex | QPersistentModelIndex, value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.CheckStateRole and index.isValid() and index.column() == 0:
            self.allColumns[index.row()].active = value == Qt.CheckState.Checked.value

        elif role == Qt.ItemDataRole.UserRole and index.isValid():
            self.allColumns[index.row()] = value

        else:
            return super().setData(index, value, role)

        self.dataChanged.emit(index, index)
        return True

    def addCalcColumn(self, dto: CalcColumnDto):
        rowCount = self.rowCount()
        self.beginInsertRows(QModelIndex(), rowCount, rowCount)
        self.allColumns.append(dto)
        self.endInsertRows()

    def hasColumn(self, title:str)->bool:
        return len([i for i in self.allColumns if i.name == title][:]) > 0

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self.allColumns)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._headers)

    def index(self, row: int, column: int, parent: QModelIndex | QPersistentModelIndex = ...) -> QModelIndex:
        if column != 0: return super().index(row, column, parent)
        return self.createIndex(row, 0, self.allColumns[row])

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Vertical:
            return section + 1

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section].title

    def removeRow(self, row: int, parent: QModelIndex | QPersistentModelIndex = ...) -> bool:
        index = self.index(row, 0)
        self.beginRemoveRows(index.parent(), row, row)
        del self.allColumns[row]
        self.endRemoveRows()
        return True

    def removeRows(self, row: int, count: int, parent: QModelIndex | QPersistentModelIndex = ...) -> bool:
        index = self.index(row, 0)
        self.beginRemoveRows(index.parent(), row, row + count)
        del self.allColumns[row:row + count]
        self.dataChanged.emit(index, index.siblingAtColumn(self.columnCount()-1))
        self.endRemoveRows()
        return True

    def flags(self, index: QModelIndex | QPersistentModelIndex) -> Qt.ItemFlag:
        if not index.isValid(): return Qt.ItemFlag.NoItemFlags

        flags = super().flags(index)
        if index.column() == 0: flags |= Qt.ItemFlag.ItemIsUserCheckable
        return flags

    def _saveColumns(self):
        serialized = jsonpickle.encode(self.allColumns)
        Config.setValueG(ConfigGroup.ProcessingDockWidget, ConfigAttribute.CustomColumns, serialized)

    def _loadColumns(self):
        jsonData = Config.valueG(ConfigGroup.ProcessingDockWidget, ConfigAttribute.CustomColumns, [])
        return jsonpickle.decode(jsonData)

    def iterateAll(self, filterFunction:callable = None) -> CalcColumnDto:
        for row in range(self.rowCount(QModelIndex())):
            index = self.index(row, 0, QModelIndex())
            item = index.internalPointer()
            if filterFunction is None or filterFunction(item):
                yield item, index
        pass
