from typing import Type

class StatisticsDto:
    _dtoAttribute: str = None
    _min: float = None
    _avg: float = None
    _max: float = None
    _missing: int = 0
    def __init__(self, attr: str) -> None:
        self._dtoAttribute = attr
        pass

    @property
    def min(self) -> float:
        return self._min

    @min.setter
    def min(self, min:float):
        self._min = min

    @property
    def avg(self) -> float:
        return self._avg

    @avg.setter
    def avg(self, avg:float):
        self._avg = avg

    @property
    def max(self) -> float:
        return self._max

    @max.setter
    def max(self, max:float):
        self._max = max

    @property
    def missing(self) -> float:
        return self._missing

    @missing.setter
    def missing(self, missing:float):
        self._missing = missing

    @property
    def dtoAttribute(self) -> str:
        return self._dtoAttribute

    @dtoAttribute.setter
    def dtoAttribute(self, dtoAttribute:str):
        self._dtoAttribute = dtoAttribute
