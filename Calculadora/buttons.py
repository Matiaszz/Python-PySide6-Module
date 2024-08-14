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
from utils import isNumOrDot, isValidNumber, isEmpty, convertToNumber


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
            ['N', '0', '.', '='],
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
        self.display.delPressed.connect(self._backspace)
        self.display.operatorPressed.connect(self._configLeftOP)
        self.display.inputPressed.connect(self._insertToDisplay)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)

                self.slot = self._makeSlot(
                    self._insertToDisplay, buttonText)
                self._clickSignal(button, self.slot)

    def _clickSignal(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._clickSignal(button, self._clear)

        if text == '◀':
            self._clickSignal(button, self.display.backspace)

        if text == 'N':
            self._clickSignal(button, self._invertNumber)

        if text in '+-/*^':
            self._clickSignal(
                button,
                self._makeSlot(self._configLeftOP, text)
            )

        if text == '=':
            self._clickSignal(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = convertToNumber(displayText) * -1
        self.display.setText(str(number))

    @Slot()
    def _insertToDisplay(self, text):
        displayText = self.display.text() + text

        if not isValidNumber(displayText):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._leftNumber = None
        self._rightNumber = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _configLeftOP(self, text):
        displayText = self.display.text()  # _leftNumber
        self.display.clear()  # Clean the display

        # if user clicked on operator but dont clicked in a number before
        if not isValidNumber(displayText) and self._leftNumber is None:
            self._showError('Nothing in display.')
            return

        # if the left number, program waits the right number
        if self._leftNumber is None:
            self._leftNumber = convertToNumber(displayText)

        self._operator = text
        self.equation = f'{self._leftNumber} {self._operator} ?? '

        self.display.setFocus()

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._leftNumber is None:
            return self._showError('Incomplete calculation.')

        if self._leftNumber is not None and self._operator is None:
            return
        self.display.clear()

        if self._leftNumber and self._operator is not None:

            if self._rightNumber is None:
                self._rightNumber = convertToNumber(displayText)

            self.equation = f'{self._leftNumber} {self._operator}\
 {self._rightNumber} '
            result = 'error'

            try:
                if ('^' in self.equation) and \
                        (isinstance(self._leftNumber, (int, float))):

                    result = math.pow(self._leftNumber, self._rightNumber)
                    result = convertToNumber(str(result))
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

        self.display.setFocus()

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

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _showError(self, textError, title='Error'):
        msgBox = self._makeDialog(textError, title)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, textInfo, title='Info'):
        msgBox = self._makeDialog(textInfo, title)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
