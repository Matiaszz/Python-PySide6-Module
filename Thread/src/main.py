from PySide6.QtWidgets import (QApplication, QWidget)
from PySide6.QtCore import QThread, QObject, Signal
from window import Ui_myWidget
from time import sleep
import sys


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(3):
            value = str(i)
            self.progressed.emit(value)
            sleep(1)

        self.finished.emit(value)


class main(QWidget, Ui_myWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()
        worker = self._worker
        thread = self._thread

        # move the worker to thread
        worker.moveToThread(thread)

        # run
        thread.started.connect(worker.run)
        thread.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        # Events
        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1InProgress)
        worker.finished.connect(self.worker1Finish)

        # Finalization
        thread.start()
        thread.exit()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        print('Thread Started')
        self.label1.setText(value)

    def worker1InProgress(self, value):
        print('Thread in progress')
        self.label1.setText(value)

    def worker1Finish(self, value):
        self.button1.setDisabled(False)
        print('Thread finished')
        self.label1.setText(value)

    ################################

    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()
        worker = self._worker2
        thread = self._thread2

        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        thread.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2InProgress)
        worker.finished.connect(self.worker2Finish)

        thread.start()
        thread.exit()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        print('2 Thread Started')
        self.label2.setText(value)

    def worker2InProgress(self, value):
        print('2 Thread in progress')
        self.label2.setText(value)

    def worker2Finish(self, value):
        self.button2.setDisabled(False)
        print('2 Thread finished')
        self.label2.setText(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = main()

    widget.show()
    app.exec()
