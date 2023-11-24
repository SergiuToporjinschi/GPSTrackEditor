import typing, enum

from PySide6.QtGui import QColor


class MarkerDto:

    class MakerIteratorType(enum.Enum):
        OneByOne = 1
        FreeAtOnce = 2

    _name: str = None
    _typeName: str = None
    _indexes: list[int] = None
    _color: QColor = None
    _expression: str = None
    _iteratorType: MakerIteratorType = MakerIteratorType.OneByOne

    def __init__(self, name: str, indexes:list[int], color:QColor, expression: typing.Optional[str] = None) -> None:
        self._name = name
        self._indexes = indexes
        self._color = color
        self._expression = expression
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self._name = name

    @property
    def typeName(self):
        return self._typeName

    @typeName.setter
    def typeName(self, typeName:str):
        self._typeName = typeName

    @property
    def indexes(self):
        return self._indexes

    @indexes.setter
    def indexes(self, indexes: list[int]):
        self._indexes = indexes

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color:QColor):
        self._color = color

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, expression: str):
        self._expression = expression

    @property
    def iteratorType(self):
        return self._iteratorType

    @iteratorType.setter
    def iteratorType(self, iteratorType: MakerIteratorType):
        self._iteratorType = iteratorType

    @property
    def countIndexes(self):
        return len(self.indexes)

    def __eq__(self, other):
        # Customize the equality comparison based on your requirements
        if isinstance(other, MarkerDto):
            return self.name == other.name
        return False