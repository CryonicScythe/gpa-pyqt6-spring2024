import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QLabel, QLineEdit, QMainWindow, QPushButton, QDoubleSpinBox, QWidget, QHBoxLayout, QGridLayout
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("GPA Calculator App")


        # Create layouts
        main_layout = QGridLayout()


        # Title label
        title_label = QLabel("GPA Calculator App")
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)


        # Course labels
        class_label = QLabel("Class")
        class_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        credits_label = QLabel("Credits")
        credits_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        grade_label = QLabel("Grade")
        grade_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        # Course widgets
        self.course1_input = CourseWidget()
        self.course2_input = CourseWidget()
        self.course3_input = CourseWidget()
        self.course4_input = CourseWidget()
        self.course5_input = CourseWidget()
        self.course6_input = CourseWidget()
        self.course7_input = CourseWidget()
        self.course8_input = CourseWidget()


        # Results label
        result_label = QLabel("Result: Your GPA is ")
        h2_font = result_label.font()
        h2_font.setPointSize(25)
        result_label.setFont(h2_font)


        # Row, column, row span, column span (0, 0, 1, 5)
        # Adding labels to layout
        main_layout.addWidget(title_label, 0, 0, 1, 5)
        main_layout.addWidget(class_label, 1, 0, 1, 4)
        main_layout.addWidget(credits_label, 1, 3, 1, 2)
        main_layout.addWidget(grade_label, 1, 4, 1, 3)


        # Adding courses to layout
        main_layout.addWidget(self.course1_input, 2, 0, 1, 5)
        main_layout.addWidget(self.course2_input, 3, 0, 1, 5)
        main_layout.addWidget(self.course3_input, 4, 0, 1, 5)
        main_layout.addWidget(self.course4_input, 5, 0, 1, 5)
        main_layout.addWidget(self.course5_input, 6, 0, 1, 5)
        main_layout.addWidget(self.course6_input, 7, 0, 1, 5)
        main_layout.addWidget(self.course7_input, 8, 0, 1, 5)
        main_layout.addWidget(self.course8_input, 9, 0, 1, 5)


        widget = QWidget()
        widget.setLayout(main_layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)



class CourseWidget(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        hbox = QHBoxLayout()

        self.coursetitle = QLineEdit()
        self.coursetitle.setPlaceholderText("Course Title (Optional)")

        self.creditsinput = QDoubleSpinBox()
        self.creditsinput.setMinimum(0)
        self.creditsinput.setMaximum(2)

        self.gradeinput = QComboBox()
        self.gradeinput.addItems(["A", "B", "C", "D", "F"])

        hbox.addWidget(self.coursetitle)
        hbox.addWidget(self.creditsinput)
        hbox.addWidget(self.gradeinput)

        self.setLayout(hbox)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()