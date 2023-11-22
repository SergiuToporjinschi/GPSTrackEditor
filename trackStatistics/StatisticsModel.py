from typing import Any, Generator
from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel, QPersistentModelIndex, Qt, QObject

from .StatisticsDto import StatisticsDto

class StatisticsModel(QAbstractTableModel):
    _lines: list[StatisticsDto] = []
    _headers: list[str] = ['Min', 'Avg','Max', 'Missing']

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(None)
        self._lines = [
            StatisticsDto('latitude', float, 'Latitude'),
            StatisticsDto('longitude', float, 'Longitude'),
            StatisticsDto('altitude', float, 'Altitude'),
            StatisticsDto('hartRate', int, 'Hart rate'),
            StatisticsDto('distance', float, 'Distance km'),
            StatisticsDto(None, float, 'Distance m', 'func'),
            StatisticsDto('calculatedDistance', float, 'Calculated distance km'),
            StatisticsDto(None, float, 'Calculated distance m', 'func'),
            StatisticsDto('speed', float, 'Speed km/h'),
            StatisticsDto(None, float, 'Speed m/h', 'func'),
            StatisticsDto('calculatedSpeed', float, 'Calculated speed km/h'),
            StatisticsDto(None, float, 'Calculated speed m/h', 'func'),
            StatisticsDto('sensorState', str, 'Sensor state')
        ]

    def func(self, a:float, b:float) -> float:
        return a + b
        pass

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._headers)

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._lines)

    def iterateIndexes(self) -> Generator[StatisticsDto, None, None]:
        for item in self._lines:
            yield item

    def data(self, index, role= Qt.ItemDataRole):
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None
        attr = self._headers[index.column()].lower()
        return getattr(self._lines[index.row()], attr)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        if orientation == Qt.Orientation.Vertical:
            return self._lines[section]._title