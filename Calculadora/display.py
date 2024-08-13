from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from variables import BIG_SIZE, TEXT_MARGIN, MIN_WIDTH
from utils import isEmpty


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size:{BIG_SIZE}px;')
        self.setMinimumHeight(BIG_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        self.setMinimumWidth(MIN_WIDTH)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        text = event.text().strip()

        KEYS = Qt.Key
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isESC = key in [KEYS.Key_Escape, KEYS.Key_C]

        if isEnter:
            self.eqPressed.emit()
            event.ignore()

        if isDelete:
            self.delPressed.emit()
            event.ignore()

        if isESC:
            self.clearPressed.emit()
            event.ignore()

        if isEmpty(text):
            return event.ignore()

        print('key:', text)
