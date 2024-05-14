import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Button')
        button = QPushButton("Click Me!")
        button.setCheckable(True)
        button.setChecked(True)
        button.clicked.connect(self.btnclicked)

        self.setCentralWidget(button)

    def btnclicked(self, state):
        print('Button was clicked', state)


app = QApplication([])

window = ButtonHolder()
window.show()

app.exec()
