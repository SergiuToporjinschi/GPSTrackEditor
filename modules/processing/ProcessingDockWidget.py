from PySide6.QtWidgets import QDockWidget
from abstracts import AbstractModelWidget
from gui.processing_dock_ui import Ui_DockWidget as processingDock

class ProcessingDockWidget(AbstractModelWidget, QDockWidget, processingDock):

    def _setupUi(self):
        self.buttonCalculateSpeed.clicked.connect(self._calculateSpeed)
        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))

    def _calculateSpeed(self):
        self.model.allTrackPoints
        pass