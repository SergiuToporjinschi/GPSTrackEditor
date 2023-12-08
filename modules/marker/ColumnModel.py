from typing import Type

class ColumnModel:
    _title: str = None
    _editable: bool = None
    _editControl: Type = None
    _dtoAttributeType: Type = None
    _dtoAttributeName: str = None
    def __init__(self, title:str, editable: bool, editControl: Type, dtoAttributeType: Type, dtoAttributeName: str) -> None:
        self._title = title
        self._editable = editable
        self._editControl = editControl
        self._dtoAttributeType = dtoAttributeType
        self._dtoAttributeName = dtoAttributeName
        pass

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title:str):
        self._title = title

    @property
    def editable(self) -> bool:
        return self._editable

    @editable.setter
    def editable(self, editable: bool):
        self._editable = editable

    @property
    def editControl(self) -> Type:
        return self._editControl

    @editControl.setter
    def editControl(self, editControl: Type):
        self._editControl = editControl

    @property
    def dtoAttributeType(self) -> Type:
        return self._dtoAttributeType

    @dtoAttributeType.setter
    def dtoAttributeType(self, dtoAttributeType: Type):
        self._dtoAttributeType = dtoAttributeType

    @property
    def dtoAttributeName(self) -> str:
        return self._dtoAttributeName

    @dtoAttributeName.setter
    def dtoAttributeName(self, dtoAttributeName: str):
        self._dtoAttributeName = dtoAttributeName