from dto import MarkerDto, TrackDataDTO, MarkerCategory
import pandas as pd
import UtilFunctions as Util


class AbstractMarkerProcessor:
    def __init__(self, dataFrame:pd.DataFrame, marker: MarkerDto, dataItemsList: list[TrackDataDTO]) -> None:
        self.df = dataFrame
        self.data = dataItemsList
        self.marker = marker
        pass

    def getIndexes(self):
        pass

class CustomMarkerProcessor(AbstractMarkerProcessor):

    def getIndexes(self):
        filtered_dfs = self.df.query(self.marker.expression)
        return filtered_dfs.index.tolist()
    pass

class StationaryMarkerProcessor(CustomMarkerProcessor):
    def getIndexes(self):
        self.df['distanceDifference'] = self.df['distance'].diff().abs()
        super().getIndexes()
        return super().getIndexes()
    pass


class MarkerProcessorFactory:

    @classmethod
    def buildProcessor(cls, marker: MarkerDto, dataItemsList: list[TrackDataDTO]) -> AbstractMarkerProcessor:
        objList = [(obj.time,
                obj.latitude,
                obj.longitude,
                obj.altitude,
                obj.hartRate,
                obj.distance,
                obj.calculatedDistance,
                obj.speed,
                obj.calculatedSpeed,
                obj.sensorState) for obj in dataItemsList][:]

        cols = Util.getClassPublicAttributes(TrackDataDTO)

        df = pd.DataFrame(objList, columns=cols)

        if marker.category == MarkerCategory.Custom:
            return CustomMarkerProcessor(df, marker, dataItemsList)
        elif marker.category == MarkerCategory.Stationary:
            return StationaryMarkerProcessor(df, marker, dataItemsList)
        else:
            raise ValueError('Invalid groupName!!!')
    pass