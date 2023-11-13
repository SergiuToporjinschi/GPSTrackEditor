import xml.etree.ElementTree as ET
import pytz, re, typing
from datetime import datetime
from typing import List, Any, Union
from qtpy.QtCore import Signal, Slot

from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel, QObject, QPersistentModelIndex

from delegates import DateTimeDelegate, FloatDelegate, ListOfValuesDelegate


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

class TrackPointModel:
    colNames =  ['Time', 'Latitude', 'Longitude', 'Altitude (m)', 'Distance (m)', 'Calculated distance (m)', 'Speed (km/h)', 'Calculated speed (km/h)', 'Hart rate (bpm)', 'Sensor state']
    colInfo = {
            'time': (datetime, DateTimeDelegate('dd-MM-yyyy HH:mm:ss.z t','%d-%m-%Y %H:%M:%S.%f %Z')),
            'latitude': (float, FloatDelegate(-90, 90, 8)),
            'longitude': (float, FloatDelegate(-180, 180, 8)),
            'altitude': (float, FloatDelegate(-200, 9000, 3)),
            'distance': (float, FloatDelegate(-20000, 20000, 16)),
            'calculatedDistance': (float, FloatDelegate(-20000, 20000, 16)),
            'speed': (float, FloatDelegate(0, 1000, 12)),
            'calculatedSpeed': (float, FloatDelegate(0, 1000, 12)),
            'hartRate': (int, FloatDelegate(0, 250, 0)),
            'sensorState': (str, ListOfValuesDelegate(('Present', 'Present'), ('Absent','Absent')))
        }
    def __init__(self, time: datetime, latitude: float, longitude:float, altitude:float, hartRate: int, distance: float, speed: float, sensorState: str=None, calculatedDistance:float=None, calculatedSpeed: float=None) -> None:
        self.data = {
            'time': time,
            'latitude': latitude,
            'longitude': longitude,
            'altitude': altitude,
            'distance': distance,
            'calculatedDistance': calculatedDistance,
            'speed': speed,
            'calculatedSpeed': calculatedSpeed,
            'hartRate': hartRate,
            'sensorState': sensorState
        }
        pass



    def getValueByColumnIndex(self, index: int):
        return self.getValueByColumnName(TrackPointModel.indexToName(index))

    def getValueByColumnName(self, colName: str):
        return self.data[colName]

    def setValue(self, col:str|int, value: Any):
        if isinstance(col, int):
            col = TrackPointModel.indexToName(col)
        self.data[col] = self._checkValueType(col, value)
        pass

    def _checkValueType(self, col: str, value: Any):
        colType, _ = TrackPointModel.colInfo[col]
        if isinstance(value, int) and colType == float:
            value = float(value)
        if isinstance(value, float) and colType == int:
            value = int(value)
        if not isinstance(value, colType):
            raise ValueError(f'The {col} should be {colType}')
        return value

    @staticmethod
    def getNoOfColumns():
        return len(TrackPointModel.colInfo)

    @staticmethod
    def getColDelegate(index: int):
        _, delegate = TrackPointModel.colInfo[TrackPointModel.indexToName(index)]
        return delegate

    @staticmethod
    def indexToName(index: int):
        return list(TrackPointModel.colInfo.keys())[index]

    @staticmethod
    def nameToIndex(colName: str):
        index = 0
        for key in TrackPointModel.colInfo:
            if key == colName:
                return index
            index += 1
        return -1



class TrackPointsModel(QAbstractTableModel):
    mainSeriesChanged = Signal() # when the entire track (without any filters or markers) changed
    mainSeriesLengthChanged = Signal(int) # when the entire track changes the number of items
    trimRangeChange = Signal()
    # markingChange = Signal()
    contentChanged = Signal()

    rowCountChanged = Signal(int)
    allTrackPointsCountChanged = Signal(int)
    statusMessage = Signal(str)
    workingProgress = Signal(int)

    filterRange = None
    trackPoints = []
    allTrackPoints = []
    markers: [Marker] = []
    _lastFindDataExpression = None
    def __init__(self, trackPoints: List[TrackPointModel] = None, palette: QPalette=None ) -> None:
        super(TrackPointsModel, self).__init__()
        self.allTrackPoints = trackPoints or []
        self.trackPoints = self.allTrackPoints
        self.palette = palette
        self.mainSeriesLengthChanged.emit(len(self.allTrackPoints))
        self.rowsMoved.connect(self._test)
        self.rowsInserted.connect(self._test)
    def _test(Self, index:QModelIndex, a: int, b:int, c: QModelIndex, d:int):
        pass
    def loadData(self, trackPoints: List[TrackPointModel]):
        self.beginResetModel()
        self.allTrackPoints.clear()
        self.allTrackPoints.extend(trackPoints)
        self.trackPoints = self.allTrackPoints
        # self.rowCountChanged.emit(len(self.allTrackPoints))
        # self.allTrackPointsCountChanged.emit(len(self.allTrackPoints))
        self.mainSeriesChanged.emit()
        self.mainSeriesLengthChanged.emit(len(self.allTrackPoints))
        self.endResetModel()

    def clearData(self):
        self.beginResetModel()
        self.allTrackPoints.clear()
        self.trackPoints = self.allTrackPoints
        # self.rowCountChanged.emit(len(self.allTrackPoints))
        # self.allTrackPointsCountChanged.emit(0)
        self.mainSeriesChanged.emit()
        self.mainSeriesLengthChanged.emit(len(self.allTrackPoints))
        self.endResetModel()

    def indexByColName(self, row: int, column: str, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> QModelIndex:
        return self.index(row, TrackPointModel.nameToIndex('calculatedSpeed'))

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            return self.trackPoints[index.row()].getValueByColumnIndex(index.column())
        if role == Qt.ItemDataRole.EditRole:
            return self.trackPoints[index.row()].getValueByColumnIndex(index.column())
        if role == Qt.ItemDataRole.BackgroundRole and len(self.markers) > 0:
            selectedColor = None
            for marker in self.markers:
                if index.row() in marker.indexes:
                    selectedColor = marker.color
            if selectedColor is not None: return selectedColor

    def dataByColNames(self, row: int, colNames: [str], role: typing.Optional[int] = Qt.ItemDataRole.EditRole) -> Any:
        response = ()
        for colName in colNames:
            response += (self.data(self.index(row, TrackPointModel.nameToIndex(colName)), role), )
        return response

    def dataByColName(self, row: int, colName: str, role: typing.Optional[int] = Qt.ItemDataRole.EditRole) -> Any:
        return self.data(self.index(row, TrackPointModel.nameToIndex(colName)), role)

    def dataByIndex(self, row: int, col: int, role: typing.Optional[int] = Qt.ItemDataRole.EditRole) -> Any:
        return self.data(self.index(row, col), role), TrackPointModel.indexToName(col)

    def setData(self, index: QModelIndex, value: Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            self.trackPoints[index.row()].setValue(index.column(), value)
            return True
        return super().setData(index, value, role)

    def setDataByColumnName(self, row: int, colName: str, value: Any, role: typing.Optional[int] = Qt.ItemDataRole.EditRole) -> bool:
        return self.setData(self.indexByColName(row, colName), value, role)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.trackPoints)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return TrackPointModel.getNoOfColumns()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return TrackPointModel.colNames[section]
        return super().headerData(section, orientation, role)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        return super().flags(index) | Qt.ItemFlag.ItemIsEditable

    def sortBy(self, column:str, order: Qt.SortOrder = ...):
        self.beginResetModel()
        def key_function(item):
            val = item.data[column]
            return val if val is not None else 0

        self.trackPoints.sort(key=key_function, reverse=order == Qt.SortOrder.DescendingOrder)
        self.contentChanged.emit()
        # if self._lastFindDataExpression is not None: self.findByExpression(self._lastFindDataExpression)
        self.endResetModel()

    def sort(self, column:int, order: Qt.SortOrder = ...):
        self.sortBy(TrackPointModel.indexToName(column), order)
        # if self._lastFindDataExpression is not None: self.findByExpression(self._lastFindDataExpression)

    def trimRows(self, interval: tuple = None):
        self.beginResetModel()
        min, max = interval
        self.trackPoints = [i for index, i in enumerate(self.allTrackPoints) if index in range(min-1,max)]
        self.trimRangeChange.emit()
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

class TCXLoader(QObject):
    workingProgress = Signal(int)
    fileDataChanged = Signal(dict)
    def __init__(self, file_path = None):
        super().__init__()
        self.data = {
            'activity': {
                'file': file_path,
                'lapsCount': None,
                'trackPointsCount': None,
                'type': None,
                'id': None,
                'notes': None,
                'start_time': None
            },
            'laps': [],
            'trackpoints': [],
        }
        self.fileDataChanged.emit(self.data['activity'])

    def load_tcx_file(self, file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            # Extract activity information
            activity = root.find(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Activity")
            self.data['activity']['file'] = file_path
            self.data['activity']['type'] = activity.attrib['Sport']
            self.data['activity']['id'] = activity.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Id").text
            self.data['activity']['notes'] = self._getNotes(activity)
            # self.data['calories'] = lap.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Calories").text
            # Extract lap data
            laps = root.findall(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Lap")
            for index, lap in enumerate(laps):
                lap_data = {
                    'start_time': datetime.strptime(lap.get("StartTime"), "%Y-%m-%dT%H:%M:%S.%fZ"),
                    'total_time': float(lap.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}TotalTimeSeconds").text),
                    'average_hart_rate' : self._getAverageHartRate(lap),
                    'distance_meters': self._getDistance(lap),
                    'trigger_method': self._getTriggerMethod(lap),
                    'max_hart_rate': self._getMaxHartRate(lap),
                    'max_speed': self._getMaxSpeed(lap),
                    'intensity': self._getIntensity(lap),
                    'calories': self._getCalories(lap),
                    # Add more lap data as needed
                }
                self.data['laps'].append(lap_data)
                self.workingProgress.emit(int((index + 1) * 25 / len(laps)))
            self.data['activity']['lapsCount'] = len(self.data['laps'])

            # Extract trackpoint data (GPS data, heart rate, etc.)
            trackpoints = root.findall(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Trackpoint")
            for index, trackpoint in enumerate(trackpoints):
                time = self._getDateTimeUTC(trackpoint)
                latitude = self._getLatitude(trackpoint)
                longitude = self._getLongitude(trackpoint)
                altitude = self._getAltitude(trackpoint)
                heart_rate = self._getHartRate(trackpoint)
                distance = self._getDistance(trackpoint)
                speed =  self._getSpeedExtension(trackpoint)
                sensorState = self._getSensorState(trackpoint)
                self.data['trackpoints'].append(TrackPointModel(time, latitude, longitude, altitude, heart_rate, distance, speed, sensorState))
                self.workingProgress.emit(int(25 + (index + 1) * 75 / len(trackpoints)))
            self.data['activity']['start_time'] = self.data['trackpoints'][0].getValueByColumnName('time')
            self.data['activity']['trackPointsCount'] = len(self.data['trackpoints'])
            self.fileDataChanged.emit(self.data['activity'])
        except ET.ParseError as e:
            print(f"Error parsing TCX file: {e}")

    def getTrackPoints(self):
        return self.data['trackpoints']

    def getLaps(self):
        return self.data['laps']

    def getType(self):
        return self.data['activity']['type']

    def getId(self):
        return self.data['activity']['id']

    def getNotes(self):
        return self.data['activity']['notes']

    def getStartTime(self):
        return self.data['activity']['start_time']

    def _getDateTimeUTC(self, node):
        strVal = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Time")
        if strVal.text is None: return None
        dt = datetime.strptime(strVal.text[:-1] + ' UTC', "%Y-%m-%dT%H:%M:%S.%f %Z")
        dt = dt.replace(tzinfo=pytz.UTC)
        return dt

    def _getLatitude(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Position/{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}LatitudeDegrees")
        return  float(value.text) if value is not None else None

    def _getLongitude(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Position/{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}LongitudeDegrees")
        return  float(value.text) if value is not None else None

    def _getNotes(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Notes")
        return value.text if value is not None else None

    def _getAverageHartRate(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}AverageHeartRateBpm/{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Value")
        return int(value.text) if value is not None else None

    def _getTriggerMethod(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}TriggerMethod")
        return value.text if value is not None else None

    def _getMaxSpeed(self,node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}MaximumSpeed")
        return float(value.text) if value is not None else None

    def _getMaxHartRate(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}MaximumHeartRateBpm/{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Value")
        return int(value.text) if value is not None else None

    def _getIntensity(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Intensity")
        return value.text if value is not None else None

    def _getCalories(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Calories")
        return int(value.text) if value is not None else None

    def _getAltitude(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}AltitudeMeters")
        return float(value.text) if value is not None else None

    def _getHartRate(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}HeartRateBpm/{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Value")
        return int(value.text) if value is not None else None

    def _getDistance(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}DistanceMeters")
        return float(value.text) if value is not None else None

    def _getSpeedExtension(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Extensions/{http://www.garmin.com/xmlschemas/ActivityExtension/v2}TPX/{http://www.garmin.com/xmlschemas/ActivityExtension/v2}Speed")
        return float(value.text) if value is not None else None

    def _getSensorState(self, node):
        value = node.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}SensorState")
        return value.text if value is not None else None



