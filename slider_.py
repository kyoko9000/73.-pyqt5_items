import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.horizontalSlider.valueChanged.connect(self.changevalue)

    def changevalue(self):
        values = self.uic.horizontalSlider.value()
        print(values)
        self.uic.label.setText(str(values))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())