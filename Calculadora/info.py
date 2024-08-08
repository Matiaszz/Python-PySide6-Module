from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from variables import SMALL_SIZE


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(f'font-size: {SMALL_SIZE}')
