from PySide6.QtWidgets import QApplication, QMainWindow
from rockwidget import RockWidget
from button import Button

window_titles = [
    'My App',
    'Still My App',
    'What on earth',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle('App Name Goes Here')
        self.setFixedSize(400, 400)

        self.button = Button('Worked?')
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.changeTitle)

    def changeTitle(self):
        self.setWindowTitle(f"Title is now: {window_titles[self.n_times_clicked]}")
        self.n_times_clicked += 1
        self.setFixedSize(600, 600)
        if window_titles == 'Something went wrong':
            self.button.setDisabled(True)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
# 47:45
