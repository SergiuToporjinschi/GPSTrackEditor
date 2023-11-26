from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView,  QPushButton, QWidget, QVBoxLayout, QStyledItemDelegate
from PySide6.QtCore import Qt, QAbstractItemModel
from PySide6.QtGui import  QStandardItemModel, QStandardItem

class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        if index.column() == 0:  # Replace '1' with the column number where you want the button
            button = QPushButton("Click Me", parent)
            return button
        return super().createEditor(parent, option, index)

# Example usage:
app = QApplication([])

main_window = QMainWindow()

tree_view = QTreeView(main_window)
model = QStandardItemModel()
tree_view.setModel(model)

delegate = ButtonDelegate(tree_view)
tree_view.setItemDelegate(delegate)

root_item = QStandardItem("Root")
child_item1 = QStandardItem("Child 1")
child_item2 = QStandardItem("Child 2")

model.appendRow(root_item)
root_item.appendRow([child_item1, child_item2])

main_window.setCentralWidget(tree_view)
main_window.show()

app.exec()