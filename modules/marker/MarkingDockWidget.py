
import pandas as pd
from typing import Union
from PySide6.QtGui import QColor, QColorConstants
from PySide6.QtWidgets import QHeaderView, QMessageBox
from PySide6.QtCore import Qt, QItemSelectionModel, QModelIndex, QItemSelection
from qtpy.QtCore import Signal

from config import *
from .MarkerListDelegate import MarkerListDelegate
from dto import MarkerDto, TrackDataDTO, MarkerCategory, MarkerGroupDto
from abstracts import AbstractModelWidget, AbstractWidgetMaximizeable
from StatusMessage import StatusMessage
from .MarkerStatusModel import MarkerStatusModel
from .MarkerProcessor import MarkerProcessorFactory, AbstractMarkerProcessor
from gui.marking_dock_ui import Ui_DockWidget as markingDock
import UtilFunctions as Util


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
    markers : [MarkerDto] = []

    markerActivated = Signal(MarkerDto, bool) #emitted when a marker is activated or deactivated (marker data, active)

    def _setupUi(self):
        self.pushAdd.clicked.connect(self._onAddMarker)
        self.treeViewMarker.setItemDelegate(MarkerListDelegate())

        self.markerTreeModel = MarkerStatusModel(self)
        self.treeViewMarker.setModel(self.markerTreeModel)

        self._resizeHeader(self.treeViewMarker.header())

        self.treeViewMarker.expandAll()
        self.toolActivate.toggled.connect(self._onActivate)
        self.toolActivate.toggled.connect(lambda state: self.toolActivate.setText('Clear' if state else 'Apply'))
        self.toolDelete.clicked.connect(self._onDelete)
        self.toolActivateAll.clicked.connect(lambda: self._changeStateAllMarkers(True))
        self.toolClearAll.clicked.connect(lambda: self._changeStateAllMarkers(False))

        self.treeViewMarker.setSelectionModel(MarkerRecordSelectionModel(self.markerTreeModel))
        self.treeViewMarker.selectionModel().currentRowChanged.connect(self._onSelectionChanged)
        self.markerTreeModel.modelReset.connect(self.treeViewMarker.expandAll)

        self.markerActivated.connect(self.model.markerActivated)
        self.model.mainSeriesChanged.connect(lambda: self._changeStateAllMarkers(False))
        pass

    def _resizeHeader(self, header:QHeaderView):
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)

    def _onActivate(self, value:bool):
        currentSelection:QItemSelectionModel = self.treeViewMarker.selectionModel()
        colIndex = currentSelection.model().headerModelIndex('active')
        for selected in currentSelection.selectedRows(colIndex):
            marker:MarkerDto = selected.internalPointer()
            if value: marker.indexes = self._calculateIndexes(marker)
            self.markerActivated.emit(marker, value)
            self.markerTreeModel.setData(selected, value, Qt.ItemDataRole.EditRole)

    def _onDelete(self):
        currentSelection:QItemSelectionModel = self.treeViewMarker.selectionModel()

        item = currentSelection.currentIndex().internalPointer()
        confirmation = QMessageBox.question(
            None, 'Delete', f'Are you sure you want to delete marker: "{item.name}"?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        )
        if confirmation == QMessageBox.StandardButton.No: return

        selectionModel = currentSelection.model()

        for indexToDelete in currentSelection.selectedRows(0):
            parentIndex = selectionModel.parent(indexToDelete)
            selectionModel.removeRow(indexToDelete.row(), parentIndex)
            self.markerActivated.emit(indexToDelete.internalPointer(), False)

    def _onSelectionChanged(self, newIndex: QModelIndex, oldIndex: QModelIndex):
        item = newIndex.internalPointer()

        self.toolActivate.blockSignals(True)
        self.toolDelete.blockSignals(True)

        self.toolDelete.setEnabled(isinstance(item, MarkerDto))
        self.toolActivate.setEnabled(isinstance(item, MarkerDto))

        self.toolActivate.setChecked(isinstance(item, MarkerDto) and item.active == True)
        if isinstance(item, MarkerDto):
            self.toolActivate.setText('Clear' if item.active else 'Apply')

        self.toolActivate.blockSignals(False)
        self.toolDelete.blockSignals(False)
        pass

    def _onAddMarker(self):
        name:str = self.editMarkerName.text()
        markerCategory = MarkerCategory.fromString(self.tabWidget.currentWidget().property('markerCategory'))
        if not self._isValidMarkerName(name):
            self.statusMessage.emit(StatusMessage.error('Marker name must be unique!'))
            return

        if name is None or len(name.strip()) <= 0:
            self.statusMessage.emit(StatusMessage.error('Marker name is mandatory!'))
            return

        if markerCategory == MarkerCategory.Custom:
            expression = self._buildMarkerBaseOnDto(TrackDataDTO)
        else:
            expression = f'distanceDifference >= 0 and distanceDifference <= {self.spinBoxStatTolerance.value()}'

        if expression is None or len(expression.strip()) <= 0:
            self.statusMessage.emit(StatusMessage.error('Nothing to save there is no expression!'))
            return

        marker = MarkerDto.initFrom(markerCategory, expression)
        marker.name = self.editMarkerName.text()
        marker.indexes = self._calculateIndexes(marker)
        self.markerTreeModel.addRow(marker)

    def _isValidMarkerName(self, name:str):
        for item, _ in self.markerTreeModel.iterateAll():
            item:MarkerDto
            if name == item.name:
                return False
        return True

    def _buildMarkerBaseOnDto(self, type: type) -> MarkerDto:
        fields = [item for item in vars(self) if item.startswith('editAttr')][:]
        fieldExpressions = []
        for item in Util.iterateClassPublicAttributes(type, lambda it: it[0] != '_' and f'editAttr{it[0].upper() + it[1:]}' in fields) :
            value = eval(f'self.editAttr{item[0].upper() + item[1:]}.text()').strip()

            if value != '':
                fieldExpressions.append(Util.buildAttributeExpression(item, value))
        return '|'.join(fieldExpressions)

    def _calculateIndexes(self, marker: MarkerDto):
        proc:AbstractMarkerProcessor = MarkerProcessorFactory.buildProcessor(marker, self.model.allTrackPoints)
        return proc.getIndexes()

    def _changeStateAllMarkers(self, value: bool):
        self.markerTreeModel.beginResetModel()
        for item, _ in self.markerTreeModel.iterateAll():
            item:MarkerDto
            item.active = value
            if value:
                item.indexes = self._calculateIndexes(item)
            self.markerActivated.emit(item, value)
            pass
        self.markerTreeModel.endResetModel()
