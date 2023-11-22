from .map_dock_ui import Ui_DockWidget as mapDock
from .statistics_dock_ui import Ui_DockWidget as statisticsDock
from .file_info_dock_ui import Ui_DockWidget as fileInfoDock
from .filter_dock_ui import Ui_DockWidget as filterDock
from .processing_dock_ui import Ui_DockWidget as processingDock
from .marking_dock_ui import Ui_DockWidget as markingDock
from .DockWidget import MarkingDockWidget, ProcessingDockWidget, FilterDockWidget, FileInfoDockWidget, StatisticsDockWidget, MapDockWidget

__all__ = [
    "mapDock",
    "statisticsDock",
    "fileInfoDock",
    "filterDock",
    "processingDock",
    "markingDock",
    "MarkingDockWidget",
    "ProcessingDockWidget",
    "FilterDockWidget",
    "FileInfoDockWidget",
    "StatisticsDockWidget",
    "MapDockWidget"
]