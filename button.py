from PySide6.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, title):
        super().__init__(title)

        self.setCheckable(True)
        self.setChecked(False)

        self.clicked.connect(self.button_pressed)

    def button_pressed(self, state):
        print('You clicked the button!! : Also, this is the state of the button:  ', state)
