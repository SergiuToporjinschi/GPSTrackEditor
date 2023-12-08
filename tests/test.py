from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLabel, QWidget

class HelpExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Create a QPushButton
        self.button = QPushButton("Help Button")
        self.button.setToolTip("Click this button to see help information")

        # Set the 'whatsthis' property for the button (help text)
        self.button.whatsthis = "This button provides help information when clicked."

        # Create a QLabel to display help text
        self.help_label = QLabel("Hover over the button and click 'What's This?' to see help text.")
        self.help_label.setWordWrap(True)

        layout.addWidget(self.button)
        layout.addWidget(self.help_label)

        # Connect button clicked event to show_help_text method
        self.button.clicked.connect(self.show_help_text)

    def show_help_text(self):
        # Get the help text from the 'whatsthis' property of the button
        help_text = self.button.whatsthis

        # Update the QLabel to display the help text
        self.help_label.setText(f"Help Text: {help_text}")

if __name__ == "__main__":
    app = QApplication([])

    # Create and show the main window
    window = HelpExample()
    window.show()

    app.exec()
