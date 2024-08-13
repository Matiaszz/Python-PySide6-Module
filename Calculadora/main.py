import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import Window
from variables import ICON_ADRESS
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonGrid
if __name__ == '__main__':
    # Create app
    app = QApplication(sys.argv)
    window = Window()
    setupTheme(app)

    # define the icon
    icon = QIcon(str(ICON_ADRESS))
    window.setWindowIcon(icon)

    # Info
    info = Info()
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonGrid = ButtonGrid(display, info, window)
    window.vLayout.addLayout(buttonGrid)

    # Execution
    window.adjustFixedSize()
    window.show()
    app.exec()
