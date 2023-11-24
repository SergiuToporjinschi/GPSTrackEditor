import typing, re
from PySide6.QtGui import QPalette, QColor, QColorConstants
from PySide6.QtWidgets import QColorDialog

from dto import MarkerDto
from abstracts import AbstractModelWidget, AbstractWidgetMaximizeable
from StatusMessage import StatusMessage

from gui.marking_dock_ui import Ui_DockWidget as markingDock


class MarkingDockWidget(AbstractModelWidget, AbstractWidgetMaximizeable, markingDock):
    colorCustomMarking:QColor = QColorConstants.Red
    colorStationaryMarking: QColor = QColorConstants.Yellow
    pattern = re.compile(r'([<|>|=|\s]+)\s*(\d*[.|,]?\d+)\s*([&|]{1})*\s*')
    markers : [MarkerDto] = []

    def _setupUi(self):
        self._setColor(self.pushStatMarkSelColor, self.colorStationaryMarking)
        self._setColor(self.pushCustomMarkSelColor, self.colorCustomMarking)

        self.pushCustomMark.clicked.connect(self._onCustomMarkButton)
        self.pushCustomMarkClear.clicked.connect(lambda: self._clearMarker('custom'))
        self.pushCustomMarkSelColor.clicked.connect(lambda: self._setColor(self.pushCustomMarkSelColor))

        self.pushStatMark.clicked.connect(self._markStationary)
        self.pushStatMarkClear.clicked.connect(lambda: self._clearMarker('stationary'))
        self.pushStatMarkSelColor.clicked.connect(lambda: self._setColor(self.pushStatMarkSelColor))

        self.model.contentChanged.connect(self._refreshMarkers)
        self.model.trimRangeChanged.connect(self._refreshMarkers)

        self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))
        pass

    def _setColor(self, control, color = None):
        if color is None:
            color = QColorDialog.getColor()
        if color.isValid():
            pal = QPalette()
            pal.setColor(QPalette.ColorRole.Button, color)
            control.setPalette(pal)
        pass

    def _markStationary(self, marker: typing.Optional[MarkerDto] = None):
        self.statusMessage.emit(StatusMessage('Marking...'))
        self.updateProgress.emit(0)
        color = self.pushStatMarkSelColor.palette().button().color()
        tolerance = self.spinBoxMarkStatTolerance.value()
        marker = MarkerDto('stationary', [], color, tolerance) if not isinstance(marker, MarkerDto) or marker is None else marker
        marker.indexes.clear()
        prevItem = None
        trackPointsCount = len(self.model.allTrackPoints)
        for index, item in enumerate(self.model.allTrackPoints):
            self.updateProgress.emit(int((index + 1)/trackPointsCount))
            self.statusMessage.emit(StatusMessage(f'Marking... index {index}'))
            dist = item.getValueByColName('distance')
            prevDist = prevItem.getValueByColName('distance') if prevItem is not None else None
            if dist is not None and prevDist is not None and abs(prevDist - dist) <= marker.expression:
                marker.indexes.append(index)
                marker.indexes.append(index - 1)
            prevItem = item
        self._applyMarker(marker)
        self.updateProgress.emit(0)
        self.statusMessage.emit(None)
        pass

    def _clearMarker(self, name):
        self.markers[:] = [maker for maker in self.markers if maker.name != name]
        self.model.clearMarker(name)
        pass

    def _onCustomMarkButton(self, marker: typing.Optional[MarkerDto] = None):
        self.statusMessage.emit(StatusMessage('Marking...'))
        marker = self._buildCustomMarker() if not isinstance(marker, MarkerDto) or marker is None else marker
        try:
            marker.indexes = []
            trackPointsCount = len(self.model.allTrackPoints)
            for index, item in enumerate(self.model.allTrackPoints):
                self.updateProgress.emit(int((index + 1)/trackPointsCount))
                if eval(marker.expression):
                    marker.indexes.append(index)
            self.updateProgress.emit(0)
        except Exception:
            self._lastFindDataExpression = None
            self.statusMessage.emit(f"Syntax error (syntax: <=,<,<>><value><&,|>)")
        self._applyMarker(marker)
        self.statusMessage.emit(None)
        self.updateProgress.emit(0)
        pass

    def _buildCustomMarker(self):
        findBy = {
            "time": self.editFindByTime.text(),
            "latitude": self.editFindByLatitude.text(),
            "longitude": self.editFindByLongitude.text(),
            "distance": self.editFindByDistance.text(),
            "calculatedDistance": self.editFindByCalculatedDistance.text(),
            "altitude": self.editFindByAltitude.text(),
            "speed": self.editFindBySpeed.text(),
            "calculatedSpeed": self.editFindByCalculatedSpeed.text(),
            "hartRate": self.editFindByHartRate.text(),
            "sensorState": self.editFindBySensorState.text()
        }
        expression = []
        for key, value in findBy.items():
            if value is not None and value.strip() != "":
                expression.append(self._buildCustomMarkerKey(key, self.pattern.findall(value)))
        color = self.pushCustomMarkSelColor.palette().button().color()
        return MarkerDto('custom', [], color, ' or '.join(expression))

    def _buildCustomMarkerKey(self, key:str, expression: list[tuple]):
        result = ''
        # key = 'item.data["'+key+'"]'
        key = f'item.getValueByColName("{key}")'
        for item in expression:
            item = [key] + [(val.replace('&', 'and').replace('|', 'or').replace('=', '==')) for val in item]
            result += ' '.join(item) + ' '
        return key + ' is not None and ' + result.strip()

    def _applyMarker(self, marker: MarkerDto):
        if marker not in self.markers:
            self.markers.append(marker)
        self.model.addMarker(marker)
        pass

    def _refreshMarkers(self):
        self.model.clearAllMarker()

        for marker in self.markers:
            if marker.name == 'custom':
                self._onCustomMarkButton(marker)
            elif marker.name == 'stationary':
                self._markStationary(marker)
            self.model.addMarker(marker)
        pass
