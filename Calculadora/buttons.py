from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_SIZE
from utils import CHARS
from display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self.display = display
        self._readMask()

    def _readMask(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)
                if buttonText not in CHARS:
                    button.setProperty('cssClass', 'specialButton')
                self.addWidget(button, i, j)

                self.buttonSlot = self._makeDisplayConnection(
                    self._signal, button)

                button.clicked.connect(self.buttonSlot)

    def _makeDisplayConnection(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _signal(self, button: Button):
        self.display.insert(button.text())
