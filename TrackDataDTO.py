from datetime import datetime
from typing import List

class TrackDataDTO:
    time: datetime = None
    latitude: float = None
    longitude: float = None
    altitude: float = None
    hartRate: int = None
    distance: float = None
    calculatedDistance: float = None
    speed: float = None
    calculatedSpeed: float = None
    sensorState: str = None

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