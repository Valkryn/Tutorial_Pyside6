from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        btn1 = QPushButton("Button1")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn1)

        self.setLayout(btn_layout)
