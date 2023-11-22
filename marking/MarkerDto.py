import typing

from PySide6.QtGui import QColor


class MarkerDto:
    _name: str = None
    _indexes: list[int] = None
    _color: QColor = None
    _expression: str = None
    def __init__(self, name: str, indexes:list[int], color:QColor, expression: typing.Optional[str] = None) -> None:
        self._name = name
        self._indexes = indexes
        self._color = color
        self._expression = expression
        pass

    @property
    def name(self):
        return self._name

    @property
    def indexes(self):
        return self._indexes

    @indexes.setter
    def indexes(self, indexes: []):
        self._indexes = indexes

    @property
    def color(self):
        return self._color

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, expression: str):
        self._expression = expression

    def __eq__(self, other):
        # Customize the equality comparison based on your requirements
        if isinstance(other, MarkerDto):
            return self.name == other.name
        return False