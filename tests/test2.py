from PySide6.QtCore import QTimer, QCoreApplication

# Function to be executed after a delay
def delayed_action():
    print("Delayed action executed")

# Create a QTimer instance
timer = QTimer()

# Connect the timeout signal of the timer to the delayed_action function
timer.timeout.connect(delayed_action)

# Set the interval (in milliseconds) for the timer
delay_in_seconds = 2  # 2 seconds
timer.start(delay_in_seconds * 1000)  # QTimer works in milliseconds

# Start the application event loop
app = QCoreApplication([])

# Here, you can start your application logic...
# For demonstration purposes, we'll wait for the timer to complete
QCoreApplication.processEvents()