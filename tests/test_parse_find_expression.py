from PySide6.QtWidgets import QApplication, QTreeView, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QSpinBox, QStyledItemDelegate
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QFile, QIODevice, QModelIndex
import sys
import json

class JsonEditor(QWidget):
    def __init__(self, json_data):
        super().__init__()
        self.setWindowTitle("JSON Editor")
        self.setGeometry(100, 100, 400, 400)

        self.json_data = json_data

        # Create a QTreeView with two columns
        self.tree_view = QTreeView()
        self.model = QStandardItemModel()
        self.model.setColumnCount(5)  # Set the column count to 2
        self.tree_view.setModel(self.model)

        # Populate the tree view based on JSON data
        self.populate_treeview2(self.model.invisibleRootItem(), self.json_data)
        self.tree_view.expanded.connect(self.test)
        # Set headers for columns
        # self.tree_view.setHeaderLabels(['Attribute', 'Value'])

        # Set custom delegate to allow for custom widgets within the tree
        # self.tree_view.setItemDelegate(TreeDelegate(self))

        # Add tree view to layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tree_view)
        self.setLayout(main_layout)
    def test(self, x):
        self.tree_view.rowHeight(x)
        self.tree_view.font().
        pass
    def populate_treeview2(self, parent: QStandardItem, data, p:QStandardItem=None):
        columns = ['min', 'avg', 'max', 'missing']
        if isinstance(data, dict):
            for key, value in data.items():
                if key in columns:
                    p.setChild(parent.row(), columns.index(key) + 1, QStandardItem(str(value)))
                    continue
                else:
                    item = QStandardItem(str(key))
                    parent.appendRow(item)
                    if isinstance(value, dict):
                        self.populate_treeview2(item, value, parent)

    def populate_treeview(self, parent: QStandardItem, data):
        if isinstance(data, dict):
            for key, value in data.items():
                item = QStandardItem(str(key))
                parent.appendRow(item)
                if isinstance(value, dict):
                    self.populate_treeview(item, value)
                else:
                    item2 = QStandardItem(str(value))
                    if isinstance(value, int):
                        item2.customType = int
                    if isinstance(value, str):
                        item2.customType = str
                    parent.setChild(item.row(), 1, item2)  # Add value to the second column

class TreeDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        if index.column() == 1:  # Only create editor for the second column
            value = index.model().data(index, Qt.ItemDataRole.EditRole)
            if isinstance(value, str):
                editor = QSpinBox(parent)
                return editor
            elif isinstance(value, int):
                editor = QSpinBox(parent)
                return editor
            elif isinstance(value, list):
                editor = QComboBox(parent)
                editor.addItems(value)  # For simplicity, adding list items to a combo box
                return editor
        return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.ItemDataRole.DisplayRole)
        if isinstance(value, str):
            editor.setText(value)
        elif isinstance(value, int):
            editor.setValue(value)
        elif isinstance(value, list):
            # No need to set data for combo box
            pass
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        value = editor.text() if isinstance(editor, QLineEdit) else editor.currentText() if isinstance(editor, QComboBox) else editor.value() if isinstance(editor, QSpinBox) else None
        if value is not None:
            model.setData(index, value, Qt.ItemDataRole.DisplayRole)
        else:
            super().setModelData(editor, model, index)

def _getResourceContent(resourceFilePath: str):
    htmlContent = ""
    html_resource = QFile(resourceFilePath)
    if html_resource.open(QIODevice.ReadOnly | QIODevice.Text):
        html_content = html_resource.readAll().data().decode('utf-8')
        htmlContent = html_content
        html_resource.close()
    return htmlContent

def main():
    app = QApplication(sys.argv)

    # JSON data

    data = json.loads(_getResourceContent("E:/IOT/Projects/Python/GPSTrackEditor/resources/statisticTreeStructure.json"))
    editor = JsonEditor(data)
    editor.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()