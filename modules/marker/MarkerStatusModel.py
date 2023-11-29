import jsonpickle
from enum import Enum
from typing import Any, Union
from config import *
from delegates import ExtRoles
from dto import MarkerDto, MarkerGroupDto
from .ColumnModel import ColumnModel
from PySide6.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt, QPersistentModelIndex
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QBrush, QColor
class MarkerCategory(Enum):
    Custom = 'Custom'
    Stationary = 'Stationary'
    pass

class MarkerStatusModel(QAbstractItemModel):
    _headers: list[ColumnModel] = [
        ColumnModel("Type",       False, None,         str,  'name'),
        ColumnModel("Color",      True,  QColorDialog, str,  'color'),
        ColumnModel("Expression", False, None,         str,  'expression'),
        ColumnModel("No.",        False, None,         int,  'countIndexes'),
        ColumnModel("Active",     True,  None,         bool, 'active')
    ]

    _markerData:list[MarkerGroupDto]
    def __init__(self, parent: QObject = None) -> None:
        self._markerData = self._loadMarkers()

        # self._markerData.append(MarkerGroupDto("Custom"))
        # self._markerData.append(MarkerGroupDto("Stationary"))
        super().__init__(parent)
        pass

    def headerModels(self) -> list[ColumnModel]:
        return self._headers

    def headerModelIndex(self, dtoAttribute:str) -> int:
        returnValue = None
        for i, item in enumerate(self._headers):
            if item.dtoAttributeName == dtoAttribute:
                returnValue = i
                break
        return returnValue

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        if not index.isValid(): return None

        item = index.internalPointer()
        colModel = self._headers[index.column()]

        if role == ExtRoles.Item:
            return item

        elif role == ExtRoles.ColModel:
            return colModel

        elif role in (Qt.ItemDataRole.EditRole, Qt.ItemDataRole.DisplayRole):
            result = self._dataByEditDisplayRole(item, colModel, index)
            self._saveMarkers()
            return result
        elif role == Qt.ItemDataRole.CheckStateRole:
            return self._dataByCheckStateRole(item, colModel, index)

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return self._dataByTextAlignmentRole(item, colModel, index)

        elif role == Qt.ItemDataRole.ForegroundRole:
            return self._dataByForegroundRole(item, colModel, index)

        elif role == Qt.ItemDataRole.BackgroundRole:
            return self._dataByBackgroundRole(item, colModel, index)
        return None

    def setData(self, index: QModelIndex | QPersistentModelIndex, value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.EditRole and Qt.ItemFlag.ItemIsEditable in self.flags(index):
            item:MarkerDto = index.internalPointer()
            headerModel = self._headers[index.column()]

            if headerModel.dtoAttributeName is None: return False

            setattr(item, headerModel.dtoAttributeName, value)

            self.dataChanged.emit(index, index, [
                Qt.ItemDataRole.EditRole,
                Qt.ItemDataRole.DisplayRole,
                Qt.ItemDataRole.CheckStateRole,
                Qt.ItemDataRole.BackgroundRole
                ])
            return True
        return False

    def index(self, row: int, column: int, parent: QModelIndex | QPersistentModelIndex = ...) -> QModelIndex:
        if parent.isValid() and parent.column() != 0:
            return QModelIndex()
        if not self.hasIndex(row, column, parent): return QModelIndex()

        if not parent.isValid(): #is root
            parentItem = self._markerData
        else:
            parentItem = parent.internalPointer()

        if parentItem == self._markerData:
            children = parentItem[row]
        elif isinstance(parentItem, MarkerGroupDto):
            children = parentItem.markers[row]
        elif isinstance(parentItem, MarkerDto):
            children = None

        if children:
            return self.createIndex(row, column, children)
        else:
            return QModelIndex()
        pass

    def parent(self, childIndex: QModelIndex) -> QModelIndex:
        if not childIndex.isValid():
            return QModelIndex()

        childItem = childIndex.internalPointer()

        parent = None

        if childItem is None:
            parent = None
        elif isinstance(childItem, MarkerGroupDto):
            parent = self._markerData
        elif isinstance(childItem, MarkerDto):
            for i in self._markerData:
                if i.category == childItem.category:
                    parent = i
                    break

        if parent is None:
            return QModelIndex()
        elif parent == self._markerData:
            poz = self._markerData.index(childItem)
            return self.createIndex(poz, 0, parent)
        elif isinstance(parent, MarkerGroupDto):
            for index, item in enumerate(self._markerData):
                if item.category == childItem.category:
                    return self.createIndex(index, 0, parent)
        elif isinstance(parent, MarkerDto):
            return QModelIndex()

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self._markerData
        else:
            parentItem = parent.internalPointer()

        if parentItem == self._markerData:
            return len(parentItem)
        elif isinstance(parentItem, MarkerGroupDto):
            return len(parentItem.markers)
        elif isinstance(parentItem, MarkerDto):
            return 0
        else:
            return 0

    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            headerTitles = [item.title for item in self._headers][:]
            return headerTitles[section]

    def removeRow(self, row: int, parent: QModelIndex | QPersistentModelIndex = ...) -> bool:
        if not parent.isValid(): return False
        self.beginRemoveRows(parent, row, 1)

        group:MarkerGroupDto = parent.internalPointer()
        del group.markers[row]

        self.endRemoveRows()
        self._saveMarkers()
        return True

    def addRow(self, item: MarkerDto) -> bool:
        parentIndex = None
        grp:MarkerGroupDto = None
        # Find parent
        for row in range(self.rowCount(QModelIndex())):
            index = self.index(row, 0, QModelIndex())
            grp = self.data(index, ExtRoles.Item)
            if grp.category == item.category:
                parentIndex  = index
                break

        # Add marker
        if parentIndex is not None and grp is not None:
            self.beginInsertRows(parentIndex, len(grp.markers), 1)
            grp.markers.append(item)
            self.endInsertRows()
            self._saveMarkers()
        return True

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._headers)

    def flags(self, index: QModelIndex | QPersistentModelIndex) -> Qt.ItemFlag:
        flags = super(MarkerStatusModel, self).flags(index)
        if self._headers[index.column()].editable:
            return Qt.ItemFlag.ItemIsEditable | flags
        return flags

    def _dataByEditDisplayRole(self, item:Union[MarkerDto, MarkerGroupDto], colModel:ColumnModel, index:QModelIndex):
        if isinstance(item, MarkerGroupDto):
            if index.column() == 0: return item.category
            else: return None

        elif isinstance(item, MarkerDto):
            if colModel.dtoAttributeType == Enum:
                return getattr(item, colModel.dtoAttributeName).name
            elif colModel.dtoAttributeType == bool: return None
            else:
                attrName = colModel.dtoAttributeName
                return getattr(item, attrName) if attrName is not None else None
        else: return None

    def _dataByCheckStateRole(self, item:Union[MarkerDto, MarkerGroupDto], colModel:ColumnModel, index:QModelIndex):
        if isinstance(item, MarkerDto) and colModel.dtoAttributeType == bool:
            value = getattr(item, colModel.dtoAttributeName)
            return Qt.CheckState.Checked if value else Qt.CheckState.Unchecked

    def _dataByTextAlignmentRole(self, item:Union[MarkerDto, MarkerGroupDto], colModel:ColumnModel, index:QModelIndex):
        if index.column() > 0:
            return Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter

    def _dataByBackgroundRole(self, item:Union[MarkerDto, MarkerGroupDto], colModel:ColumnModel, index:QModelIndex):
        if isinstance(item, MarkerDto) and colModel.editControl == QColorDialog:
            val = getattr(item, colModel.dtoAttributeName)
            return QBrush(val) if val is not None else 'black'

    def _dataByForegroundRole(self, item:Union[MarkerDto, MarkerGroupDto], colModel:ColumnModel, index:QModelIndex):
        if isinstance(item, MarkerDto) and colModel.editControl == QColorDialog:
            lum = QColor(item.color).lightnessF()
            return QColor('white') if lum < 0.4 else QColor('black')

    def _saveMarkers(self):
        serialized = jsonpickle.encode(self._markerData)
        Config.setValueG(ConfigGroup.MarkingDockWidget, ConfigAttribute.Markers, serialized)

    def _loadMarkers(self):
        jsonData = Config.valueG(ConfigGroup.MarkingDockWidget, ConfigAttribute.Markers, None)

        if jsonData is None: return [MarkerGroupDto(MarkerCategory.Custom.name), MarkerGroupDto(MarkerCategory.Stationary.name)]

        return jsonpickle.decode(jsonData)


