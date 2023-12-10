import re, enum
import pandas as pd
from pandas.errors import UndefinedVariableError
from typing import Union
from PySide6.QtGui import QColor, QColorConstants
from PySide6.QtWidgets import QHeaderView, QMessageBox
from PySide6.QtCore import Qt, QItemSelectionModel, QModelIndex, QItemSelection
from qtpy.QtCore import Signal

from config import *
from dto import MarkerDto, MarkerCategory, MarkerGroupDto
from abstracts import AbstractModelWidget, AbstractWidgetMaximizable, FrameState
from StatusMessage import StatusMessage
from .MarkerListDelegate import MarkerListDelegate
from .MarkerStatusModel import MarkerStatusModel
from .MarkerProcessor import MarkerProcessorFactory, AbstractMarkerProcessor
import UtilFunctions as Util
from gui.marking_dock_ui import Ui_DockWidget as markingDock

log = Util.initLogging()

class RecordAction(enum.Enum):
    Changed = 0
    Add = 1
    Remove = 2

class MarkerRecordSelectionModel(QItemSelectionModel):
    def __init__(self, model):
        super().__init__(model)

    def select(self, selection: Union[QItemSelection, QModelIndex], command : QItemSelectionModel.SelectionFlag):
        if isinstance(selection, QItemSelection):
            newSelection = QItemSelection()
            selected_indexes = selection.indexes()
            for index in selected_indexes:
                if isinstance(index.internalPointer(), MarkerDto): newSelection.select(index,index)
            super().select(newSelection, command)  # Allow selection for other rows
            return
        else:
            if not isinstance(selection.internalPointer(), MarkerDto):
                return

        super().select(selection, command)  # Allow selection for other rows

class MarkingDockWidget(AbstractModelWidget, AbstractWidgetMaximizable, markingDock):
    colorCustomMarking:QColor = QColorConstants.Red
    colorStationaryMarking: QColor = QColorConstants.Yellow
    markers : [MarkerDto] = []

    def _setupUi(self):
        self.pushAdd.clicked.connect(self._onAddSaveMarker)
        self.treeViewMarker.setItemDelegate(MarkerListDelegate())

        self.markerTreeModel = MarkerStatusModel(self)
        self.treeViewMarker.setModel(self.markerTreeModel)

        # dataChanged (index, index, roles)
        self.markerTreeModel.dataChanged.connect(self._applyChangeMarker)

        # insert/delete row (parentIndex, poz, poz)
        self.markerTreeModel.rowsInserted.connect(lambda pIndex, pozFrom, pozTo: self._applyAddRemoveMarker(pIndex, pozFrom, pozTo, RecordAction.Add))
        self.markerTreeModel.rowsAboutToBeRemoved.connect(lambda pIndex, pozFrom, pozTo: self._applyAddRemoveMarker(pIndex, pozFrom, pozTo, RecordAction.Remove))

        self._resizeHeader(self.treeViewMarker.header())

        self.treeViewMarker.expandAll()
        self.toolEdit.clicked.connect(self._editMarker)
        self.toolDelete.clicked.connect(self._onDelete)
        self.toolActivateAll.clicked.connect(lambda: self._changeStateAllMarkers(True))
        self.toolClearAll.clicked.connect(lambda: self._changeStateAllMarkers(False))

        self.treeViewMarker.setSelectionModel(MarkerRecordSelectionModel(self.markerTreeModel))
        self.markerTreeModel.modelReset.connect(self.treeViewMarker.expandAll)

        self.pushCancelEdit.clicked.connect(lambda:  self.setState(FrameState.View))
        self.treeViewMarker.selectionModel().selectionChanged.connect(lambda sel, deSel: self.toolEdit.setEnabled(len(self.treeViewMarker.selectionModel().selectedRows()) == 1))
        self.treeViewMarker.selectionModel().selectionChanged.connect(lambda sel, deSel: self.toolDelete.setEnabled(len(self.treeViewMarker.selectionModel().selectedRows()) > 0))

        self.model.mainSeriesChanged.connect(lambda: self._changeStateAllMarkers(False))
        pass

    def _resizeHeader(self, header:QHeaderView):
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

    def _onDelete(self):
        currentSelection:QItemSelectionModel = self.treeViewMarker.selectionModel()
        item = currentSelection.currentIndex().internalPointer()
        countSelected = len([selIndex.row() for selIndex in currentSelection.selectedIndexes() if selIndex.column() == 0][:])
        confirmation = QMessageBox.question(
            None, 'Delete', f'Are you sure you want to delete {item.name if countSelected == 1 else countSelected} marker(s)?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        )
        if confirmation == QMessageBox.StandardButton.No: return

        selectionModel = self.markerTreeModel

        for indexToDelete in reversed(currentSelection.selectedRows(0)):
            parentIndex = selectionModel.parent(indexToDelete)
            selectionModel.removeRow(indexToDelete.row(), parentIndex)
            # self.markerActivated.emit(indexToDelete.internalPointer(), False)

    def _editMarker(self):
        index = self.treeViewMarker.selectionModel().currentIndex()
        item:MarkerDto = index.internalPointer()
        for tabIndex in range(self.tabWidget.count()):
            if self.tabWidget.widget(tabIndex).property('markerCategory') == item.category.name:
                self.tabWidget.setCurrentIndex(tabIndex)
                break

        self.editMarkerName.setText(item.name)
        if item.category == MarkerCategory.Custom:
            self.editCustomColExpression.setText(item.expression)

        elif item.category == MarkerCategory.Stationary:
            found = re.search(r'\b(\d+\.\d+)?$', item.expression)
            self.spinBoxStatTolerance.setValue(float(found.group(0)) if found else float(0))

        self.pushAdd.setText('Save')
        self.state = FrameState.Edit

    def _onAddSaveMarker(self):
        name:str = self.editMarkerName.text()
        markerCategory = MarkerCategory.fromString(self.tabWidget.currentWidget().property('markerCategory'))

        if markerCategory == MarkerCategory.Custom:
            expression = self.editCustomColExpression.text()
        else:
            expression = f'distanceDifference >= 0 and distanceDifference <= {self.spinBoxStatTolerance.value()}'

        marker = MarkerDto.initFrom(name, markerCategory, expression)

        if self.state == FrameState.View:
            if not self._isValid(marker): return

            try:
                marker.indexes = self._calculateIndexes(marker)
            except (UndefinedVariableError, TypeError, SyntaxError, ValueError) as err:
                self.statusMessage.emit(StatusMessage.error(f'{err.args[0]}'))
                return

            self.markerTreeModel.addMarker(marker)

        elif self.state == FrameState.Edit:
            if not self._isValid(marker): return

            index = self.treeViewMarker.selectionModel().currentIndex()
            self.markerTreeModel.setData(index, marker, Qt.ItemDataRole.UserRole)

            self.state = FrameState.View
            self.pushAdd.setText('Add')

    def _isValid(self, item:MarkerDto) -> bool:
        if item.name is None or len(item.name.strip()) <= 0:
            self.statusMessage.emit(StatusMessage.error('Marker name is mandatory!'))
            return False

        if item.expression is None or len(item.expression.strip()) <= 0:
            self.statusMessage.emit(StatusMessage.error('Nothing to save, there is no expression!'))
            return False

        if self.isViewMode():
            if not self._isValidMarkerName(item.name):
                self.statusMessage.emit(StatusMessage.error('Marker name must be unique!'))
                return False

        elif self.isEditMode():
            index = self.treeViewMarker.selectionModel().currentIndex()
            foundIndexes = self.markerTreeModel.match(index.parent(), Qt.ItemDataRole.DisplayRole, item.name, -1, Qt.MatchFlag.MatchRecursive | Qt.MatchFlag.MatchFixedString | Qt.MatchFlag.MatchWrap | Qt.MatchFlag.MatchCaseSensitive)
            for ind in foundIndexes:
                if index.internalId() == ind.internalId(): foundIndexes.remove(ind)

            if len(foundIndexes) > 0:
                self.statusMessage.emit(StatusMessage.error('Another marker with the same already exists!!'))
                return

        if item.category == MarkerCategory.Custom:
            pass

        elif item.category == MarkerCategory.Stationary:
            tolerance = self.spinBoxStatTolerance.value()
            if not tolerance or tolerance is None:
                self.statusMessage.emit(StatusMessage.error('Marker name must be unique!'))
                return False
            pass
        return True

    def _isValidMarkerName(self, name:str):
        for item, _ in self.markerTreeModel.iterateAll():
            item:MarkerDto
            if name == item.name:
                return False
        return True

    def _calculateIndexes(self, marker: MarkerDto, saveIndex:bool = False):
        proc:AbstractMarkerProcessor = MarkerProcessorFactory.buildProcessor(marker, self.model.allTrackPoints)
        indexes = proc.getIndexes()
        if saveIndex:
            marker.indexes = indexes
        return indexes

    def testItsem(self, item):
        from dto import MarkerDto
        item: MarkerDto

        m = pd.DataFrame({'Color': [item.color], 'Indexes': [item.indexes], 'Id': [item.id]})
        self.r = pd.concat([self.r ,m])
        print(self.r)
        # selectedColor = self.r[self.r['Indexes'].apply(lambda x: 3 in x)]
        # selectedColor['Color'].iloc[-1]
        pass

    def testRIstem(self, item):
        from dto import MarkerDto
        item: MarkerDto

        self.r = self.r[self.r['Id'] != item.id]
        print(self.r)
        # selectedColor = self.r[self.r['Indexes'].apply(lambda x: 3 in x)]
        # selectedColor['Color'].iloc[-1]
        pass

    def _changeStateAllMarkers(self, value: bool):
        self.r = pd.DataFrame([], columns=['Color','Indexes','Id'])
        log.debug(f'{"Check" if value else "Uncheck"} all markers!')
        self.markerTreeModel.beginResetModel()
        items = []
        for item, _ in self.markerTreeModel.iterateAll():
            item:MarkerDto
            item.active = value
            if value:
                self._calculateIndexes(item, True)
                self.model.addMarker(item)
                items.append(item)
            else:
                item.indexes = []
                self.model.removeMarker(item)

        self.markerTreeModel.endResetModel()
        # Util.test(items)

    # dataChanged (index, index, roles)
    def _applyChangeMarker(self, indexFrom: QModelIndex, indexTo: QModelIndex, role: list[Qt.ItemDataRole], action: RecordAction = RecordAction.Changed):
        item:MarkerDto = indexFrom.internalPointer()
        if Qt.ItemDataRole.CheckStateRole in role: #activate or deactivate
            if item.active: #add
                self._calculateIndexes(item, True)
                self.model.addMarker(item)
            else: # remove
                self.model.removeMarker(item)

        elif item.active and len(list(set(role) & set((Qt.ItemDataRole.UserRole, Qt.ItemDataRole.EditRole)))) > 0: #change color, expression or name
            self._calculateIndexes(item, True)
            self.model.changeMarker(item)
            pass

    # insert/delete row (parentIndex, poz, poz)
    def _applyAddRemoveMarker(self, pIndex: QModelIndex, pFrom: int, pTo: int, action: RecordAction):
        pItem:MarkerGroupDto = pIndex.internalPointer()
        item:MarkerDto = pItem.markers[pFrom]

        if item.active and action == RecordAction.Add: # add
            self._calculateIndexes(item, True)
            self.model.addMarker(item)
        elif item.active and action == RecordAction.Remove: # remove
            self.model.removeMarker(item)
        pass