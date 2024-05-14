import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        btn = QPushButton("Click Me!")
        btn.setCheckable(True)
        btn.clicked.connect(self.btn_clicked)

        self.setCentralWidget(btn)

    def btn_clicked(self, state):
        print('btn was clicked', state)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
