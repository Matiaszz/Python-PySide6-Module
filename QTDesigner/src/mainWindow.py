from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from typing import cast

import sys


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.confirmButton.clicked.connect(self._changeLabelResult)

        self.inputName.installEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:

            # troca o tipo da variavel
            event = cast(QKeyEvent, event)

            text = self.inputName.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)

    def _changeLabelResult(self):
        text = self.inputName.text()

        if not text.split():
            return

        self.labelResult.setText(text)
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()

    window.show()
    app.exec()
