# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regisgQdDFz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_registro_ventana(object):
    def setupUi(self, registro_ventana):
        if not registro_ventana.objectName():
            registro_ventana.setObjectName(u"registro_ventana")
        registro_ventana.resize(797, 600)
        self.centralwidget = QWidget(registro_ventana)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(190, 70, 311, 421))
        self.frame.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.imag2 = QLabel(self.frame)
        self.imag2.setObjectName(u"imag2")
        self.imag2.setGeometry(QRect(100, 30, 111, 121))
        self.imag2.setStyleSheet(u"")
        self.imag2.setPixmap(QPixmap(u"reg.png"))
        self.imag2.setScaledContents(True)
        self.usuarioR = QLineEdit(self.frame)
        self.usuarioR.setObjectName(u"usuarioR")
        self.usuarioR.setGeometry(QRect(70, 190, 171, 31))
        self.usuarioR.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.usuarioR.setAlignment(Qt.AlignCenter)
        self.usuarioR.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.contraseaR = QLineEdit(self.frame)
        self.contraseaR.setObjectName(u"contraseaR")
        self.contraseaR.setGeometry(QRect(70, 260, 171, 31))
        self.contraseaR.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.contraseaR.setAlignment(Qt.AlignCenter)
        self.contraseaR.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.regisBtn = QPushButton(self.frame)
        self.regisBtn.setObjectName(u"regisBtn")
        self.regisBtn.setGeometry(QRect(100, 340, 101, 31))
        self.regisBtn.setStyleSheet(u"QPushButton {\n"
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
        registro_ventana.setCentralWidget(self.centralwidget)

        self.retranslateUi(registro_ventana)

        QMetaObject.connectSlotsByName(registro_ventana)
    # setupUi

    def retranslateUi(self, registro_ventana):
        registro_ventana.setWindowTitle(QCoreApplication.translate("registro_ventana", u"MainWindow", None))
        self.imag2.setText("")
        self.usuarioR.setPlaceholderText(QCoreApplication.translate("registro_ventana", u"Usuario", None))
        self.contraseaR.setPlaceholderText(QCoreApplication.translate("registro_ventana", u"Contrase\u00f1a", None))
        self.regisBtn.setText(QCoreApplication.translate("registro_ventana", u"Registrar", None))
        self.exit.setText(QCoreApplication.translate("registro_ventana", u"X", None))
        self.error.setText("")
    # retranslateUi

