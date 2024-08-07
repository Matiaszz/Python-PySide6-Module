# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central)
#           -> Layout (layout)
#               -> Widget 1 (btn)
#               -> Widget 2 (btn2)
#               -> Widget 3 (btn3)
#   -> show
# -> exec

# achei legalzinho esse formato pra importar muitas coisas
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


def slot_example(status):
    status.showMessage('Slot executado')


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

# status bar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')


# menu
menu = window.menuBar()
first_menu = menu.addMenu('Qualquer coisa')
first_action = first_menu.addAction('Primeira ação')

# quando a ação do menu for clicada, mude o status bar
first_action.triggered.connect(
    lambda:  slot_example(status_bar)
)

window.show()
app.exec()
