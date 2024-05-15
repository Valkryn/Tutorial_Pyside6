from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from rockwidget import RockWidget
from button import Button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('App Name Goes Here')
        self.setMaximumSize(800, 800)

        my_button = Button('Worked?')
        self.setCentralWidget(my_button)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
# 47:45
