# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enviobgTAEQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_envio_ventana(object):
    def setupUi(self, envio_ventana):
        if not envio_ventana.objectName():
            envio_ventana.setObjectName(u"envio_ventana")
        envio_ventana.resize(800, 600)
        self.centralwidget = QWidget(envio_ventana)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(230, 70, 311, 361))
        self.frame.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.imag = QLabel(self.frame)
        self.imag.setObjectName(u"imag")
        self.imag.setGeometry(QRect(100, 10, 121, 121))
        self.imag.setStyleSheet(u"")
        self.imag.setPixmap(QPixmap(u"courier.png"))
        self.imag.setScaledContents(True)
        self.exit = QPushButton(self.frame)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(270, 10, 31, 21))
        self.terminar = QPushButton(self.frame)
        self.terminar.setObjectName(u"terminar")
        self.terminar.setGeometry(QRect(110, 310, 101, 31))
        self.terminar.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 160, 211, 16))
        self.tiempo = QLabel(self.frame)
        self.tiempo.setObjectName(u"tiempo")
        self.tiempo.setGeometry(QRect(70, 200, 171, 81))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.tiempo.setFont(font)
        envio_ventana.setCentralWidget(self.centralwidget)

        self.retranslateUi(envio_ventana)

        QMetaObject.connectSlotsByName(envio_ventana)
    # setupUi

    def retranslateUi(self, envio_ventana):
        envio_ventana.setWindowTitle(QCoreApplication.translate("envio_ventana", u"MainWindow", None))
        self.imag.setText("")
        self.exit.setText(QCoreApplication.translate("envio_ventana", u"X", None))
        self.terminar.setText(QCoreApplication.translate("envio_ventana", u"Terminar", None))
        self.label_3.setText(QCoreApplication.translate("envio_ventana", u"TIEMPO DE ENTREGA:", None))
        self.tiempo.setText("")
    # retranslateUi

