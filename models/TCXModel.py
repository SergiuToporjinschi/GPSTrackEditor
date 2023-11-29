from datetime import datetime
from typing import Any, Type, Generator
from qtpy.QtCore import Signal
from StatusMessage import StatusMessage

from PySide6.QtGui import QPalette
from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel
from PySide6.QtWidgets import QStyledItemDelegate

from TrimmerInterval import TrimmerInterval
from delegates import DateTimeDelegate, FloatDelegate, ListOfValuesDelegate
from dto import TrackDataDTO, MarkerDto


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


class TCXRowModel(TrackDataDTO):
    def __init__(self, row: TrackDataDTO) -> None:
        for name in vars(TrackDataDTO):
            if isinstance(getattr(TrackDataDTO, name), property):
                setattr(self, name, getattr(row, name))

    def __getitem__(self, index):
        return getattr(self, TCXColModel()[index].dtoAttribute)

    def getValueByColName(self, colName):
        # [maker for maker in self.markers if maker.name != name]
        col = [colModel for colModel in TCXColModel() if colModel.dtoAttribute == colName]
        if col is None:
            raise Exception('Column does not exists!')
        return getattr(self, colName)

class TrackPointsModel(QAbstractTableModel):
    mainSeriesChanged = Signal()           # when the entire track changed, track without any filters or markers
    mainSeriesLengthChanged = Signal(int)  # when the entire track changes in length (number of items)
    trimRangeChanged = Signal(int)         # when trimming has changed spinners|slider, length|position (length, number of elements)
    contentChanged = Signal()              # content has changed its position ex: sorting

    statusMessage = Signal(StatusMessage)
    workingProgress = Signal(int)

    updateSelection = Signal(int)          # signal emited
    updateTrackPoints = Signal(int)

    markers: list[MarkerDto] = []
    trimmerInterval = TrimmerInterval(1, 1)
    allTrackPoints = list[TCXRowModel]

    def __init__(self, trackPoints: list[TCXRowModel] = None, palette: QPalette=None ) -> None:
        super(TrackPointsModel, self).__init__()
        self.allTrackPoints = trackPoints or []
        self.palette = palette
        self.trimmerInterval.max = len(self.allTrackPoints)
        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)

    def loadData(self, trackPoints: list[TrackDataDTO]):
        self.beginResetModel()
        self.allTrackPoints.clear()
        self.allTrackPoints.extend(self._decorateData(trackPoints))
        self.trimmerInterval.max = len(self.allTrackPoints)
        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)
        self.endResetModel()
        self.mainSeriesChanged.emit()

    def _decorateData(self, data: list [TrackDataDTO]) -> list[TCXRowModel]:
        return  [TCXRowModel(item) for item in data][:]

    def clearData(self):
        self.beginResetModel()
        self.allTrackPoints.clear()
        self.trimmerInterval.max = 0
        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)
        self.endResetModel()
        self.mainSeriesChanged.emit()

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return self.allTrackPoints[self.trimmerInterval.index(index.row())][index.column()]
        if role == Qt.ItemDataRole.BackgroundRole and len(self.markers) > 0:
            selectedColor = None
            for marker in self.markers:
                if self.trimmerInterval.index(index.row()) in marker.indexes:
                    selectedColor = marker.color
            if selectedColor is not None: return selectedColor

    def getTrimmedDataItem(self, row: int) -> TCXRowModel:
        return self.allTrackPoints[self.trimmerInterval.index(row)]

    def iterateTrimmedTracks(self) -> Generator[TCXRowModel, None, None]:
        for index in range(0, self.rowCount()):
            yield self.allTrackPoints[self.trimmerInterval.index(index)]

    def iterateAllTracks(self) -> Generator[TCXRowModel, None, None]:
        for item in self.allTrackPoints:
            yield item

    def setData(self, index: QModelIndex, value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            self.allTrackPoints[self.trimmerInterval.index(index.row())].setValue(index.column(), value)
            return True
        return super().setData(index, value, role)

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
        self.trimRangeChanged.emit(len(self.trimmerInterval)) # TODO add the number of rows
        self.endResetModel()

    def addMarker(self, maker: MarkerDto):
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
