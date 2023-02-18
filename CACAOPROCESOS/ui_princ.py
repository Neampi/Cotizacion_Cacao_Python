# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'princwJkUyE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_principal_ventana(object):
    def setupUi(self, principal_ventana):
        if not principal_ventana.objectName():
            principal_ventana.setObjectName(u"principal_ventana")
        principal_ventana.resize(524, 578)
        self.centralwidget = QWidget(principal_ventana)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 40, 311, 421))
        self.frame.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.imag = QLabel(self.frame)
        self.imag.setObjectName(u"imag")
        self.imag.setGeometry(QRect(100, 30, 111, 121))
        self.imag.setStyleSheet(u"")
        self.imag.setPixmap(QPixmap(u":/ima/reg.png"))
        self.imag.setScaledContents(True)
        self.usuario = QLineEdit(self.frame)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(70, 190, 171, 31))
        self.usuario.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.usuario.setAlignment(Qt.AlignCenter)
        self.usuario.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.contrasea = QLineEdit(self.frame)
        self.contrasea.setObjectName(u"contrasea")
        self.contrasea.setGeometry(QRect(70, 260, 171, 31))
        self.contrasea.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.contrasea.setAlignment(Qt.AlignCenter)
        self.contrasea.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.registrarBtn = QPushButton(self.frame)
        self.registrarBtn.setObjectName(u"registrarBtn")
        self.registrarBtn.setGeometry(QRect(30, 350, 101, 31))
        self.registrarBtn.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.IniciaBtn = QPushButton(self.frame)
        self.IniciaBtn.setObjectName(u"IniciaBtn")
        self.IniciaBtn.setGeometry(QRect(150, 350, 121, 31))
        self.IniciaBtn.setStyleSheet(u"QPushButton {\n"
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
        self.error = QLabel(self.frame)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(70, 310, 171, 16))
        principal_ventana.setCentralWidget(self.centralwidget)

        self.retranslateUi(principal_ventana)

        QMetaObject.connectSlotsByName(principal_ventana)
    # setupUi

    def retranslateUi(self, principal_ventana):
        principal_ventana.setWindowTitle(QCoreApplication.translate("principal_ventana", u"MainWindow", None))
        self.imag.setText("")
        self.usuario.setPlaceholderText(QCoreApplication.translate("principal_ventana", u"Usuario", None))
        self.contrasea.setPlaceholderText(QCoreApplication.translate("principal_ventana", u"Contrase\u00f1a", None))
        self.registrarBtn.setText(QCoreApplication.translate("principal_ventana", u"Registrar", None))
        self.IniciaBtn.setText(QCoreApplication.translate("principal_ventana", u"Iniciar Sesion", None))
        self.exit.setText(QCoreApplication.translate("principal_ventana", u"X", None))
        self.error.setText("")
    # retranslateUi

