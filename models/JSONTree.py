from typing import List, Dict, Union


class JSONTreeItem:

    def __init__(self, parent: "JSONTreeItem" = None):
        self._parent = parent
        self._attribute = ""
        self._value = ""
        self._value_type = None
        self._children = []

    def appendChild(self, item: "JSONTreeItem"):
        self._children.append(item)

    def child(self, row: int) -> "JSONTreeItem":
        return self._children[row]

    def parent(self) -> "JSONTreeItem":
        return self._parent

    def childCount(self) -> int:
        return len(self._children)

    def row(self) -> int:
        return self._parent._children.index(self) if self._parent else 0

    @property
    def attribute(self) -> str:
        return self._attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self._attribute = attribute

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    @property
    def valueType(self):
        return self._value_type

    @valueType.setter
    def valueType(self, value):
        self._value_type = value


    @classmethod
    def load(cls, value: Union[List, Dict], parent: "JSONTreeItem" = None, sort=True) -> "JSONTreeItem":
        rootItem = JSONTreeItem(parent)
        rootItem.attribute = "root"

        if isinstance(value, dict):
            # items = sorted(value.items()) if sort else value.items()
            items = value.items()
            for attribute, value in items:
                child = cls.load(value, rootItem)
                child.attribute = attribute
                child.valueType = type(value)
                rootItem.appendChild(child)

        elif isinstance(value, list):
            for index, value in enumerate(value):
                child = cls.load(value, rootItem)
                child.attribute = index
                child.valueType = type(value)
                rootItem.appendChild(child)

        else:
            rootItem.value = value
            rootItem.valueType = type(value)

        return rootItem
