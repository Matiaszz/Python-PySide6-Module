from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout)
from PySide6.QtCore import QThread, QObject, Qt
from window import Ui_myWidget
from time import sleep
import sys


class main(QWidget, Ui_myWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.botao1.clicked.connect(self.hardWork1)
        self.botao2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self.label1.setText('Trabalho 1 iniciado')
        for i in range(3):
            print(i)
            sleep(1)
        self.label1.setText('Trabalho 1 terminado')

    def hardWork2(self):
        self.label1.setText('Trabalho 2 iniciado')
        for i in range(3):
            print(i)
            sleep(1)
        self.label1.setText('Trabalho 2 terminado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgeet = main()

    widgeet.show()
    app.exec()
