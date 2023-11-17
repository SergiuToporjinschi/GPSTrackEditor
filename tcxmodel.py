import typing
from datetime import datetime
from typing import Any, Union, Type
import types
from qtpy.QtCore import Signal
from statusBar import StatusMessage

from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel, QPersistentModelIndex

from TrimmerInterval import TrimmerInterval
from delegates import DateTimeDelegate, FloatDelegate, ListOfValuesDelegate
from TrackDataDTO import TrackDataDTO
from PySide6.QtWidgets import QStyleOptionViewItem, QStyledItemDelegate, QWidget

class Marker:
    _name: str = None
    _indexes: [int] = None
    _color: [QColor] = None
    _expression: str = None
    def __init__(self, name: str, indexes:[int], color:QColor, expression: typing.Optional[str] = None) -> None:
        self._name = name
        self._indexes = indexes
        self._color = color
        self._expression = expression
        pass

    @property
    def name(self):
        return self._name

    @property
    def indexes(self):
        return self._indexes

    @indexes.setter
    def indexes(self, indexes: []):
        self._indexes = indexes

    @property
    def color(self):
        return self._color

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, expression: str):
        self._expression = expression

    def __eq__(self, other):
        # Customize the equality comparison based on your requirements
        if isinstance(other, Marker):
            return self.name == other.name
        return False

class TCXColInfoModel:
    columnTitle: str = None
    dataType: Type = None
    delegate: QStyledItemDelegate = None
    dtoAttribute: str = None

    def __init__(self, dtoAttribute: str, colTile: str, dataType: Type, cellDelegate: QStyledItemDelegate) -> None:
        self.columnTitle = colTile
        self.dataType = dataType
        self.delegate = cellDelegate
        self.dtoAttribute = dtoAttribute



class TCXColModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._buildModel()
        return cls._instance

    def _buildModel(self) -> None:
        self._colInfo: list[TCXColInfoModel] = []
        self._colInfo.append(TCXColInfoModel('time', 'Time', datetime, DateTimeDelegate('dd-MM-yyyy HH:mm:ss.z t','%d-%m-%Y %H:%M:%S.%f %Z')))
        self._colInfo.append(TCXColInfoModel('latitude', 'Latitude', float, FloatDelegate(-90, 90, 8)))
        self._colInfo.append(TCXColInfoModel('longitude', 'Longitude', float, FloatDelegate(-180, 180, 8)))
        self._colInfo.append(TCXColInfoModel('altitude', 'Altitude (m)', float, FloatDelegate(-200, 9000, 3)))
        self._colInfo.append(TCXColInfoModel('distance', 'Distance (m)', float, FloatDelegate(-20000, 20000, 16)))
        self._colInfo.append(TCXColInfoModel('calculatedDistance', 'Calculated distance (m)', float, FloatDelegate(-20000, 20000, 16)))
        self._colInfo.append(TCXColInfoModel('speed', 'Speed (km/h)', float, FloatDelegate(0, 1000, 12)))
        self._colInfo.append(TCXColInfoModel('calculatedSpeed', 'Calculated speed (km/h)', float, FloatDelegate(0, 1000, 12)))
        self._colInfo.append(TCXColInfoModel('hartRate', 'Hart rate (bpm)', int, FloatDelegate(0, 250, 0)))
        self._colInfo.append(TCXColInfoModel('sensorState', 'Sensor state', str, ListOfValuesDelegate(('Present', 'Present'), ('Absent','Absent'))))
        pass

    def getIndexOfColumnName(self, colName: str):
        model = TCXColModel()
        for index in range(0, len(model)):
            if model[index].dtoAttribute == colName:
                return index
        return None

    def __getitem__(self, index):
        return self._colInfo[index]

    def __len__(self):
        return len(self._colInfo)


class TCXRowModel:
    def __init__(self, row: TrackDataDTO) -> None:
        self.rowData = row

    def __getitem__(self, index):
        colName = TCXColModel()[index].dtoAttribute
        return getattr(self.rowData, colName)

    def getValueByColName(self, colName):
        # [maker for maker in self.markers if maker.name != name]
        col = [colModel for colModel in TCXColModel() if colModel.dtoAttribute == colName]
        if col is None:
            raise Exception('Column does not exists!')
        return getattr(self.rowData, colName)

# class TrackPointModel:
#     colNames =  ['Time', 'Latitude', 'Longitude', 'Altitude (m)', 'Distance (m)', 'Calculated distance (m)', 'Speed (km/h)', 'Calculated speed (km/h)', 'Hart rate (bpm)', 'Sensor state']
#     colInfo = {
#             'time': (datetime, DateTimeDelegate('dd-MM-yyyy HH:mm:ss.z t','%d-%m-%Y %H:%M:%S.%f %Z')),
#             'latitude': (float, FloatDelegate(-90, 90, 8)),
#             'longitude': (float, FloatDelegate(-180, 180, 8)),
#             'altitude': (float, FloatDelegate(-200, 9000, 3)),
#             'distance': (float, FloatDelegate(-20000, 20000, 16)),
#             'calculatedDistance': (float, FloatDelegate(-20000, 20000, 16)),
#             'speed': (float, FloatDelegate(0, 1000, 12)),
#             'calculatedSpeed': (float, FloatDelegate(0, 1000, 12)),
#             'hartRate': (int, FloatDelegate(0, 250, 0)),
#             'sensorState': (str, ListOfValuesDelegate(('Present', 'Present'), ('Absent','Absent')))
#         }
#     def __init__(self, time: datetime, latitude: float, longitude:float, altitude:float, hartRate: int, distance: float, speed: float, sensorState: str=None, calculatedDistance:float=None, calculatedSpeed: float=None) -> None:
#         self.data = {
#             'time': time,
#             'latitude': latitude,
#             'longitude': longitude,
#             'altitude': altitude,
#             'distance': distance,
#             'calculatedDistance': calculatedDistance,
#             'speed': speed,
#             'calculatedSpeed': calculatedSpeed,
#             'hartRate': hartRate,
#             'sensorState': sensorState
#         }
#         pass

#     def getValueByColumnIndex(self, index: int):
#         return self.getValueByColumnName(TrackPointModel.indexToName(index))

#     def getValueByColumnName(self, colName: str):
#         return self.data[colName]

#     def setValue(self, col:str|int, value: Any):
#         if isinstance(col, int):
#             col = TrackPointModel.indexToName(col)
#         self.data[col] = self._checkValueType(col, value)
#         pass

#     def _checkValueType(self, col: str, value: Any):
#         colType, _ = TrackPointModel.colInfo[col]
#         if isinstance(value, int) and colType == float:
#             value = float(value)
#         if isinstance(value, float) and colType == int:
#             value = int(value)
#         if not isinstance(value, colType):
#             raise ValueError(f'The {col} should be {colType}')
#         return value

#     @staticmethod
#     def getNoOfColumns():
#         return len(TrackPointModel.colInfo)

#     @staticmethod
#     def getColDelegate(index: int):
#         _, delegate = TrackPointModel.colInfo[TrackPointModel.indexToName(index)]
#         return delegate

#     @staticmethod
#     def indexToName(index: int):
#         return list(TrackPointModel.colInfo.keys())[index]

#     @staticmethod
#     def nameToIndex(colName: str):
#         index = 0
#         for key in TrackPointModel.colInfo:
#             if key == colName:
#                 return index
#             index += 1
#         return -1



class TrackPointsModel(QAbstractTableModel):
    mainSeriesChanged = Signal()           # when the entire track changed, track without any filters or markers
    mainSeriesLengthChanged = Signal(int)  # when the entire track changes in length (number of items)
    trimRangeChanged = Signal(int)          # when trimming has changed spinners|slider, length|position (length, number of elements)
    contentChanged = Signal()              # content has changed its position ex: sorting
    markers: [Marker] = []

    statusMessage = Signal(StatusMessage)
    workingProgress = Signal(int)

    updateSelection = Signal(int)          # signal emited
    updateTrackPoints = Signal(int)
    trimmerInterval = TrimmerInterval(1, 1)

    allTrackPoints = list[TCXRowModel]

    def __init__(self, trackPoints: list[TCXRowModel] = None, palette: QPalette=None ) -> None:
        super(TrackPointsModel, self).__init__()
        self.allTrackPoints = trackPoints or []
        # self.trackPoints = self.allTrackPoints
        self.palette = palette
        self.trimmerInterval.max = len(self.allTrackPoints)
        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)

    def loadData(self, trackPoints: list[TrackDataDTO]):
        self.beginResetModel()
        self.allTrackPoints.clear()
        self.allTrackPoints.extend(self._decorateData(trackPoints))
        # self.trackPoints = self.allTrackPoints
        self.trimmerInterval.max = len(self.allTrackPoints)
        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)

        # self.mainSeriesLengthChanged.emit(len(self.allTrackPoints))

        # self.trimerInterval.min = 1
        # self.trimerInterval.max = len(self.allTrackPoints)
        # self.rowCountChanged.emit(len(self.allTrackPoints))
        # self.allTrackPointsCountChanged.emit(len(self.allTrackPoints))
        self.mainSeriesChanged.emit()
        self.endResetModel()

    def _decorateData(self, data: list [TrackDataDTO]) -> list[TCXRowModel]:
        return  [TCXRowModel(item) for item in data][:]

    def clearData(self):
        self.beginResetModel()
        self.allTrackPoints.clear()

        self.trimmerInterval.max = 0

        # self.rowCountChanged.emit(len(self.allTrackPoints))
        # self.allTrackPointsCountChanged.emit(0)
        self.mainSeriesChanged.emit()

        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)
        # self.mainSeriesLengthChanged.emit(len(self.allTrackPoints))
        self.endResetModel()

    def indexByColName(self, row: int, column: str, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> QModelIndex:
        return self.index(row, TCXColModel().getIndexOfColumnName(column))

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return self.allTrackPoints[self.trimmerInterval.index(index.row())][index.column()]
        if role == Qt.ItemDataRole.BackgroundRole and len(self.markers) > 0:
            selectedColor = None
            for marker in self.markers:
                if self.trimmerInterval.index(index.row()) in marker.indexes:
                    selectedColor = marker.color
            if selectedColor is not None: return selectedColor

    def dataByColNames(self, row: int, colNames: [str]) -> Any:
        response = ()
        for colName in colNames:
            response += (self.allTrackPoints[row].getValueByColName(colName), )
        return response

    def dataByColName(self, row: int, colName: str, role: typing.Optional[int] = Qt.ItemDataRole.EditRole) -> Any:
        return self.data(self.index(row, TCXColModel().getIndexOfColumnName(colName)), role)

    def dataAndAttributeByIndex(self, row: int, col: int, role: typing.Optional[int] = Qt.ItemDataRole.EditRole) -> Any:
        return self.data(self.index(row, col), role), TCXColModel()[col].dtoAttribute

    def setData(self, index: QModelIndex, value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            self.allTrackPoints[self.trimmerInterval.index(index.row())].setValue(index.column(), value)
            return True
        return super().setData(index, value, role)

    def setDataByColumnName(self, row: int, colName: str, value: Any, role: typing.Optional[int] = Qt.ItemDataRole.EditRole) -> bool:
        return self.setData(self.indexByColName(row, colName), value, role)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.trimmerInterval)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(TCXColModel())

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return TCXColModel()[section].columnTitle
        return super().headerData(section, orientation, role)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        return super().flags(index) | Qt.ItemFlag.ItemIsEditable

    def sortBy(self, column:str, order: Qt.SortOrder = ...):
        self.beginResetModel()
        def key_function(item:TCXRowModel):
            val = item.getValueByColName(column)
            return val if val is not None else 0

        self.allTrackPoints.sort(key=key_function, reverse=order == Qt.SortOrder.DescendingOrder)
        self.contentChanged.emit()
        self.endResetModel()

    def sort(self, column:int, order: Qt.SortOrder = ...):
        self.sortBy(TCXColModel()[column].dtoAttribute, order)

    def trimRows(self, interval: tuple = None):
        self.beginResetModel()
        self.trimmerInterval.val = interval
        # self.trackPoints = [i for index, i in enumerate(self.allTrackPoints) if index in range(min-1, max)]
        self.trimRangeChanged.emit(1) # TODO add the number of rows
        self.endResetModel()

    def addMarker(self, maker: Marker):
        self.beginResetModel()
        self.markers.append(maker)
        self.endResetModel()
        pass

    def clearAllMarker(self):
        self.beginResetModel()
        self.markers = []
        self.endResetModel()

    def clearMarker(self, name: str):
        self.beginResetModel()
        self.markers[:] = [maker for maker in self.markers if maker.name != name]
        self.endResetModel()
        pass
