from PyQt5.QtWidgets import QWidget, QGridLayout, QCompleter, QLineEdit, QApplication
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.completer = None
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # create lineedit
        self.lineedit = QLineEdit()
        self.layout.addWidget(self.lineedit, 0, 0)

        # make a list
        self.names = ["Apple", "Alps", "Berry", "Cherry"]
        # new list with lowercase
        self.new_list = []
        for i in self.names:
            self.new_list.append(i.lower())
        # create completer
        self.completer = QCompleter(self.new_list)
        # action after put text
        self.lineedit.textChanged.connect(self.result)
        # action after click text
        self.completer.activated.connect(self.tip_balloon)

    def result(self):
        # set up completer
        self.lineedit.setCompleter(self.completer)
        # search text by "find" function
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
#     a = i.find("A")
#     if a >= 0:
#         lists.append(i)
# print(lists)