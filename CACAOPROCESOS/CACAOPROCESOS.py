
import sys
from PySide2 import *
from PySide2 import QtWidgets
from ui_princ import *
from ui_regis import *
from ui_cotizar import *
from ui_total import *
from ui_envio import *


usuarios={}

def cantidadchoc(grano):
        chocolatecant =(grano*0.7 )/0.48
        return chocolatecant

def precio(chocolate):
    price=chocolate*45
    return price

def descuento(chocolate ,precio):
    if (chocolate >45):
        dscto =precio*0.30
        return dscto
    else:
        return 0

def totales(price,dscnto):
    rest=price-dscnto
    return rest

def entrega(chocolate):
    time =8
    if chocolate>=10:
        dias=chocolate /10
        new=dias+time
        return new
    else:
        return time

class sesion(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_principal_ventana()
        self.ui.setupUi(self)
        #ELIMINAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        #TRANSPARENTE
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.contrasea.setEchoMode(QLineEdit.Password)
        self.ui.IniciaBtn.clicked.connect(self.cotiz)
        self.ui.registrarBtn.clicked.connect(self.registrar)
        self.ui.exit.clicked.connect(self.fin)

    def fin(self):
        sys.exit()

    def cotiz(self):

        usu=self.ui.usuario.text()
        con=self.ui.contrasea.text()

        if (usuarios.get(usu)) and (usuarios[usu]==con):
            self.hide()
            #ABRIR VENTANA DE REGISTRO
            self.coti=cotizacion()
            self.coti.show()
        else:
            self.ui.error.setText("Usuario/Pass Incorrect")
        

    def registrar(self):
        #CERRAR VENTANA
        self.hide()
        #ABRIR VENTANA DE REGISTRO
        self.regis=registro()
        self.regis.show()



class registro(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.re=Ui_registro_ventana()
        self.re.setupUi(self)
        #ELIMINAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        #TRANSPARENTE
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.re.contraseaR.setEchoMode(QLineEdit.Password)
        self.re.regisBtn.clicked.connect(self.registrar)
        self.re.exit.clicked.connect(self.fin)

    def fin(self):
            sys.exit()

    def registrar(self):
        usu=self.re.usuarioR.text()
        con=self.re.contraseaR.text()

        if (usuarios.get(usu)) and (usuarios[usu]==con):
            self.re.error.setText("Existente")
            
        else:
            usuarios[usu]=con
            #CERRAR VENTANA
            self.hide()
            #ABRIR VENTANA DE REGISTRO
            self.sesion=sesion()
            self.sesion.show()
      
        



  
class cotizacion(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.co=Ui_cotizar_ventana()
        self.co.setupUi(self)
        #ELIMINAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        #TRANSPARENTE
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.co.procesar.clicked.connect(self.proceso)
        self.co.total.clicked.connect(self.wtotal)
        self.co.exit.clicked.connect(self.fin)

    def wtotal(self):
        #CERRAR VENTANA
        self.hide()
        #ABRIR VENTANA DE REGISTRO
        self.total=total()
        self.total.show()

    def incrementaBarra(self):
        self.co.barra.setValue(self.co.barra.value()+1)

    def proceso(self):

        cantgrano=self.co.cacao.text()
        self.co.barra.setValue(0)
        timer=QTimer(self)
        timer.timeout.connect(self.incrementaBarra)
        timer.start(5)
 
        try:

            granott=float(cantgrano)
            global result
            result=round(cantidadchoc(granott),2)
            convert=str(result)
            self.co.choco.setText(f"{convert} KG")
        except Exception:
            self.co.choco.setText("ERROR")

    def fin(self):
        sys.exit()


class total(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.to=Ui_total_ventana()
        self.to.setupUi(self)
        #ELIMINAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        #TRANSPARENTE
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.to.exit.clicked.connect(self.fin)
        self.to.envio.clicked.connect(self.venv)
        
        

        price=precio(result)
        dsct=descuento(result,price)
        tott=totales(price,dsct)

        self.to.precio.setText(f"{str(price)}$")
        self.to.dscto.setText(f"{str(dsct)}$")
        self.to.totalpre.setText(f"{str(tott)}$")


    def venv(self):
        #CERRAR VENTANA
        self.hide()
        #ABRIR VENTANA DE REGISTRO
        self.envio=envios()
        self.envio.show()

    def fin(self):
        sys.exit()

class envios(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.en=Ui_envio_ventana()
        self.en.setupUi(self)
        #ELIMINAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        #TRANSPARENTE
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.en.exit.clicked.connect(self.fin)
        self.en.terminar.clicked.connect(self.fin)

        enviar=round(entrega(result))

        self.en.tiempo.setText(f"{str(enviar)} dias")


    def fin(self):
        sys.exit()
        

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=sesion()
    window.show()
    sys.exit(app.exec_())