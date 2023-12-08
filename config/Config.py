import enum
from typing import Any

from PySide6.QtCore import QSettings

class ConfigGroup(enum.Enum):
    General = 'General'
    MainWindow = 'mainWindow'
    TrackGrid = 'trackGrid'
    MarkingDockWidget = 'markingDockWidget'
    ProcessingDockWidget = 'processingDockWidget'

class ConfigAttribute(enum.Enum):
    Geometry = 'geometry'
    State = 'state'
    State1 = 'state1'
    Sorting = 'sorting'
    Location = 'location'
    Markers = 'markers'
    CustomColumns = 'customColumns'

class Config(QSettings):

    def __init__(self) -> None:
        super().__init__("./settings.ini", QSettings.Format.IniFormat)
        self.status()
        pass

    @staticmethod
    def setValueG(group: ConfigGroup, attribute: ConfigAttribute, val: Any) -> None:
        Config().setValue(f"{group.value}/{attribute.value}", val)

    @staticmethod
    def valueG(group: ConfigGroup, attribute: ConfigAttribute, default: Any) -> Any:
        return Config().value(f"{group.value}/{attribute.value}", default)
