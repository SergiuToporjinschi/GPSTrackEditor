from PySide6.QtWidgets import QDockWidget, QHeaderView
from PySide6.QtCore import Qt, QItemSelection
from qtpy.QtCore import Signal

from gui.processing_dock_ui import Ui_DockWidget as processingDock
from abstracts import AbstractModelWidget, FrameState
from modules.processing.CalcColumnModel import CalcColumnModel
from dto import CalcColumnDto
from StatusMessage import StatusMessage
from validators import MethodNameValidator

class ProcessingDockWidget(AbstractModelWidget, QDockWidget, processingDock):
    processingCalculatedColumnsChanged = Signal(list)

    def _setupUi(self):
        self.modelCol = CalcColumnModel()

        self.processingCalculatedColumnsChanged.connect(self.model.updateCalculatedColumns)
        self.modelCol.dataChanged.connect(self._calculatedColumnsChanged)
        self.modelCol.rowsInserted.connect(self._calculatedColumnsChanged)
        self.modelCol.rowsRemoved.connect(self._calculatedColumnsChanged)

        self.tableViewCol.setModel(self.modelCol)
        self.modelCol.modelReset.connect(self.tableViewCol.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch))

        self.pushButtonAddColumn.clicked.connect(self._saveColumn)
        self.toolButtonEdit.clicked.connect(self._editColumn)
        self.toolButtonDelete.clicked.connect(self._deleteColumns)
        self.toolButtonActivateAll.clicked.connect(lambda :self._activeAll(True))
        self.toolButtonDeactivateAll.clicked.connect(lambda :self._activeAll(False))

        self.stateChanged.connect(lambda state: self.pushButtonAddColumn.setText( 'Add column' if state == FrameState.View else 'Save column'))
        self.pushButtonCancelEdit.clicked.connect(lambda:  self.setState(FrameState.View))

        self.tableViewCol.selectionModel().selectionChanged.connect(lambda sel, deSel: self.toolButtonEdit.setEnabled(len(self.tableViewCol.selectionModel().selectedRows()) == 1))
        self.tableViewCol.selectionModel().selectionChanged.connect(lambda sel, deSel: self.toolButtonDelete.setEnabled(len(self.tableViewCol.selectionModel().selectedRows()) > 0))
        self.buttonShiftTime.clicked.connect(self.test)

        self.lineEditName.setValidator(MethodNameValidator())

    def test(self):
        self.model.allTrackPoints.to_clipboard()

    def _selChanged(self, prev:QItemSelection, next:QItemSelection):
        isOneSelected = len(self.tableViewCol.selectionModel().selectedRows()) == 1
        self.toolButtonEdit.setEnabled(isOneSelected)
        self.toolButtonDelete.setEnabled(isOneSelected)

    def _deleteColumns(self):
        indexes = self.tableViewCol.selectionModel().selectedRows()
        cols = []
        for index in reversed(indexes):
            cols.append(self.modelCol.data(index, Qt.ItemDataRole.UserRole).name)
            self.modelCol.removeRow(index.row())

    def _editColumn(self):
        selectionIndex = self.tableViewCol.selectionModel().selectedRows()
        if selectionIndex is None or len(selectionIndex) <= 0:
            return

        item:CalcColumnDto = self.modelCol.data(selectionIndex[0], Qt.ItemDataRole.UserRole)
        self.lineEditName.setText(item.name)
        self.lineEditExpression.setText(item.expression)
        self.state = FrameState.Edit

    def _saveColumn(self):
        title = self.lineEditName.text()
        exp = self.lineEditExpression.text()

        # Add column
        if self.isViewMode():
            item = CalcColumnDto(title, exp, True)
            if not self._isValidColumn(item): return

            self.modelCol.addCalcColumn(item)

        # save column
        elif self.isEditMode():
            index = self.tableViewCol.selectionModel().currentIndex()

            item:CalcColumnDto = self.modelCol.data(index, Qt.ItemDataRole.UserRole)
            newItem = CalcColumnDto(title, exp, item.active)

            if not self._isValidColumn(newItem): return

            self.modelCol.setData(index, newItem, Qt.ItemDataRole.UserRole)

            self.state = FrameState.View
        pass

    def _isValidColumn(self, item: CalcColumnDto):
        if not len(item.expression.strip()) > 0 or not len(item.name.strip()) > 0:
            self.statusMessage.emit(StatusMessage.error('Name and expression are mandatory!'))
            return False

        if self.isViewMode():
            if self.modelCol.hasColumn(item.name):
                self.statusMessage.emit(StatusMessage.error('Another column with the same already exists!!'))
                return False

        elif self.isEditMode():
            index = self.tableViewCol.selectionModel().currentIndex()
            foundIndexes = self.modelCol.match(self.modelCol.index(0,0), Qt.ItemDataRole.DisplayRole, item.name, -1, Qt.MatchFlag.MatchFixedString | Qt.MatchFlag.MatchWrap | Qt.MatchFlag.MatchCaseSensitive)
            if index in foundIndexes: foundIndexes.remove(index)
            if len(foundIndexes) > 0:
                self.statusMessage.emit(StatusMessage.error('Another column with the same already exists!!'))
                return

        try:
            self.model.getCalcColumnExpression(item)
            return True
        except (AttributeError, NameError) as err:
            self.statusMessage.emit(StatusMessage.error(f'{err.name}: {err.args[0]}'))
        return False

    def _activeAll(self, isActive: bool):
        for item, index in self.modelCol.iterateAll():
            item.active = isActive
            self.modelCol.setData(index, item, Qt.ItemDataRole.UserRole)
            pass

    def _calculatedColumnsChanged(self):
        activeColumns = []
        cnt = self.modelCol.rowCount()
        for i in range(cnt):
            index = self.modelCol.index(i, 0)
            item:CalcColumnDto = self.modelCol.data(index, Qt.ItemDataRole.UserRole)
            if not item.active: continue
            activeColumns.append(item)
        self.processingCalculatedColumnsChanged.emit(activeColumns)
        pass

