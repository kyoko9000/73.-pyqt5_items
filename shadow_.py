# importing libraries
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QMainWindow, QLabel, QGraphicsDropShadowEffect, QApplication


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
        # calling method

        # creating label
        label = QLabel("Label", self)
        # setting font and size
        label.setFont(QFont('Arial', 100))
        # setting alignment
        label.setAlignment(Qt.AlignCenter)
        # setting geometry to the label
        label.setGeometry(50, 20, 400, 300)
        # setting border
        label.setStyleSheet("border : 10px solid black")

        # creating a QGraphicsDropShadowEffect object
        shadow = QGraphicsDropShadowEffect()
        # set color for shadow
        shadow.setColor(QColor(63, 63, 63, 180))
        # set offset for shadow
        shadow.setOffset(5, 5)
        # setting blur radius
        # shadow.setBlurRadius(15)
        # adding shadow to the label
        label.setGraphicsEffect(shadow)


# create pyqt5 app
App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())
