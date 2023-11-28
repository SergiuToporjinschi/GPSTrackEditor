import typing, re
import random
from typing import Optional, Union
from PySide6.QtGui import QPalette, QColor, QColorConstants, QValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QColorDialog, QColorDialog, QHeaderView, QMessageBox
from PySide6.QtCore import Qt, QItemSelectionModel, QModelIndex, QItemSelection, QRegularExpression

from .MarkerListDelegate import MarkerListDelegate
from dto import MarkerDto, TrackDataDTO
from abstracts import AbstractModelWidget, AbstractWidgetMaximizeable
from StatusMessage import StatusMessage
from .MarkerStatusModel import MarkerStatusModel
from gui.marking_dock_ui import Ui_DockWidget as markingDock
import pandas as pd
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
        name:str = self.editMarkerName.text()
        if name is None or len(name.strip()) <= 0:
            self.statusMessage.emit(StatusMessage.error('Marker name is mandatory!'))
            return

        expression = self._buildMarkerBaseOnDto(TrackDataDTO)
        if expression is None or len(expression.strip()) <= 0:
            self.statusMessage.emit(StatusMessage.error('Nothing to save there is no expression!'))
            return

        marker = MarkerDto.initFrom('Custom', expression)
        marker.category = 'Custom'
        marker.name = self.editMarkerName.text()
        marker.color = self._generateRandomColor()
        marker.indexes = self._countHits(marker.expression, TrackDataDTO)
        self.markerTreeModel.addRow(marker)

    def _buildMarkerBaseOnDto(self, type: type) -> MarkerDto:
        fields = [item for item in vars(self) if item.startswith('editAttr')][:]
        fieldExpressions = []
        for item in Util.iterateClassPublicAttributes(type, lambda it: it[0] != '_' and f'editAttr{it[0].upper() + it[1:]}' in fields) :
            value = eval(f'self.editAttr{item[0].upper() + item[1:]}.text()').strip()

            if value != '':
                fieldExpressions.append(Util.buildAttributeExpression(item, value))
        return '|'.join(fieldExpressions)

    def _generateRandomColor(self) -> str:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return QColor(red, green, blue).name()

    def _countHits(self, expression: str, type: type):
        cols = Util.getClassPublicAttributes(type)
        objList = [(obj.time,
                obj.latitude,
                obj.longitude,
                obj.altitude,
                obj.hartRate,
                obj.distance,
                obj.calculatedDistance,
                obj.speed,
                obj.calculatedSpeed,
                obj.sensorState) for obj in self.model.allTrackPoints][:]
        df = pd.DataFrame(objList, columns=cols)

        filtered_dfs = df.query(expression)

        return filtered_dfs.index.tolist()