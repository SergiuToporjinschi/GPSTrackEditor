import typing, enum

from PySide6.QtGui import QColor

class MarkerDto:

    class MakerIteratorType(enum.Enum):
        OneByOne = 1
        FreeAtOnce = 2

    _name: str = None
    _category: str = None
    _indexes: list[int] = None
    _color: str = None
    _expression: str = None
    _iteratorType: MakerIteratorType = MakerIteratorType.OneByOne
    _active: bool = None

    def __init__(self, name: str, indexes:list[int], color:QColor, expression: typing.Optional[str] = None, active: bool = None) -> None:
        self._name = name
        self._indexes = indexes
        self._color = color
        self._expression = expression
        self._active = active
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, typeName:str):
        self._category = typeName

    @property
    def indexes(self):
        return self._indexes

    @indexes.setter
    def indexes(self, indexes: list[int]):
        self._indexes = indexes

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    @property
    def expression(self) -> str:
        return self._expression

    @expression.setter
    def expression(self, expression: str):
        self._expression = expression

    @property
    def iteratorType(self) -> MakerIteratorType:
        return self._iteratorType

    @iteratorType.setter
    def iteratorType(self, iteratorType: MakerIteratorType):
        self._iteratorType = iteratorType

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, active: bool):
        self._active = active

    @property
    def countIndexes(self):
        return len(self.indexes)

    def __eq__(self, other):
        # Customize the equality comparison based on your requirements
        if isinstance(other, MarkerDto):
            return self.name == other.name
        return False
