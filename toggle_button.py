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

        toggle = Switch()
        toggle.clicked.connect(self.hh)

        toggle_1 = Toggle()
        toggle_2 = AnimatedToggle(
            checked_color="#FFB000",
            pulse_checked_color="#44FFB000"
        )
        toggle_2.clicked.connect(self.hh1)

        layout = QVBoxLayout()
        layout.addWidget(toggle)
        self.uic.frame.setLayout(layout)

        layout1 = QVBoxLayout()
        layout1.addWidget(toggle_2)
        self.uic.frame_2.setLayout(layout1)

    def hh(self, emitted):
        print(emitted)

    def hh1(self, emitted):
        print(emitted)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
