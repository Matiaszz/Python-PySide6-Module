# signal: quando algo ocorrer, execute alguma ação
# slot: ação que vai ocorrer se o signal for chamado

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QGridLayout,
    QMainWindow,
)
import sys

app = QApplication(sys.argv)
window = QMainWindow()
central = QWidget()

window.setWindowTitle('Hello, World!')


@Slot()
def slot_example(status):
    status.showMessage('Slot executado')


@Slot()
def _ischecked(checked: QWidget):
    print(f'Marcado?: {checked}')


@Slot()
def validator_check(action):
    def inner():
        _ischecked(action.isChecked())
    return inner


btn = QPushButton('Texto do botao')
btn.setStyleSheet(
    'font-size: 40px;'
)

btn2 = QPushButton('botão 2')

btn2.setStyleSheet(
    'font-size: 20px'
)

btn3 = QPushButton('botão 3')
btn3.setStyleSheet('background-color: #000')

layout = QGridLayout()

window.setCentralWidget(central)
central.setLayout(layout)

layout.addWidget(btn, 1, 1, 1, 1)
layout.addWidget(btn2, 1, 2, 1, 1)
layout.addWidget(btn3, 3, 1, 1, 2)

status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')


# menu
menu = window.menuBar()
first_menu = menu.addMenu('Qualquer coisa')
first_action = first_menu.addAction('Primeira ação')

first_action.triggered.connect(
    lambda:  slot_example(status_bar)
)


second_action = first_menu.addAction('Segunda ação')
second_action.setCheckable(True)

#              signal   slot
# second_action.toggled.connect(_ischecked)
second_action.hovered.connect(validator_check(second_action))

# verifica se a segunda ação esta marcada e retorna true ou false quando
# clicada

btn.clicked.connect(validator_check(second_action))
window.show()
app.exec()
