import typing
import enum
import UtilFunctions as Util
from PySide6.QtGui import QColor

class MarkerCategory(enum.Enum):
    Custom = 'Custom'
    Stationary = 'Stationary'

    @classmethod
    def fromString(cls, value:str):
        for i in MarkerCategory:
            if i.value == value:
                return i
        return None


class MarkerDto:
    name: str = None
    category: MarkerCategory = None
    indexes: list[int] = None
    color: str = None
    expression: str = None
    active: bool = None

    @classmethod
    def initFrom(cls, category: MarkerCategory, expression:str):
        return cls(None, category, None, Util.generateRandomColor(), expression)

    def __init__(self, name: str = None, category:MarkerCategory=None, indexes:list[int]= None, color:QColor = Util.generateRandomColor(), expression: typing.Optional[str] = None, active: bool = None) -> None:
        self.name: str = name
        self.category: MarkerCategory = category
        self.indexes: list[int] = indexes
        self.color: str = color
        self.active: bool = active
        self.expression: str = expression
        pass

    @property
    def countIndexes(self):
        return len(self.indexes) if self.indexes is not None else 0

    def __eq__(self, other):
        # Customize the equality comparison based on your requirements
        if isinstance(other, MarkerDto):
            return self.name == other.name
        return False

    def __getstate__(self):
        state = self.__dict__.copy()
        state['active'] = False
        if 'indexes' in state: del state['indexes']
        return state