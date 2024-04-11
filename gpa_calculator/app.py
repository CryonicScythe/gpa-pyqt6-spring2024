import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("GPA Calculator App")

        # Create layouts
        main_layout = QHBoxLayout()
        layout = QVBoxLayout()


        # Create 3 columns
        left_pane = QVBoxLayout()
        middle_pane = QVBoxLayout()
        right_pane = QVBoxLayout()


        # Labels
        title_label = QLabel("GPA Calculator App")
        result_label = QLabel("Result: Your GPA is ")




        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()