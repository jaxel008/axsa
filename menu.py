from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)
from addclase import *
from login import *
from pdfuser import *

class ui_menu(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        
        self.setMouseTracking(True)

        self.fuente = self.font()

        self.posicionX = int
        self.posicionY = int

    def enterEvent(self, event):
        self.posicionX = self.pos().x()
        self.posicionY = self.pos().y()
        
        self.animacionCursor = QPropertyAnimation(self, b"geometry")
        self.animacionCursor.setDuration(100)
        self.animacionCursor.setEndValue(QRect(self.posicionX-15, self.posicionY-6, 170, 60))
        self.animacionCursor.start(QAbstractAnimation.DeleteWhenStopped)
        
        self.fuente.setPointSize(11)
        self.setFont(self.fuente)

    def leaveEvent(self, event):
        self.fuente.setPointSize(10)
        self.setFont(self.fuente)
        
        self.animacionNoCursor = QPropertyAnimation(self, b"geometry")
        self.animacionNoCursor.setDuration(100)
        self.animacionNoCursor.setEndValue(QRect(self.posicionX, self.posicionY, 140, 60))
        self.animacionNoCursor.start(QAbstractAnimation.DeleteWhenStopped)


class Ui_animarBotones(QDialog):





    def abrirmenuuser(self):
        usuarioprof = self.lineEditUsuario1.text() 

        
        data=cur.execute("SELECT userId  FROM users WHERE usernick = %s",(usuarioprof))
        registro = cur.fetchall()
        i = 0
        if(data):
            self.openpdfuser()
            self.ui.usuarionick.setText(str(registro))  
            self.ui.clasecombo()




    def openpdfuser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_usermenupdf()
        self.ui.setupUi(self.window)
        self.window.show()
        



    def openclase(self):
        self.window = QtWidgets.QMainWindow()
        self.ventana = ventanaaddclase()
        self.ventana.initUI(self)
        self.ventana.show()


    def openanadirclase(self):
        usuario = self.lineEditUsuario1.text() 

        global conn,cur,data
        conn = pymysql.connect(host='localhost',user='root', password='axel', db='educativa')
        cur = conn.cursor()

        data=cur.execute("SELECT UserId  FROM users WHERE usernombre = %s",(usuario))
        registro = cur.fetchall()
        i = 0
        if(data):
            self.openclase()
            self.ventana.lineEditUserId.setText(str(registro))
     

    
    def __init__(self, parent=None):
        super(Ui_animarBotones, self).__init__(parent)
        
        self.setWindowTitle("ui_menu USUARIO")
        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)

        

    def setupUI(self, animarBotones):



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
        labelIcono.setPixmap(QPixmap("mundo.png").scaled(40, 40, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        labelIcono.move(37, 22)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(16)
        fuenteTitulo.setBold(True)

        labelTitulo = QLabel("<font color='white'>BIENVENIDO</font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(83, 20)

        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(100)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(90, 50)

        



        self.lineEditUsuario1 = QLineEdit(frameUsuario)
        
        self.lineEditUsuario1.setReadOnly(True)
        self.lineEditUsuario1.setFrame(False)
        self.lineEditUsuario1.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario1.setFixedWidth(100)
        self.lineEditUsuario1.setFixedHeight(26)
        self.lineEditUsuario1.move(0, 1)



        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(9)

        labelSubtitulo = QLabel("<font color='white'"
                                "(Python).</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(111, 46)


        self.button = ui_menu(self)
        self.button.setText("MIS CURSOS")
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.setAutoDefault(False)
        self.button.setGeometry(40, 150, 160, 60)
        self.button.clicked.connect(self.abrirmenuuser)


        self.buttonDos = ui_menu(self)
        self.buttonDos.setText("UNIRSE A \nUN CURSO")
        self.buttonDos.setCursor(Qt.PointingHandCursor)
        self.buttonDos.setAutoDefault(False)
        self.buttonDos.setGeometry(220, 150, 160, 60)
        self.buttonDos.clicked.connect(self.openanadirclase)





# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ventana = Ui_animarBotones()
    ventana.setupUI(Ui_animarBotones)
    ventana.show()


    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Arial")

    aplicacion.setFont(fuente)




    sys.exit(aplicacion.exec_())





