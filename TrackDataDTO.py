from datetime import datetime
from typing import List

class TrackDataDTO:
    def __init__(self):
        self._time: datetime = None
        self._latitude: float = None
        self._longitude: float = None
        self._altitude: float = None
        self._hartRate: int = None
        self._distance: float = None
        self._calculatedDistance: float = None
        self._speed: float = None
        self._calculatedSpeed: float = None
        self._sensorState: str = None

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time: datetime):
        self._time = time

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self._longitude = longitude

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, altitude: float):
        self._altitude = altitude

    @property
    def hartRate(self):
        return self._hartRate

    @hartRate.setter
    def hartRate(self, hartRate: int):
        self._hartRate = hartRate

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        self._distance = distance

    @property
    def calculatedDistance(self):
        return self._calculatedDistance

    @calculatedDistance.setter
    def calculatedDistance(self, calculatedDistance: float):
        self._calculatedDistance = calculatedDistance

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed: float):
        self._speed = speed

    @property
    def calculatedSpeed(self):
        return self._calculatedSpeed

    @calculatedSpeed.setter
    def calculatedSpeed(self, calculatedSpeed: float):
        self._calculatedSpeed = calculatedSpeed

    @property
    def sensorState(self):
        return self._sensorState

    @sensorState.setter
    def sensorState(self, sensorState: float):
        self._sensorState = sensorState


    def __repr__(self) -> str:
        return f'time: {self.time}, altitude: {self.altitude}, heartRate: {self.hartRate}'


class LapDataDTO:
    startTime: datetime = None
    totalTime: float = None
    averageHartRate: float = None
    distanceMeters: float = None
    triggerMethod: str = None
    maxHartRate: int = None
    maxSpeed: float = None
    intensity: str = None
    calories: int = None

    def __repr__(self) -> str:
        return f'start: {self.startTime}, totalTime: {self.totalTime}'


class FileDataDTO:
    filePath: str = None
    activityType: str = None
    id: str = None
    notes: str = None
    laps: list[LapDataDTO] = []
    trackPoints: list[TrackDataDTO] = []

    @property
    def startTime(self) -> datetime:
        return None if self.trackPoints == None or len(self.trackPoints) <= 0 else self.trackPoints[0]

    @property
    def lapsCount(self) -> int:
        return len(self.laps)

    @property
    def trackPointsCount(self) -> int:
        return len(self.trackPoints)

    def __repr__(self) -> str:
        return f'trackPoints: {self.trackPointsCount}, laps: {self.lapsCount}, file: {self.filePath}'