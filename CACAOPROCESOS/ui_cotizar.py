# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cotizarYDqEat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_cotizar_ventana(object):
    def setupUi(self, cotizar_ventana):
        if not cotizar_ventana.objectName():
            cotizar_ventana.setObjectName(u"cotizar_ventana")
        cotizar_ventana.resize(800, 600)
        self.centralwidget = QWidget(cotizar_ventana)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(220, 50, 311, 421))
        self.frame.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.imag = QLabel(self.frame)
        self.imag.setObjectName(u"imag")
        self.imag.setGeometry(QRect(70, -30, 181, 171))
        self.imag.setStyleSheet(u"")
        self.imag.setPixmap(QPixmap(u"ca.png"))
        self.imag.setScaledContents(True)
        self.cacao = QLineEdit(self.frame)
        self.cacao.setObjectName(u"cacao")
        self.cacao.setGeometry(QRect(70, 110, 171, 31))
        self.cacao.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.cacao.setAlignment(Qt.AlignCenter)
        self.cacao.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.procesar = QPushButton(self.frame)
        self.procesar.setObjectName(u"procesar")
        self.procesar.setGeometry(QRect(110, 170, 101, 31))
        self.procesar.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.exit = QPushButton(self.frame)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(270, 10, 31, 21))
        self.barra = QProgressBar(self.frame)
        self.barra.setObjectName(u"barra")
        self.barra.setGeometry(QRect(40, 230, 251, 23))
        self.barra.setValue(0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 280, 211, 16))
        self.choco = QLabel(self.frame)
        self.choco.setObjectName(u"choco")
        self.choco.setGeometry(QRect(100, 310, 111, 31))
        font = QFont()
        font.setPointSize(14)
        self.choco.setFont(font)
        self.total = QPushButton(self.frame)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(110, 370, 101, 31))
        self.total.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        cotizar_ventana.setCentralWidget(self.centralwidget)

        self.retranslateUi(cotizar_ventana)

        QMetaObject.connectSlotsByName(cotizar_ventana)
    # setupUi

    def retranslateUi(self, cotizar_ventana):
        cotizar_ventana.setWindowTitle(QCoreApplication.translate("cotizar_ventana", u"MainWindow", None))
        self.imag.setText("")
        self.cacao.setText("")
        self.cacao.setPlaceholderText(QCoreApplication.translate("cotizar_ventana", u"Gramos a cotizar", None))
        self.procesar.setText(QCoreApplication.translate("cotizar_ventana", u"Procesar", None))
        self.exit.setText(QCoreApplication.translate("cotizar_ventana", u"X", None))
        self.label.setText(QCoreApplication.translate("cotizar_ventana", u"CANTIDAD DE CHOCOLATE PROCESADO:", None))
        self.choco.setText("")
        self.total.setText(QCoreApplication.translate("cotizar_ventana", u"Total", None))
    # retranslateUi

