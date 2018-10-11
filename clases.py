import pymysql.cursors


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)


global conn,cur

conn = pymysql.connect(host='localhost',user='root', password='axel', db='educativa')
cur = conn.cursor()




class ventanaclase(QMainWindow):


    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.setText(message)
        mess.exec_()    




    def crearcurso(self):
        global conn,cur,data

        cursonombre = self.lineEditclase.text()
        idprof = self.lineEditprofid.text()

        try:
            if(len(cursonombre) >2):
                
                

                data=cur.execute("INSERT INTO CLASES (CLASENOMBRE,CLASEPROFESORID) VALUES (%s,%s)" ,(cursonombre,idprof))
                conn.commit()

                if(data):
                    self.messagebox("ANUNCIO","SE HA CREADO EL CURSO")
            else:
                self.messagebox("ANUNCIO","ENTRADA DE DATOS INCORRECTA")         

     



        except pymysql.err.InternalError:
            self.messagebox("ANUNCIO","ERROR,INTENTE DE NUEVO")         
     



    def __init__(self, parent=None):
        super(ventanaclase, self).__init__(parent)
        
        self.setWindowTitle("BIENVENIDO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 380)

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(243, 243, 243))
        self.setPalette(paleta)

        

    def initUI(self, ventanaclase):

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(76,150,123))

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
        labelIcono.setPixmap(QPixmap("icono3.png").scaled(40, 40, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        labelIcono.move(37, 22)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(16)
        fuenteTitulo.setBold(True)

        labelTitulo = QLabel("<font color='white'>CREAR CURSO</font>", frame)
        labelTitulo.setFixedWidth(1000)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(83, 20)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(9)

        labelSubtitulo = QLabel("<font color='white'"
                                "(Python).</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(111, 46)

      # ===================== WIDGETS crear ======================


        # ========================================================

        labelclase = QLabel("Nombre del Curso", self)
        labelclase.move(60, 110)
        labelclase.setFixedWidth(1000)
        frameclase = QFrame(self)
        frameclase.setFrameShape(QFrame.StyledPanel)
        frameclase.setFixedWidth(280)
        frameclase.setFixedHeight(28)
        frameclase.move(60, 136)

        imagenclase = QLabel(frameclase)
        imagenclase.setPixmap(QPixmap("cursoicon.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        imagenclase.move(10, 4)

        self.lineEditclase = QLineEdit(frameclase)
        self.lineEditclase.setFrame(False)
        self.lineEditclase.setTextMargins(8, 0, 4, 1)
        self.lineEditclase.setFixedWidth(238)
        self.lineEditclase.setFixedHeight(26)
        self.lineEditclase.move(40, 1)

        # ========================================================

        labelprofid = QLabel("ID DE USUARIO", self)
        labelprofid.move(60, 170)

        frameprofid = QFrame(self)
        frameprofid.setFrameShape(QFrame.StyledPanel)
        frameprofid.setFixedWidth(280)
        frameprofid.setFixedHeight(28)
        frameprofid.move(60, 196)

        imagenprofid = QLabel(frameprofid)
        imagenprofid.setPixmap(QPixmap("usuario.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
        imagenprofid.move(10, 4)

        self.lineEditprofid = QLineEdit(frameprofid)
        self.lineEditprofid.setFrame(False)
        self.lineEditprofid.setReadOnly(True)
        self.lineEditprofid.setTextMargins(8, 0, 4, 1)
        self.lineEditprofid.setFixedWidth(238)
        self.lineEditprofid.setFixedHeight(26)
        self.lineEditprofid.move(40, 1)
        self.lineEditprofid.setInputMask("99999")

      # ================== WIDGETS QPUSHBUTTON ===================

        buttoncrear = QPushButton("CREAR CURSO", self)
        buttoncrear.setFixedWidth(135)
        buttoncrear.setFixedHeight(28)
        buttoncrear.move(60, 286)
        buttoncrear.clicked.connect(self.crearcurso)

        buttonCancelar = QPushButton("CANCELAR", self)
        buttonCancelar.setFixedWidth(135)
        buttonCancelar.setFixedHeight(28)
        buttonCancelar.move(205, 286)


        buttonCancelar.clicked.connect(self.close)

        






# ================================================================

if __name__ == '__main__':
    



    import sys
    
    aplicacion = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ventana = ventanaclase()
    ventana.initUI(ventanaclase)
    ventana.show()


    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Arial")

    aplicacion.setFont(fuente)




    sys.exit(aplicacion.exec_())
