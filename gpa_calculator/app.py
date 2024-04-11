import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GPA Calculator App")

        # Create layouts
        main_layout = QHBoxLayout()

        # Create columns
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()

        # Title label
        title_label = QLabel("GPA Calculator App")
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        # Results label
        result_label = QLabel("Result: Your GPA is ")
        h2_font = result_label.font()
        h2_font.setPointSize(25)
        result_label.setFont(h2_font)


        layout = QVBoxLayout()
        widgets = [
            QComboBox,
            QDoubleSpinBox,
            QLabel,
            QLineEdit,
            QPushButton,
            QSpinBox,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()