import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import Window
from variables import ICON_ADRESS
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button
if __name__ == '__main__':
    # Create app
    app = QApplication(sys.argv)
    window = Window()
    setupTheme(app)

    # define the icon
    icon = QIcon(str(ICON_ADRESS))
    window.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10 = 1024')
    window.addToVLayout(info)
    # Display
    display = Display()
    window.addToVLayout(display)

    # button
    button = Button('Texto do botão')
    window.addToVLayout(button)
    # Execution
    window.adjustFixedSize()
    window.show()
    app.exec()
