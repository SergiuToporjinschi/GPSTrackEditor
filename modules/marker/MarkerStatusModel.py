import jsonpickle
from enum import Enum
from typing import Any, Union

from config import *
from delegates import ExtRoles
from dto import MarkerDto, MarkerGroupDto, MarkerCategory
from .ColumnModel import ColumnModel
import UtilFunctions as Util

from PySide6.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt, QPersistentModelIndex
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QBrush, QColor

log = Util.initLogging()

class MarkerStatusModel(QAbstractItemModel):
    _headers: list[ColumnModel] = [
        ColumnModel("Type",       False, None,         str,  'name'),
        ColumnModel("Color",      True,  QColorDialog, str,  'color'),
        ColumnModel("Expression", False, None,         str,  'expression'),
        ColumnModel("No.",        False, None,         int,  'countIndexes')
    ]

    _markerData:list[MarkerGroupDto]
    def __init__(self, parent: QObject = None) -> None:
        self._markerData = self._loadMarkers()
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

        if role == ExtRoles.ColModel:
            return colModel

        elif role in (Qt.ItemDataRole.EditRole, Qt.ItemDataRole.DisplayRole):
            result = self._dataByEditDisplayRole(item, colModel, index)
            return result

        elif role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
            return self._dataByCheckStateRole(item, colModel, index)

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return self._dataByTextAlignmentRole(item, colModel, index)

        elif role == Qt.ItemDataRole.ForegroundRole:
            return self._dataByForegroundRole(item, colModel, index)

        elif role == Qt.ItemDataRole.BackgroundRole:
            return self._dataByBackgroundRole(item, colModel, index)

        elif role == Qt.ItemDataRole.UserRole:
            return index.internalPointer()

        return None

    def setData(self, index: Union[QModelIndex, QPersistentModelIndex], value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.UserRole:
            originalItem:MarkerDto = index.internalPointer()
            if not isinstance(value, MarkerDto): raise RuntimeError(f'Cannot assign {value} to marker category!')
            if not isinstance(originalItem, MarkerDto): raise RuntimeError(f'Original item {originalItem} type not equal with edited item type {value}!')
            if not value.category == originalItem.category: raise RuntimeError(f'Original item category "{originalItem.category}" has changed {value.category}!')
            originalItem.name = value.name
            originalItem.expression = value.expression
            originalItem.indexes = None # reset index
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.UserRole, Qt.ItemDataRole.EditRole, Qt.ItemDataRole.DisplayRole])
            self._saveMarkers()
            return True

        elif role == Qt.ItemDataRole.EditRole:
            item:MarkerDto = index.internalPointer()
            headerModel = self._headers[index.column()]
            if headerModel.dtoAttributeName is None: return False

            setattr(item, headerModel.dtoAttributeName, value)

            self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.BackgroundRole, Qt.ItemDataRole.EditRole])
            self._saveMarkers()
            return True

        elif role == Qt.ItemDataRole.CheckStateRole:
            item:MarkerDto = index.internalPointer()
            if isinstance(item, MarkerDto):
                oldValue = item.active
                item.active = value == Qt.CheckState.Checked.value
                if oldValue != item.active:
                    self.dataChanged.emit(index, index, [Qt.ItemDataRole.CheckStateRole])
                return True

        return False

    def addMarker(self, item:MarkerDto):
        foundCateg = [markerGroup for markerGroup in self._markerData if markerGroup.category == item.category][:]
        if len(foundCateg) <= 0:
            raise RuntimeError(f'Cannot find category for item {item}')

        parentItem:MarkerGroupDto = foundCateg[0]
        parentIndex = self.index(self._markerData.index(parentItem), 0, QModelIndex())
        parentMarkerCnt = len(parentItem.markers)

        self.beginInsertRows(parentIndex, parentMarkerCnt, parentMarkerCnt)
        parentItem.markers.append(item)
        self.endInsertRows()
        self._saveMarkers()
        pass

    def removeRow(self, row: int, parent: QModelIndex | QPersistentModelIndex = ...) -> bool:
        if not parent.isValid(): return False
        group:MarkerGroupDto = parent.internalPointer()

        self.beginRemoveRows(parent, row, row)
        del group.markers[row]
        self.endRemoveRows()

        self._saveMarkers()
        return True

    def flags(self, index: QModelIndex | QPersistentModelIndex) -> Qt.ItemFlag:
        flags = super(MarkerStatusModel, self).flags(index)

        if self._headers[index.column()].editable:
            return Qt.ItemFlag.ItemIsEditable | flags

        if index.column() == 0: flags |= Qt.ItemFlag.ItemIsUserCheckable

        return flags

    def index(self, row: int, column: int, parent: QModelIndex | QPersistentModelIndex = ...) -> QModelIndex: #returns index of row/col from a given parent
        if parent == QModelIndex(): # parent is root -> get markerGroups
            item = self._markerData[row]
            return self.createIndex(row, column, item)

        parentItem = parent.internalPointer()

        if isinstance(parentItem, MarkerGroupDto):
            parentItem:MarkerGroupDto
            item = parentItem.markers[row]
            return self.createIndex(row, column, item)

        raise RuntimeError('Should not reach this line, index()')


    def parent(self, childIndex: QModelIndex) -> QModelIndex: #returns parent of a given index
        if not childIndex.isValid(): return QModelIndex()

        if isinstance(childIndex.internalPointer(), MarkerGroupDto):
            return QModelIndex()

        if isinstance(childIndex.internalPointer(), MarkerDto):
            markerItem:MarkerDto = childIndex.internalPointer()
            for i, groupItem in enumerate(self._markerData):
                groupItem:MarkerGroupDto
                if groupItem.category == markerItem.category:
                    return self.createIndex(i, 0, groupItem)

        raise RuntimeError('Should not reach this line, parent()')

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


    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._headers)

    def _dataByEditDisplayRole(self, item:Union[MarkerDto, MarkerGroupDto], colModel:ColumnModel, index:QModelIndex):
        if isinstance(item, MarkerGroupDto):
            if index.column() == 0: return item.category.value
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
        if isinstance(item, MarkerDto):
            return Qt.CheckState.Checked if item.active else Qt.CheckState.Unchecked

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
        log.debug("Save markers to settings")
        serialized = jsonpickle.encode(self._markerData)
        Config.setValueG(ConfigGroup.MarkingDockWidget, ConfigAttribute.Markers, serialized)

    def _loadMarkers(self):
        log.debug("Load markers from settings")
        jsonData = Config.valueG(ConfigGroup.MarkingDockWidget, ConfigAttribute.Markers, None)

        if jsonData is None: return [MarkerGroupDto(MarkerCategory.Custom), MarkerGroupDto(MarkerCategory.Stationary)]
        return jsonpickle.decode(jsonData)

    def iterateAll(self, filterFunction:callable = lambda item: isinstance(item, MarkerDto)) -> Union[MarkerDto, MarkerGroupDto]:
        for groupRow in range(self.rowCount(QModelIndex())):
            markerGroupIndex = self.index(groupRow, 0, QModelIndex())
            groupItem = markerGroupIndex.internalPointer()
            if filterFunction(groupItem):
                yield groupItem, markerGroupIndex
            if isinstance(groupItem, MarkerGroupDto):
                for markerRow in range(self.rowCount(markerGroupIndex)):
                    markerRowIndex = self.index(markerRow, 0, markerGroupIndex)
                    markerRowItem = markerRowIndex.internalPointer()
                    if filterFunction(markerRowItem):
                        yield markerRowItem, markerRowIndex

