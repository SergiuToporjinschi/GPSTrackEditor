import enum
from typing import Any, Optional, overload
from PySide6.QtCore import QSettings, QObject

class ConfigGroup(enum.Enum):
    General = 'General'
    MainWindow = 'mainWindow'
    TrackGrid = 'trackGrid'
    MarkingDockWidget = 'markingDockWidget'

class ConfigAttribute(enum.Enum):
    Geometry = 'geometry'
    State = 'state'
    State1 = 'state1'
    Sorting = 'sorting'
    Location = 'location'

class Config(QSettings):

    def __init__(self) -> None:
        super().__init__("./settings.ini", QSettings.Format.IniFormat)
        self.status()
        pass

    @staticmethod
    def setValueG(group: ConfigGroup, attribute: ConfigAttribute, val: Any) -> None:
        # if (isinstance(val, enum.Enum)):
        #     val = val.value
        #     pass
        Config().setValue(f"{group.value}/{attribute.value}", val)

    @staticmethod
    def valueG(group: ConfigGroup, attribute: ConfigAttribute, default: Any) -> Any:
        # origVal = Config().value(f"{group.value}/{attribute.value}", default)
        return Config().value(f"{group.value}/{attribute.value}", default)

    # def _convertToIntOrEnum(origVal, default):
    #     if isinstance(origVal, str) and origVal.isnumeric():
    #         if isinstance(default, enum.Enum):
    #             try:
    #                 return {str(member.value): member for member in default.__class__}.get(origVal)
    #             except ValueError: pass

    #         elif isinstance(default, int):
    #             try:
    #                 return int(origVal)
    #             except ValueError: pass

    #         elif isinstance(default, float):
    #             try:
    #                 return float(origVal)
    #             except ValueError: pass
    #     return origVal