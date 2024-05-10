import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QLabel, QLineEdit, QMainWindow, QPushButton, 
    QDoubleSpinBox, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout
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
        self.course_layout = QVBoxLayout()
        self.courses = []
        course1_input = CourseWidget()
        course2_input = CourseWidget()
        course3_input = CourseWidget()
        course4_input = CourseWidget()
        course5_input = CourseWidget()
        course6_input = CourseWidget()
        course7_input = CourseWidget()
        course8_input = CourseWidget()
        self.courses.append(course1_input)
        self.courses.append(course2_input)
        self.courses.append(course3_input)
        self.courses.append(course4_input)
        self.courses.append(course5_input)
        self.courses.append(course6_input)
        self.courses.append(course7_input)
        self.courses.append(course8_input)

        for c in self.courses:
            self.course_layout.addWidget(c)


        # Calculate GPA and clear grades and credits
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_gpa)
        self.clear_button = QPushButton("Clear")


        # Results label
        self.result_label = QLabel("Result: Your GPA is ")
        h2_font = self.result_label.font()
        h2_font.setPointSize(25)
        self.result_label.setFont(h2_font)


        # Row, column, row span, column span (0, 0, 1, 5)
        # Adding labels to layout
        main_layout.addWidget(title_label, 0, 0, 1, 5)
        main_layout.addWidget(class_label, 1, 0, 1, 4)
        main_layout.addWidget(credits_label, 1, 3, 1, 2)
        main_layout.addWidget(grade_label, 1, 4, 1, 3)
        main_layout.addWidget(self.result_label, 12, 0, 1, 5)


        # Adding courses to layout
        main_layout.addLayout(self.course_layout, 2, 0, 1, 5)


        # Adding buttons to layout
        main_layout.addWidget(self.calculate_button, 3, 1, 2, 2)
        main_layout.addWidget(self.clear_button, 3, 3, 2, 1)


        widget = QWidget()
        widget.setLayout(main_layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
    

    def calculate_gpa(self):
        """Calculate GPA"""
        # Get Credits and Grade
        credits = 0
        grade = 0
        for course in self.courses:
            title = course.coursetitle.text()
            credits = course.creditsinput.value()
            grade = course.gradeinput.currentIndex()
            score = credits * grade
            score_points = score_points + score
            total_credits = total_credits + credits

        # Get GPA
        gpa = score_points / total_credits

        # Display Results
        self.result_label.setText(f"Result: Your GPA is {gpa}")




class CourseWidget(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        hbox = QHBoxLayout()

        self.coursetitle = QLineEdit()
        self.coursetitle.setPlaceholderText("Course Title (Optional)")

        self.creditsinput = QDoubleSpinBox()
        self.creditsinput.setMinimum(0.5)
        self.creditsinput.setMaximum(2)

        self.gradeinput = QComboBox()
        self.gradeinput.addItems(["F", "D", "C", "B", "A"])

        hbox.addWidget(self.coursetitle)
        hbox.addWidget(self.creditsinput)
        hbox.addWidget(self.gradeinput)

        self.setLayout(hbox)






app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()