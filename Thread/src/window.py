# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'untitled.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QWidget)


class Ui_myWidget(object):
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(myWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout = QGridLayout()
        self.layout.setObjectName(u"layout")
        self.label1 = QLabel(myWidget)
        self.label1.setObjectName(u"label1")
        font = QFont()
        font.setPointSize(40)
        self.label1.setFont(font)

        self.layout.addWidget(self.label1, 0, 0, 1, 1)

        self.label2 = QLabel(myWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font)

        self.layout.addWidget(self.label2, 0, 1, 1, 1)

        self.button1 = QPushButton(myWidget)
        self.button1.setObjectName(u"botao1")

        self.layout.addWidget(self.button1, 1, 0, 1, 1)

        self.button2 = QPushButton(myWidget)
        self.button2.setObjectName(u"botao2")

        self.layout.addWidget(self.button2, 1, 1, 1, 1)

        self.horizontalLayout.addLayout(self.layout)

        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(
            QCoreApplication.translate("myWidget", u"Form", None))
        self.label1.setText(
            QCoreApplication.translate("myWidget", u"L1", None))
        self.label2.setText(
            QCoreApplication.translate("myWidget", u"L2", None))
        self.button1.setText(QCoreApplication.translate(
            "myWidget", u"butao1", None))
        self.button2.setText(QCoreApplication.translate(
            "myWidget", u"butao2", None))
    # retranslateUi
