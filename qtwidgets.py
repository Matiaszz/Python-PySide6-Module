# QVBoxLayout - widgets verticais
# QHBoxLayout - widgets Horizontais
# QGridLayout - widgets se comportam como se estivessem em uma grade, tendo
# Linhas e colunas para posicionar os widgets
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout
import sys

app = QApplication(sys.argv)

btn = QPushButton('Texto do botao')
# QSS (um css do QT, é parecido com CSS, para separar, usar ";")

btn.setStyleSheet(
    'font-size: 40px;'
)


# Se eu tiver esse botão de baixo, vai criar outra janela apenas com esse botao
# (buttons2.show())

btn2 = QPushButton('botão 2')

btn2.setStyleSheet(
    'font-size: 20px'
)

btn3 = QPushButton('botão 3')
btn3.setStyleSheet('background-color: #000')


# Para corrigir esse "problema", precisamos de um widget central, que seria:
central = QWidget()  # uma janela que só vai servir para colocar outros widgets
layout = QGridLayout()  # define o layout da janela

central.setLayout(layout)

# grid: row (linha), column (coluna), rowspan(quantas linhas o elem se expande)
# colspan: (quantas colunas o elem se expande)
layout.addWidget(btn, 1, 1, 1, 1)  # Padrão: 1 rowspan, 1colspan
layout.addWidget(btn2, 1, 2, 1, 1)
layout.addWidget(btn3, 3, 1, 1, 2)


central.show()
app.exec()
