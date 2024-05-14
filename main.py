from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
from button import ButtonHolder
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ExPDF")
        btn = QPushButton("Click Me!")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 600)
        self.setCentralWidget(btn)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()

#47:45