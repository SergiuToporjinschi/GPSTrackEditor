import UtilFunctions as Util
import pandas as pd
from datetime import datetime
from typing import Any, Type, Generator, Union
from qtpy.QtCore import Signal
from StatusMessage import StatusMessage

from PySide6.QtGui import QPalette, QBrush, QColor
from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel
from PySide6.QtWidgets import QStyledItemDelegate

from TrimmerInterval import TrimmerInterval
from delegates import DateTimeDelegate, FloatDelegate, ListOfValuesDelegate, IntDelegate
from dto import TrackDataDTO, MarkerDto


class TrackPointsModel(QAbstractTableModel):
    mainSeriesChanged = Signal()           # when the entire track changed, track without any filters or markers
    mainSeriesLengthChanged = Signal(int)  # when the entire track changes in length (number of items)
    trimRangeChanged = Signal(int)         # when trimming has changed spinners|slider, length|position (length, number of elements)
    contentChanged = Signal()              # content has changed its position ex: sorting

    statusMessage = Signal(StatusMessage)
    workingProgress = Signal(int)

    updateSelection = Signal(int)
    updateTrackPoints = Signal(int)

    markers: list[MarkerDto] = []
    trimmerInterval = TrimmerInterval(0, 0)
    allTrackPoints:pd.DataFrame = None

    def __init__(self, palette: QPalette=None ) -> None:
        super(TrackPointsModel, self).__init__()
        self.allTrackPoints = self._getEmptyDataFrame()
        self.trimmerInterval.max = len(self.allTrackPoints)
        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)
        self.palette = palette

    def loadData(self, trackPoints: list[TrackDataDTO]):
        self.beginResetModel()

        objList = [(obj.time,
                obj.latitude,
                obj.longitude,
                obj.altitude,
                obj.hartRate,
                obj.distance,
                obj.speed,
                obj.sensorState) for obj in trackPoints][:]

        cols = Util.getClassPublicAttributes(TrackDataDTO)
        self.allTrackPoints = self._removeNan(pd.DataFrame(objList, columns=cols))

        self.trimmerInterval.max = len(self.allTrackPoints.index)
        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)
        self.endResetModel()
        self.mainSeriesChanged.emit()

    def _getEmptyDataFrame(self):
        cols = Util.getClassPublicAttributes(TrackDataDTO)
        return pd.DataFrame(columns=cols)

    def clearData(self):
        self.beginResetModel()
        self.allTrackPoints = self._getEmptyDataFrame()
        self.trimmerInterval.max = 0
        self.mainSeriesLengthChanged.emit(self.trimmerInterval.max)
        self.endResetModel()
        self.mainSeriesChanged.emit()

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        trimmedRow = self.trimmerInterval.index(index.row())
        trimmedCol = index.column()
        if role == Qt.ItemDataRole.EditRole:
            val = self.allTrackPoints.iat[trimmedRow, trimmedCol]
            if val is None: val = 0
            return val

        elif role == Qt.ItemDataRole.DisplayRole:
            return self.allTrackPoints.iat[trimmedRow, trimmedCol]

        elif role == Qt.ItemDataRole.BackgroundRole and len(self.markers) > 0:
            selectedColor = None
            for marker in self.markers:
                if marker.indexes is not None and trimmedRow in marker.indexes:
                    selectedColor = marker.color
            if selectedColor is not None: return QBrush(selectedColor)

        elif role == Qt.ItemDataRole.ForegroundRole:
            color:QBrush = self.data(index, Qt.ItemDataRole.BackgroundRole)
            if color is None: return
            lum = color.color().lightnessF()
            return QColor('white') if lum < 0.4 else QColor('black')

    def index(self, row: int, column: int, parent: QModelIndex = ...) -> QModelIndex:
        return self.createIndex(row, column, self.allTrackPoints.iat[row, column])

    def getTrimmedDataItem(self, row: int) -> pd.DataFrame:
        return self.allTrackPoints.iloc[self.trimmerInterval.index(row)]

    def setData(self, index: QModelIndex, value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            self.beginResetModel()
            self.allTrackPoints.iloc[index.row(), index.column()] = value
            self.endResetModel()
            return True
        return False # super().setData(index, value, role)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.trimmerInterval)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.allTrackPoints.columns)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role != Qt.ItemDataRole.DisplayRole: return None
        if orientation == Qt.Orientation.Horizontal:
            return Util.makeItTitle(str(self.allTrackPoints.columns[section]))
        if orientation == Qt.Orientation.Vertical:
            return str(self.allTrackPoints.index[section])
        return super().headerData(section, orientation, role)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        return super().flags(index) | Qt.ItemFlag.ItemIsEditable

    def sortBy(self, column:str, order: Qt.SortOrder = ...):
        return

    def sort(self, column:int, order: Qt.SortOrder = ...):
        self.beginResetModel()

        colName = self.allTrackPoints.columns[column]
        self.allTrackPoints = self.allTrackPoints.sort_values(by=colName, ascending=order == Qt.SortOrder.AscendingOrder)

        self.contentChanged.emit()
        self.endResetModel()

    def trimRows(self, interval: tuple = None):
        self.beginResetModel()
        self.trimmerInterval.val = interval
        self.trimRangeChanged.emit(len(self.trimmerInterval)) # TODO add the number of rows
        self.endResetModel()

    def markerActivated(self, marker: MarkerDto, active: bool):
        foundIndex = self.markers.index(marker) if marker in self.markers else None

        if active and foundIndex is None:
            self.beginResetModel()
            self.markers.append(marker)
            self.endResetModel()

        elif not active and foundIndex is not None:
            self.beginResetModel()
            del self.markers[foundIndex]
            self.endResetModel()

    def _removeNan(self, df:pd.DataFrame) -> pd.DataFrame:
        for key in ['distance', 'longitude', 'latitude', 'altitude', 'hartRate', 'speed']:
            if not df[key].isnull().all():
                if pd.isna(df[key].iloc[0]):
                    first_valid_index = df[key].first_valid_index()
                    df.loc[:1, key] = df.loc[:1, key].fillna(df[key].iloc[first_valid_index])
                    df.loc[1:, key] = df.loc[1:, key].ffill()
                else:
                    df[key] = df[key].ffill()
        return df