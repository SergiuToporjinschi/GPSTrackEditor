import typing
from PySide6.QtGui import QColor
from .AbstractDto import AbstractDto

class MarkerDto(AbstractDto):
    name: str = None
    category: str = None
    indexes: list[int] = None
    color: str = None
    expression: str = None
    active: bool = None

    @classmethod
    def initFrom(cls, category: str, expression:str):
        return cls(None, category, None, None, expression)

    def __init__(self, name: str = None, category:str=None, indexes:list[int]= None, color:QColor= None, expression: typing.Optional[str] = None, active: bool = None) -> None:
        self.name: str = name
        self.category: str = category
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
