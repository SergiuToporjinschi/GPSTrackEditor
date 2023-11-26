import typing, re
from typing import Union
from PySide6.QtGui import QPalette, QColor, QColorConstants
from PySide6.QtWidgets import QColorDialog, QColorDialog, QHeaderView, QMessageBox
from PySide6.QtCore import Qt, QItemSelectionModel, QModelIndex, QItemSelection

from .MarkerListDelegate import MarkerListDelegate
from dto import MarkerDto
from abstracts import AbstractModelWidget, AbstractWidgetMaximizeable
from StatusMessage import StatusMessage
from .MarkerStatusModel import MarkerStatusModel
from gui.marking_dock_ui import Ui_DockWidget as markingDock

class MarkerRecordSelectionModel(QItemSelectionModel):
    def __init__(self, model):
        super().__init__(model)

    def select(self, selection: Union[QItemSelection, QModelIndex], command : QItemSelectionModel.SelectionFlag):
        if isinstance(selection, QItemSelection):
            selected_indexes = selection.indexes()
            for index in selected_indexes:
                if not isinstance(index.internalPointer(), MarkerDto):
                    return  # Do not allow selection for this row
        else:
            if not isinstance(selection.internalPointer(), MarkerDto):
                return
        super().select(selection, command)  # Allow selection for other rows


class MarkingDockWidget(AbstractModelWidget, AbstractWidgetMaximizeable, markingDock):
    colorCustomMarking:QColor = QColorConstants.Red
    colorStationaryMarking: QColor = QColorConstants.Yellow
    pattern = re.compile(r'([<|>|=|\s]+)\s*(\d*[.|,]?\d+)\s*([&|]{1})*\s*')
    markers : [MarkerDto] = []

    def _setupUi(self):
        self.pushAdd.clicked.connect(self._onAddMarker)
        self.treeViewMarker.setItemDelegate(MarkerListDelegate())

        self.markerTreeModel = MarkerStatusModel(self)
        self.treeViewMarker.setModel(self.markerTreeModel)
        self._resizeHeader(self.treeViewMarker.header())

        self.treeViewMarker.expandAll()
        self.toolActivate.toggled.connect(self._onActivate)
        self.toolDelete.clicked.connect(self._onDelete)

        self.treeViewMarker.setSelectionModel(MarkerRecordSelectionModel(self.markerTreeModel))
        self.treeViewMarker.selectionModel().currentRowChanged.connect(self._onSelectionChanged)


        # self.markerTreeModel.selecselectionModel
        # for i, item in range(self.markerTreeModel.rowCount(None)):
        #     index = self.markerTreeModel.index(i, 5)
        #     self.treeViewMarker.setIndexWidget(index, QPushButton('Apply'))
        # model.index(0,0, model._markerData[0])
        # model.beginResetModel()
        # marker = MarkerDto('Dot dead', [],  QColor('red'), 'hartRate>0')
        # marker.iteratorType = MarkerDto.MakerIteratorType.OneByOne
        # marker.category = MarkerCategory.Custom
        # model._markerData[0].markers.append(marker)
        # model.endResetModel()
        # model.insertRow()
        # self._setColor(self.pushStatMarkSelColor, self.colorStationaryMarking)
        # self._setColor(self.pushCustomMarkSelColor, self.colorCustomMarking)

        # self.pushCustomMark.clicked.connect(self._onCustomMarkButton)
        # self.pushCustomMarkClear.clicked.connect(lambda: self._clearMarker('custom'))
        # self.pushCustomMarkSelColor.clicked.connect(lambda: self._setColor(self.pushCustomMarkSelColor))

        # self.pushStatMark.clicked.connect(self._markStationary)
        # self.pushStatMarkClear.clicked.connect(lambda: self._clearMarker('stationary'))
        # self.pushStatMarkSelColor.clicked.connect(lambda: self._setColor(self.pushStatMarkSelColor))

        # self.model.contentChanged.connect(self._refreshMarkers)
        # self.model.trimRangeChanged.connect(self._refreshMarkers)

        # self.model.mainSeriesLengthChanged.connect(lambda cnt: self.setEnabled(cnt > 0))
        pass

    def _resizeHeader(self, header:QHeaderView):
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

    def _onActivate(self, value:bool):
        currentSelection:QItemSelectionModel = self.treeViewMarker.selectionModel()
        colIndex = currentSelection.model().headerModelIndex('active')
        for selected in currentSelection.selectedRows(colIndex):
            self.markerTreeModel.setData(selected, value, Qt.ItemDataRole.EditRole)

    def _onDelete(self):
        currentSelection:QItemSelectionModel = self.treeViewMarker.selectionModel()

        item = currentSelection.currentIndex().internalPointer()
        confirmation = QMessageBox.question(
            None, "Delete", f"Are you sure you want to delete marker: \"{item.name}\"?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        )
        if confirmation == QMessageBox.StandardButton.No: return

        model = currentSelection.model()

        for indexToDelete in currentSelection.selectedRows(0):
            parentIndex = model.parent(indexToDelete )
            model.removeRow(indexToDelete.row(), parentIndex)
        pass

    def _onSelectionChanged(self, newIndex: QModelIndex, oldIndex: QModelIndex):
        item = newIndex.internalPointer()

        self.toolActivate.blockSignals(True)
        self.toolDelete.blockSignals(True)

        self.toolDelete.setEnabled(isinstance(item, MarkerDto))
        self.toolActivate.setEnabled(isinstance(item, MarkerDto))

        self.toolActivate.setChecked(isinstance(item, MarkerDto) and item.active)

        self.toolActivate.blockSignals(False)
        self.toolDelete.blockSignals(False)
        pass

    def _onAddMarker(self):
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

