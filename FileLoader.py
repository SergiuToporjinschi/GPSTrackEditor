import xml.etree.ElementTree as ET
import pytz, threading
from typing import List
from datetime import datetime
from qtpy.QtCore import Signal

from PySide6.QtCore import QObject
from TrackDataDTO import FileDataDTO, LapDataDTO, TrackDataDTO

class TCXLoader(QObject):
    workingProgress = Signal(int)
    fileDataChanged = Signal(FileDataDTO)
    trackPointsChanged = Signal(list)

    def __init__(self):
        super().__init__()

    def load_tcx_file(self, file_path):
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

            # self.data['calories'] = lap.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Calories").text
            # Extract lap data
            laps = root.findall(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Lap")
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
                # self.workingProgress.emit(int((index + 1) * 25 / len(laps)))

            # Extract trackpoint data (GPS data, heart rate, etc.)
            trackpoints = root.findall(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Trackpoint")
            for index, trackPoint in enumerate(trackpoints):
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
                # self.data['trackpoints'].append(TrackPointModel(time, latitude, longitude, altitude, heart_rate, distance, speed, sensorState))
                # self.workingProgress.emit(int(25 + (index + 1) * 75 / len(trackpoints)))
            self.trackPointsChanged.emit(dto.trackPoints)
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


