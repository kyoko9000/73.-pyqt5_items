# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
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
        shadow.setColor(QColor(63, 63, 63, 180))
        shadow.setOffset(5, 5)

        # setting blur radius
        # shadow.setBlurRadius(15)

        # adding shadow to the label
        label.setGraphicsEffect(shadow)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
