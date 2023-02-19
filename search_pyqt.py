from PyQt5.QtWidgets import QWidget, QGridLayout, QCompleter, QLineEdit, QApplication, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.completer = None
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.lineedit = QLineEdit()
        self.layout.addWidget(self.lineedit, 0, 0)

        self.names = ["Apple", "Alps", "Berry", "Cherry"]
        self.new_list = []
        for i in self.names:
            self.new_list.append(i.lower())
        self.completer = QCompleter(self.new_list)
        self.lineedit.textChanged.connect(self.result)
        self.completer.activated.connect(self.tip_balloon)

    def result(self):
        self.lineedit.setCompleter(self.completer)

        text = self.lineedit.text()
        lists = []
        for i in self.new_list:
            a = i.find(text)
            if a >= 0:
                lists.append(i)
        print("result", lists)

    def tip_balloon(self, text):
        print("click", text)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

# names = ["Apple", "Alps", "Berry", "Cherry"]
# lists = []
# for i in names:
#     a = i.find("er")
#     if a >= 0:
#         lists.append(i)
# print(lists)