# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'totaluhoeiy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_total_ventana(object):
    def setupUi(self, total_ventana):
        if not total_ventana.objectName():
            total_ventana.setObjectName(u"total_ventana")
        total_ventana.resize(800, 600)
        self.centralwidget = QWidget(total_ventana)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(250, 30, 311, 421))
        self.frame.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.imag = QLabel(self.frame)
        self.imag.setObjectName(u"imag")
        self.imag.setGeometry(QRect(70, -30, 181, 171))
        self.imag.setStyleSheet(u"")
        self.imag.setPixmap(QPixmap(u"ca.png"))
        self.imag.setScaledContents(True)
        self.exit = QPushButton(self.frame)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(270, 10, 31, 21))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 190, 211, 16))
        self.choco = QLabel(self.frame)
        self.choco.setObjectName(u"choco")
        self.choco.setGeometry(QRect(100, 310, 111, 31))
        font = QFont()
        font.setPointSize(14)
        self.choco.setFont(font)
        self.envio = QPushButton(self.frame)
        self.envio.setObjectName(u"envio")
        self.envio.setGeometry(QRect(110, 370, 101, 31))
        self.envio.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 100, 47, 13))
        self.precio = QLabel(self.frame)
        self.precio.setObjectName(u"precio")
        self.precio.setGeometry(QRect(110, 130, 121, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.precio.setFont(font1)
        self.dscto = QLabel(self.frame)
        self.dscto.setObjectName(u"dscto")
        self.dscto.setGeometry(QRect(110, 220, 121, 31))
        self.dscto.setFont(font1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 270, 211, 16))
        self.totalpre = QLabel(self.frame)
        self.totalpre.setObjectName(u"totalpre")
        self.totalpre.setGeometry(QRect(110, 300, 121, 31))
        self.totalpre.setFont(font1)
        total_ventana.setCentralWidget(self.centralwidget)

        self.retranslateUi(total_ventana)

        QMetaObject.connectSlotsByName(total_ventana)
    # setupUi

    def retranslateUi(self, total_ventana):
        total_ventana.setWindowTitle(QCoreApplication.translate("total_ventana", u"MainWindow", None))
        self.imag.setText("")
        self.exit.setText(QCoreApplication.translate("total_ventana", u"X", None))
        self.label.setText(QCoreApplication.translate("total_ventana", u"DESCUENTO:", None))
        self.choco.setText("")
        self.envio.setText(QCoreApplication.translate("total_ventana", u"Envio", None))
        self.label_2.setText(QCoreApplication.translate("total_ventana", u"PRECIO:", None))
        self.precio.setText("")
        self.dscto.setText("")
        self.label_3.setText(QCoreApplication.translate("total_ventana", u"TOTAL:", None))
        self.totalpre.setText("")
    # retranslateUi

