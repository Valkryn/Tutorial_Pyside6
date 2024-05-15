from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider


def respond_to_slider(data):
    print("slider moved to : ", data)


app = QApplication([])

slider = QSlider(Qt.Vertical)
slider.setMinimum(1)
slider.setMaximum(50)
slider.setValue(25)


slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
