from typing import TYPE_CHECKING

# Values of modules inside of if above, always in quotes. EX: 'Info'
if TYPE_CHECKING:
    from info import Info
    from display import Display
    from main_window import Window

import math
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
    def __init__(self, display: 'Display', info: 'Info', window: 'Window',
                 *args, **kwargs):
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
        self.window = window
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
        self.display.eqPressed.connect(self._eq)
        self.display.clearPressed.connect(self._clear)
        self.display.delPressed.connect(self.display.backspace)

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

        if text == '◀':
            self._clickSignal(button, self.display.backspace)

        if text in '+-/*^':
            self._clickSignal(
                button,
                self._makeSlot(self._operatorClicked, button)
            )

        if text == '=':
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
            self._showError('Nothing in display.')
            return

        # if the left number, program waits the right number
        if self._leftNumber is None:
            self._leftNumber = float(displayText)

        self._operator = buttonText
        self.equation = f'{self._leftNumber} {self._operator} ?? '

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return self._showError('Incomplete calculation.')

        if self._leftNumber is not None and self._operator is None:
            return
        self.display.clear()

        if self._leftNumber and self._operator is not None:

            if self._rightNumber is None:
                self._rightNumber = float(displayText)

            self.equation = f'{self._leftNumber} {self._operator}\
 {self._rightNumber} '
            result = 'error'

            try:
                if ('^' in self.equation) and \
                        (isinstance(self._leftNumber, float)):

                    result = math.pow(self._leftNumber, self._rightNumber)
                    self.info.setText(f'{self.equation} = {result}')
                else:
                    result = eval(self.equation)
            # WARNING: transform string to command line python, be careful!
            except ZeroDivisionError:
                self._clear()
                return self._showError('Impossible to divise by zero.')

            except OverflowError:
                self._clear()
                return self._showError('Impossible to calculate.')

            self.info.setText(f'{self.equation} = {result}')

            self._leftNumber = result
            self._operator = None
            self._rightNumber = None

            if result == 'error':
                self._leftNumber = None

    def _makeDialog(self, text, title):
        msgBox = self.window.makeMsgBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setStandardButtons(msgBox.StandardButton.Ok)  # Generic icons

        # # how to create others buttons on error case:
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.Ok  # | msgBox.StandardButton.Cancel
        # )
        return msgBox

    def _showError(self, textError, title='Error'):
        msgBox = self._makeDialog(textError, title)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()

    def _showInfo(self, textInfo, title='Info'):
        msgBox = self._makeDialog(textInfo, title)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
