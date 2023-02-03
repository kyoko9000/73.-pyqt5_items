import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from qtwidgets import Toggle, AnimatedToggle

from gui import Ui_MainWindow
from main import Switch


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        w = Switch()
        toggle_1 = Toggle()
        toggle_2 = AnimatedToggle(
            checked_color="#FFB000",
            pulse_checked_color="#44FFB000"
        )

        layout = QVBoxLayout()
        layout.addWidget(w)
        self.uic.frame.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
