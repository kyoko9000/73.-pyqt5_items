import sys

from PyQt5 import QtCore, QtPrintSupport, QtGui
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.frame.setGeometry(QtCore.QRect(10, 10, 500, 300))
        self.button = QPushButton("button")
        self.button.clicked.connect(self.to_pdf)

        self.w = QTableWidget(10, 10)
        it = QTableWidgetItem("hi")
        self.w.setItem(1, 3, it)
        it = QTableWidgetItem("44. hi")
        self.w.setItem(5, 2, it)

        layout = QVBoxLayout()
        layout.addWidget(self.w)
        layout.addWidget(self.button)
        self.uic.frame.setLayout(layout)

    def to_pdf(self):
        filename = "table.pdf"
        model = self.w.model()

        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setPaperSize(QtPrintSupport.QPrinter.A4)
        printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
        printer.setOutputFileName(filename)

        doc = QtGui.QTextDocument()

        html = """<html>
        <head>
        <style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;
        }
        </style>
        </head>"""
        html += "<table><thead>"
        html += "<tr>"
        for c in range(model.columnCount()):
            html += "<th>{}</th>".format(model.headerData(c, QtCore.Qt.Horizontal))

        html += "</tr></thead>"
        html += "<tbody>"
        for r in range(model.rowCount()):
            html += "<tr>"
            for c in range(model.columnCount()):
                html += "<td>{}</td>".format(model.index(r, c).data() or "")
            html += "</tr>"
        html += "</tbody></table>"
        doc.setHtml(html)
        doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
        doc.print_(printer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())