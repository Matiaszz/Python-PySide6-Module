from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
)


class Window(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, *kwargs)

        # Configuring basic layout
        self.central = QWidget()
        self.vLayout = QVBoxLayout()
        self.central.setLayout(self.vLayout)
        self.setCentralWidget(self.central)

        # window Settings
        self.setWindowTitle('Calculator')

        # Last thing to be done
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
