from typing import TYPE_CHECKING

# Values of modules inside of if above, always in quotes. EX: 'Info'
if TYPE_CHECKING:
    from info import Info
    from display import Display

from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_SIZE
from utils import CHARS, isValidNumber


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
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equationInitialValue = 'Your calculation'
        self.equation = self._equationInitialValue
        self._leftNumber = None
        self._rightNumber = None
        self._operator = None
        self.equation = self._equationInitialValue
        self._readMask()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _readMask(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if buttonText not in CHARS:
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)

                self.slot = self._makeSlot(
                    self._insertButtonTextToDisplay, button)
                self._clickSignal(button, self.slot)

    def _clickSignal(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._clickSignal(button, self._clear)

        if text in '+-/*':
            self._clickSignal(
                button,
                self._makeSlot(self._operatorClicked, button)
            )

        if text in '=':
            self._clickSignal(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):

        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button: Button):
        buttonText = button.text()
        displayText = self.display.text() + buttonText

        if not isValidNumber(displayText):
            return
        self.display.insert(buttonText)

    def _clear(self):
        self._leftNumber = None
        self._rightNumber = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()  # +-/* (etc...)
        displayText = self.display.text()  # _leftNumber
        self.display.clear()  # Clean the display

        # if user clicked on operator but dont clicked in a number before
        if not isValidNumber(displayText) and self._leftNumber is None:
            return

        # if the left number, program waits the right number
        if self._leftNumber is None:
            self._leftNumber = float(displayText)

        self._operator = buttonText
        self.equation = f'{self._leftNumber} {self._operator} ?? '

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber:
            return

        if self._leftNumber is not None and self._operator is None:
            return
        self.display.clear()

        if self._leftNumber and self._operator is not None:

            if self._rightNumber is None:
                self._rightNumber = float(displayText)

            self.equation = f'{self._leftNumber} {self._operator}\
 {self._rightNumber} '

            # WARNING: transform string to command line python, be careful!
            try:
                result = eval(self.equation)
            except ZeroDivisionError:
                self._clear()
                return

            self.info.setText(f'{self.equation} = {result}')

            self._leftNumber = result
            self._operator = None
            self._rightNumber = None

            self.display.setText(str(result))
