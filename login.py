import pymysql.cursors


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
							 QPushButton)

import sys
from menu import *
from menuprof import *
from registro import *






global lineEditUsuario

class ventanaLogin(QMainWindow,object):

	def openregistro(self):

		self.window = QtWidgets.QMainWindow()
		self.ventana = registro()
		self.ventana.initUI(self)
		self.ventana.show()


	

	def messagebox(self,title,message):
		mess=QtWidgets.QMessageBox()
		mess.setWindowTitle(title)
		mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
		mess.setText(message)
		mess.exec_()    


	def openmenuprof(self):
	  self.window = QtWidgets.QMainWindow()
	  self.ui = menuprofesor()
	  self.ui.setupUI(self.window)
	  self.ui.show()
			

	def openprincipal(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_animarBotones()
		self.ui.setupUI(self.window)
		self.ui.show()
		


	def checklogin(self):
		global lineEditUsuario
		


		usuario = self.lineEditUsuario.text()
		contra = self.lineEditContrasenia.text()

		
		try:
			global conn,cur,data
			conn = pymysql.connect(host='localhost',user='root', password='axel', db='educativa')
			cur = conn.cursor()
		
			if(self.comboBoxCuenta.currentText() == 'Usuario'):
				data = cur.execute("SELECT UserNick, UserPass FROM users WHERE UserNick = %s and UserPass = %s ",(usuario,contra))    
				conn.commit()
				if(data):
					self.openprincipal()
					self.ui.lineEditUsuario1.setText(usuario)

				else:
					self.messagebox("ANUNCIO","CONTRASEÑA O USUARIO INVALIDOS")   

			if(self.comboBoxCuenta.currentText() == ''):
				self.messagebox("ANUNCIO","ELIJA EL TIPO DE CUENTA") 

		


			if(self.comboBoxCuenta.currentText() == 'Profesor'):
				data = cur.execute("SELECT ProfesorNick, ProfesorPass FROM profesor WHERE ProfesorNick = %s and ProfesorPass = %s",(usuario,contra))       
				if(data):
					self.openmenuprof()
					self.ui.lineEditUsuario2.setText(usuario)
				else:
					self.messagebox("ANUNCIO","CONTRASEÑA O USUARIO INVALIDOS")     

		except:
			print("error")                   


	def __init__(self, parent=None):
		super(ventanaLogin, self).__init__(parent)
		
		self.setWindowTitle("BIENVENIDOS")
		self.setWindowIcon(QIcon("icono.jpg"))
		self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
		self.setFixedSize(400, 380)

		paleta = QPalette()
		paleta.setColor(QPalette.Background, QColor(243, 243, 243))
		self.setPalette(paleta)

		self.initUI()

	def initUI(self):

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
		labelIcono.setPixmap(QPixmap("icono.jpg").scaled(40, 40, Qt.KeepAspectRatio,
														 Qt.SmoothTransformation))
		labelIcono.move(37, 22)

		fuenteTitulo = QFont()
		fuenteTitulo.setPointSize(16)
		fuenteTitulo.setBold(True)

		labelTitulo = QLabel("<font color='white'>PLATAFORMA EDUCATIVA</font>", frame)
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

		# ========================================================

		labelUsuario = QLabel("Usuario", self)
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

		# ========================================================

		labelContrasenia = QLabel("Contraseña", self)
		labelContrasenia.move(60, 224)

		frameContrasenia = QFrame(self)
		frameContrasenia.setFrameShape(QFrame.StyledPanel)
		frameContrasenia.setFixedWidth(280)
		frameContrasenia.setFixedHeight(28)
		frameContrasenia.move(60, 250)

		imagenContrasenia = QLabel(frameContrasenia)
		imagenContrasenia.setPixmap(QPixmap("contraseña.png").scaled(20, 20, Qt.KeepAspectRatio,
																	 Qt.SmoothTransformation))
		imagenContrasenia.move(10, 4)

		self.lineEditContrasenia = QLineEdit(frameContrasenia)
		self.lineEditContrasenia.setFrame(False)
		self.lineEditContrasenia.setEchoMode(QLineEdit.Password)
		self.lineEditContrasenia.setTextMargins(8, 0, 4, 1)
		self.lineEditContrasenia.setFixedWidth(238)
		self.lineEditContrasenia.setFixedHeight(26)
		self.lineEditContrasenia.move(40, 1)



		buttonLogin = QPushButton("Iniciar sesión", self)
		buttonLogin.setFixedWidth(135)
		buttonLogin.setFixedHeight(28)
		buttonLogin.move(60, 286)
		buttonLogin.clicked.connect(self.checklogin)

		buttonCancelar = QPushButton("Registrarse", self)
		buttonCancelar.setFixedWidth(135)
		buttonCancelar.setFixedHeight(28)
		buttonCancelar.move(205, 286)
		buttonCancelar.clicked.connect(self.openregistro)






		





# ================================================================

if __name__ == '__main__':
	
	import sys
	
	aplicacion = QApplication(sys.argv)

	fuente = QFont()
	fuente.setPointSize(10)
	fuente.setFamily("Bahnschrift Light")

	aplicacion.setFont(fuente)
	
	ventana = ventanaLogin()
	ventana.show()
	
	sys.exit(aplicacion.exec_())