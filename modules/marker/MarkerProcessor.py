from dto import MarkerDto, MarkerCategory
import pandas as pd


class AbstractMarkerProcessor:
    def __init__(self, dataFrame:pd.DataFrame, marker: MarkerDto) -> None:
        self.df = dataFrame
        self.marker = marker
        pass

    def getIndexes(self):
        pass

    def testExpression(self) -> bool:
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
    def buildProcessor(cls, marker: MarkerDto, data: pd.DataFrame) -> AbstractMarkerProcessor:
        if marker.category == MarkerCategory.Custom:
            return CustomMarkerProcessor(data, marker)
        elif marker.category == MarkerCategory.Stationary:
            return StationaryMarkerProcessor(data, marker)
        else:
            raise ValueError('Invalid groupName!!!')
    pass