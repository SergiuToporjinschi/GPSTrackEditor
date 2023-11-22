from typing import Type

class StatisticsDto:
    _dtoAttribute: str = None
    _dataType: Type = None
    _title: str = None
    _min: float = None
    _avg: float = None
    _max: float = None
    _missing: int = 0
    _func: str = None
    def __init__(self, attr: str, dataTye: Type, title: str, func: str = None) -> None:
        self._dtoAttribute = attr
        self._dataType = dataTye
        self._title = title
        self._func = func
        pass

    @property
    def title(self) -> float:
        return self._title

    @title.setter
    def title(self, title:str):
        self._title = title

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
    def dataType(self) -> Type:
        return self._dataType

    @dataType.setter
    def dataType(self, dataType:Type):
        self._dataType = dataType

    @property
    def dtoAttribute(self) -> str:
        return self._dtoAttribute

    @dtoAttribute.setter
    def dtoAttribute(self, dtoAttribute:str):
        self._dtoAttribute = dtoAttribute

    @property
    def func(self) -> str:
        return self._func

    @func.setter
    def func(self, func: str):
        self._func = func
