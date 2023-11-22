import xml.etree.ElementTree as ET
import pytz
from datetime import datetime

from qtpy.QtCore import Signal
from PySide6.QtCore import QObject

from TrackDataDTO import FileDataDTO, LapDataDTO, TrackDataDTO
from StatusMessage import StatusMessage
from abstracts import AbstractNotificationWidget
from ThreadExecutor import AsyncExecutor, AsyncManager

class TCXLoader(AbstractNotificationWidget, AsyncManager, QObject):
    fileDataChanged = Signal(FileDataDTO)
    trackPointsChanged = Signal(list)

    _threads: list[AsyncExecutor] = []
    def __init__(self, fileName: str = None):
        super().__init__()
        self.fileName = fileName

    def loadTCXAsync(self, fileName:str):
        val = self._executeOnThread(self._loadTCXFile, (fileName))
        self.statusMessage.emit(val.value)

    def _loadTCXFile(self, file_path):
        try:
            dto = FileDataDTO()
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Extract activity information
            activity = root.find(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Activity")
            dto.filePath = file_path
            dto.activityType = activity.attrib['Sport']
            dto.id = activity.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Id").text
            dto.notes = self._getNotes(activity)
            self.statusMessage.emit(StatusMessage('Parsing schema...'))

            # Extract lap data
            laps = root.findall(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Lap")
            self.statusMessage.emit(StatusMessage('Loading laps'))
            lapCount = len(laps)
            for index, lap in enumerate(laps):
                lapDto = LapDataDTO()
                lapDto.startTime = datetime.strptime(lap.get("StartTime"), "%Y-%m-%dT%H:%M:%S.%fZ")
                lapDto.totalTime = float(lap.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}TotalTimeSeconds").text)
                lapDto.averageHartRate  = self._getAverageHartRate(lap)
                lapDto.distanceMeters = self._getDistance(lap)
                lapDto.triggerMethod = self._getTriggerMethod(lap)
                lapDto.maxHartRate = self._getMaxHartRate(lap)
                lapDto.maxSpeed = self._getMaxSpeed(lap)
                lapDto.intensity = self._getIntensity(lap)
                lapDto.calories = self._getCalories(lap)
                dto.laps.append(lapDto)
                self.updateProgress.emit(int((index + 1) * 25 / lapCount))
            # Extract track point data (GPS data, heart rate, etc.)
            self.statusMessage.emit(StatusMessage('Loading track points'))
            trackPoints = root.findall(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Trackpoint")
            trackPointsCount = len(trackPoints)
            for index, trackPoint in enumerate(trackPoints):
                track = TrackDataDTO()
                track.time = self._getDateTimeUTC(trackPoint)
                track.latitude = self._getLatitude(trackPoint)
                track.longitude = self._getLongitude(trackPoint)
                track.altitude = self._getAltitude(trackPoint)
                track.hartRate = self._getHartRate(trackPoint)
                track.distance = self._getDistance(trackPoint)
                track.speed =  self._getSpeedExtension(trackPoint)
                track.sensorState = self._getSensorState(trackPoint)
                dto.trackPoints.append(track)
                self.updateProgress.emit(int(25 + (index + 1) * 75 / trackPointsCount))
            self.updateProgress.emit(100)
            self.trackPointsChanged.emit(dto.trackPoints)
            self.statusMessage.emit(None)
            self.updateProgress.emit(0)
            self.fileDataChanged.emit(dto)
        except ET.ParseError as e:
            print(f"Error parsing TCX file: {e}")

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


