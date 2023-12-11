import pandas as pd
import re
from typing import Any
from qtpy.QtCore import Signal
from PySide6.QtGui import QPalette, QBrush, QColor
from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel

import UtilFunctions as Util
from dto import TrackDataDTO, MarkerDto, CalcColumnDto
from StatusMessage import StatusMessage
from TrimmerInterval import TrimmerInterval

log = Util.initLogging()

class TrackPointsModel(QAbstractTableModel):
    mainSeriesChanged = Signal()           # when the entire track changed, track without any filters or markers
    mainSeriesLengthChanged = Signal(int)  # when the entire track changes in length (number of items)
    trimRangeChanged = Signal(int)         # when trimming has changed spinners|slider, length|position (length, number of elements)
    contentChanged = Signal()              # content has changed its position ex: sorting

    statusMessage = Signal(StatusMessage)
    workingProgress = Signal(int)

    updateSelection = Signal(int)
    updateTrackPoints = Signal(int)
    markers = pd.DataFrame([], columns=['Indexes', 'Color'])
    trimmerInterval = TrimmerInterval(0, 0)
    allTrackPoints:pd.DataFrame = None
    calculatedColumns: list[CalcColumnDto] = []

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
        self.refreshCalculatedColumns()
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
        if role == Qt.ItemDataRole.BackgroundRole and index.column() == 0:
            lastColor = self.markers[self.markers['Indexes'] == trimmedRow]
            if not lastColor.empty:
                return QBrush(lastColor.apply(lambda row: row[row.last_valid_index()], axis=1).values[0])

        elif role == Qt.ItemDataRole.EditRole:
            val = self.allTrackPoints.iat[trimmedRow, trimmedCol]
            if val is None: val = 0
            return val

        elif role == Qt.ItemDataRole.DisplayRole:
            return self.allTrackPoints.iat[trimmedRow, trimmedCol]

        elif role == Qt.ItemDataRole.ForegroundRole:
            color:QBrush = self.data(index, Qt.ItemDataRole.BackgroundRole)
            if color is None: return
            lum = color.color().lightnessF()
            return QColor('white') if lum < 0.4 else QColor('black')

        return None

    def index(self, row: int, column: int, parent: QModelIndex = ...) -> QModelIndex:
        return self.createIndex(row, column, self.allTrackPoints.iat[row, column])

    def getTrimmedDataItem(self, row: int) -> pd.DataFrame:
        return self.allTrackPoints.iloc[self.trimmerInterval.index(row)]

    def setData(self, index: QModelIndex, value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            self.beginResetModel()
            self.allTrackPoints.iloc[index.row(), index.column()] = value
            self.refreshCalculatedColumns()
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
            colName = str(self.allTrackPoints.columns[section])
            colName = re.sub(r'calc_', ' ', colName)
            return Util.makeItTitle(colName)
        if orientation == Qt.Orientation.Vertical:
            return str(self.allTrackPoints.index[section])
        return super().headerData(section, orientation, role)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        myFlags = super().flags(index)
        if not str(self.allTrackPoints.columns[index.column()]).lower().endswith('calc.'):
            myFlags = myFlags | Qt.ItemFlag.ItemIsEditable
        return myFlags

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

    def addMarker(self, item: MarkerDto):
        log.info(f"Add marker: {item}")
        if self.rowCount() <= 0 or item.indexes == None or len(item.indexes) <= 0: return

        if self.markers.empty:
            self.markers = pd.DataFrame({'Indexes': [index for index in item.indexes], item.id: item.color})
        else:
            newDf = pd.DataFrame({'Indexes': [index for index in item.indexes], item.id: item.color})
            self.markers = pd.merge(self.markers, newDf, on='Indexes', how='outer', sort=True)

        self.markers['Color'] = self.markers.apply(lambda row: row[row.last_valid_index()], axis=1)
        self.markers.sort_values(by=['Indexes'])

        self._refreshAll()
        pass

    def removeMarker(self, item: MarkerDto):
        log.info(f"Remove marker: {item}")
        if self.rowCount() <= 0 or self.markers.empty: return

        self.markers.drop(columns=item.id, inplace=True) # drop marker column
        self.markers.dropna(subset=self.markers.columns[(self.markers.columns != 'Indexes') & (self.markers.columns != 'Color')], how='all', axis=0, inplace=True) # drop indexes which does not have any marker

        if not self.markers.empty:
            self.markers['Color'] = self.markers.apply(lambda row: row[row.last_valid_index()], axis=1)
            self.markers.sort_values(by=['Indexes'])

        self._refreshAll()
        pass

    def changeMarker(self, item: MarkerDto):
        log.info(f"Change marker: {item}")
        if self.rowCount() <= 0 or self.markers.empty or item.indexes == None or len(item.indexes) <= 0: return

        # drop changed column
        self.markers.drop(columns=item.id, inplace=True) # drop marker column
        self.markers.dropna(subset=self.markers.columns[(self.markers.columns != 'Indexes') & (self.markers.columns != 'Color')], how='all', axis=0, inplace=True) # drop indexes which does not have any marker

        # add changed column as a new
        newDf = pd.DataFrame({'Indexes': [index for index in item.indexes], item.id: item.color})
        self.markers = pd.merge(self.markers, newDf, on='Indexes', how='outer', sort=True)

        self.markers['Color'] = self.markers.apply(lambda row: row[row.last_valid_index()], axis=1)
        self.markers.sort_values(by=['Indexes'])

        self._refreshAll()
        pass

    def _refreshAll(self):
        firstIndex = self.index(0,0, QModelIndex())
        lastIndex = self.index(self.rowCount() - 1, self.columnCount() - 1, QModelIndex())
        self.dataChanged.emit(firstIndex, lastIndex, [Qt.ItemDataRole.BackgroundRole])

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

    def getCalcColumnExpression(self, calcCol: CalcColumnDto):
        return eval(f'self.allTrackPoints.assign(calc_{calcCol.name}=lambda row: {calcCol.expression})')

    def refreshCalculatedColumns(self):
        calcColNames = [f'calc_{col.name}' for col in self.calculatedColumns][:]
        existingColNames = [col for col in self.allTrackPoints.columns.tolist() if col.startswith('calc_')][:]

        updateColList = list(set(calcColNames) & set(existingColNames))
        removeColList = list(set(existingColNames) - set(calcColNames))
        addColList = list(set(calcColNames) - set(existingColNames))

        for attribute in addColList:
            found = list(filter(lambda obj: f'calc_{obj.name}' == attribute, self.calculatedColumns))[0]
            self.allTrackPoints = self.getCalcColumnExpression(found)
            pass

        for attribute in updateColList:
            found = list(filter(lambda obj: f'calc_{obj.name}' == attribute, self.calculatedColumns))[0]
            self.allTrackPoints = self.getCalcColumnExpression(found)
            pass

        for attribute in removeColList:
            self.allTrackPoints = self.allTrackPoints.drop(columns = attribute)
            pass

    def updateCalculatedColumns(self, cols: list[CalcColumnDto]):
        self.beginResetModel()
        self.calculatedColumns = cols
        self.refreshCalculatedColumns()
        self.endResetModel()
        pass