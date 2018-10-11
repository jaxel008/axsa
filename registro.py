import pymysql.cursors


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton, QMessageBox)




global conn,cur

conn = pymysql.connect(host='localhost',user='root', password='axel', db='educativa')
cur = conn.cursor()


class registro(QMainWindow):

    

    def registrarus(self):
        global conn,cur,data

        cuenta = self.comboBoxCuenta.currentText()

        user = self.lineEditUsuario.text()
        apellidop = self.lineEditapellidop.text()
        apellidom = self.lineEditapellidom.text()
        correo = self.lineEditcorreo.text()
        nick = self.lineEditnick.text()
        contra = self.lineEditcontraseña.text()



        if(self.comboBoxCuenta.currentText() == 'Usuario'):
        
            try:
                data = cur.execute("INSERT INTO users (UserNombre,UserApellidoP,UserApellidoM,UserCorreo,UserNick,UserPass) VALUES (%s,%s,%s,%s,%s,%s)",(user,apellidop,apellidom,correo,nick,contra))
                conn.commit()

                if(data):
                    self.messagebox("ANUNCIO","SE HA REGISTRADO CON EXITO")

                else:
                    self.messagebox("error","error")        
        

            except pymysql.err.InternalError:
                self.messagebox("ERROR","INTENTE DE NUEVO")

            except pymysql.err.IntegrityError:
                self.messagebox("ERROR","EL CORREO YA ESTA EN USO")      

        if(self.comboBoxCuenta.currentText() == 'Profesor'):
        
            try:
                data = cur.execute("INSERT INTO profesor (ProfesorNombre,ProfesorApellidoP,ProfesorApellidoM,ProfesorCorreo,ProfesorNick,ProfesorPass) VALUES (%s,%s,%s,%s,%s,%s)",(user,apellidop,apellidom,correo,nick,contra))
                conn.commit()
                if(data):
                    self.messagebox("ANUNCIO","SE HA REGISTRADO CON EXITO")

            except pymysql.err.InternalError:
                self.messagebox("error","error")      
        if(self.comboBoxCuenta.currentText() == ''):
            self.messagebox("ANUNCIO","ELIJA EL TIPO DE CUENTA")                               

 


    

    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.setText(message)
        mess.exec_()    



    def __init__(self, parent=None):
        super(registro, self).__init__(parent)
        
        self.setWindowTitle("BIENVENIDOS")
        self.setWindowIcon(QIcon("registro.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 560)

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(243, 243, 243))
        self.setPalette(paleta)

        self.initUI(registro)

    



       

    def initUI(self,registro):

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(0,0,93))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(400)
        frame.setFixedHeight(84)
        frame.move(0, 0)

        labelIcono = QLabel(frame)
        labelIcono.setFixedWidth(40)
        labelIcono.setFixedHeight(40)
        labelIcono.setPixmap(QPixmap("registro.png").scaled(40, 40, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        labelIcono.move(37, 22)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(16)
        fuenteTitulo.setBold(True)

        labelTitulo = QLabel("<font color='white'>REGISTRO </font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(83, 20)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(9)

        labelSubtitulo = QLabel("<font color='white'"
                                "(Python).</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(111, 46)



        labelCuenta = QLabel("Cuenta", self)
        labelCuenta.move(60, 110)

        self.comboBoxCuenta = QComboBox(self)
        self.comboBoxCuenta.addItems(["Profesor", "Usuario"])
        self.comboBoxCuenta.setCurrentIndex(-1)
        self.comboBoxCuenta.setFixedWidth(280)
        self.comboBoxCuenta.setFixedHeight(26)
        self.comboBoxCuenta.move(60, 136)






        labelUsuario = QLabel("Nombre", self)
        labelUsuario.move(60, 170)

        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(60, 196)

        imagenUsuario = QLabel(frameUsuario)
        imagenUsuario.setPixmap(QPixmap("usuario.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        imagenUsuario.move(10, 4)

        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)



        labelapellidop = QLabel("Apellido Paterno", self)
        labelapellidop.move(60, 224)

        frameapellidop = QFrame(self)
        frameapellidop.setFrameShape(QFrame.StyledPanel)
        frameapellidop.setFixedWidth(280)
        frameapellidop.setFixedHeight(28)
        frameapellidop.move(60, 250)

        imagenapellidop = QLabel(frameapellidop)
        imagenapellidop.setPixmap(QPixmap("").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
        imagenapellidop.move(10, 4)

        self.lineEditapellidop = QLineEdit(frameapellidop)
        self.lineEditapellidop.setFrame(False)
        
        self.lineEditapellidop.setTextMargins(8, 0, 4, 1)
        self.lineEditapellidop.setFixedWidth(238)
        self.lineEditapellidop.setFixedHeight(26)
        self.lineEditapellidop.move(40, 1)



        labelapellidom = QLabel("Apellido Materno", self)
        labelapellidom.move(60, 278)

        frameapellidom = QFrame(self)
        frameapellidom.setFrameShape(QFrame.StyledPanel)
        frameapellidom.setFixedWidth(280)
        frameapellidom.setFixedHeight(28)
        frameapellidom.move(60, 304)

        imagenapellidom = QLabel(frameapellidop)
        imagenapellidom.setPixmap(QPixmap("").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
        imagenapellidom.move(10, 4)

        self.lineEditapellidom = QLineEdit(frameapellidom)
        self.lineEditapellidom.setFrame(False)
        self.lineEditapellidom.setTextMargins(8, 0, 4, 1)
        self.lineEditapellidom.setFixedWidth(238)
        self.lineEditapellidom.setFixedHeight(26)
        self.lineEditapellidom.move(40, 1)


        labelcorreo = QLabel("Correo",self)
        labelcorreo.move(60,332)

        framecorreo = QFrame(self)
        framecorreo.setFrameShape(QFrame.StyledPanel)
        framecorreo.setFixedWidth(280)
        framecorreo.setFixedHeight(28)
        framecorreo.move(60, 358)

        imagencorreo = QLabel(framecorreo)
        imagencorreo.setPixmap(QPixmap("correo.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
        imagencorreo.move(10, 4)

        self.lineEditcorreo = QLineEdit(framecorreo)
        self.lineEditcorreo.setFrame(False)
        self.lineEditcorreo.setTextMargins(8, 0, 4, 1)
        self.lineEditcorreo.setFixedWidth(238)
        self.lineEditcorreo.setFixedHeight(26)
        self.lineEditcorreo.move(40, 1)

        labelnick = QLabel("Nick",self)
        labelnick.move(60,386)

        framenick = QFrame(self)
        framenick.setFrameShape(QFrame.StyledPanel)
        framenick.setFixedWidth(280)
        framenick.setFixedHeight(28)
        framenick.move(60, 412)

        self.lineEditnick = QLineEdit(framenick)
        self.lineEditnick.setFrame(False)
        self.lineEditnick.setTextMargins(8, 0, 4, 1)
        self.lineEditnick.setFixedWidth(238)
        self.lineEditnick.setFixedHeight(26)
        self.lineEditnick.move(40, 1)

        labelcontraseña = QLabel("Contraseña",self)
        labelcontraseña.move(60,440)



        framecontraseña = QFrame(self)
        framecontraseña.setFrameShape(QFrame.StyledPanel)
        framecontraseña.setFixedWidth(280)
        framecontraseña.setFixedHeight(28)
        framecontraseña.move(60, 466)

        imagenContraseña = QLabel(framecontraseña)
        imagenContraseña.setPixmap(QPixmap("contraseña.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
        imagenContraseña.move(10, 4)

        self.lineEditcontraseña = QLineEdit(framecontraseña)
        self.lineEditcontraseña.setFrame(False)

        self.lineEditcontraseña.setTextMargins(8, 0, 4, 1)
        self.lineEditcontraseña.setFixedWidth(238)
        self.lineEditcontraseña.setFixedHeight(26)
        self.lineEditcontraseña.move(40, 1)



        buttonregistrarse = QPushButton("Registrarse", self)
        buttonregistrarse.setFixedWidth(135)
        buttonregistrarse.setFixedHeight(28)
        buttonregistrarse.move(60, 502)
        buttonregistrarse.clicked.connect(self.registrarus)



        

        buttonCancelar = QPushButton("Cancelar", self)
        buttonCancelar.setFixedWidth(135)
        buttonCancelar.setFixedHeight(28)
        buttonCancelar.move(205, 502)

        buttonCancelar.clicked.connect(self.close)


























if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)


    MainWindow = QtWidgets.QMainWindow()
    ventana = registro()
    ventana.initUI(registro)
    ventana.show()


    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)
    
    ventana = registro()
    ventana.show()
    
    sys.exit(aplicacion.exec_())

#------------------------------------------------------------

