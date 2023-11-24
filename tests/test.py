from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView,  QStyledItemDelegate, QStyleOptionButton, QStyle
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

class RadioDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        checked = index.data(Qt.CheckStateRole)
        if checked == Qt.Checked:
            radio_state = "checked"
        elif checked == Qt.Unchecked:
            radio_state = "unchecked"
        else:
            radio_state = "none"

        style = QApplication.style()
        QStyle.ControlElement.CE_RadioButton
        style.drawControl(QStyle.ControlElement.CE_RadioButton, self.getRadioButtonStyle(option, radio_state), painter)

    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                model.setData(index, Qt.Checked, Qt.CheckStateRole)
        return True

    def getRadioButtonStyle(self, option, state):
        opt = QStyleOptionButton()
        opt.state |= QStyle.State_Enabled
        if state == "checked":
            opt.state |= QStyle.State_On
        elif state == "unchecked":
            opt.state |= QStyle.State_Off
        opt.rect = option.rect
        opt.palette = option.palette
        return opt


# Example usage:
app = QApplication([])

main_window = QMainWindow()

tree_view = QTreeView(main_window)
model = QStandardItemModel()
tree_view.setModel(model)

delegate = RadioDelegate(tree_view)
tree_view.setItemDelegate(delegate)

root_item = QStandardItem("Root")

for i in range(5):
    parent_item = QStandardItem(f"Parent {i}")

    for j in range(3):
        child_item = QStandardItem(f"Child {j}")
        child_item.setCheckable(True)
        parent_item.appendRow(child_item)

    root_item.appendRow(parent_item)

model.appendRow(root_item)

tree_view.expandAll()
main_window.setCentralWidget(tree_view)
main_window.show()

app.exec()
