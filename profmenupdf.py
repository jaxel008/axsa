from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
                             QLabel, QLineEdit)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/dell/Desktop/PLATAFORMAEDUCATIVA/pdfsmenuprof.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from os import getcwd

import pymysql

import base64



global conn,cur

conn = pymysql.connect(host='localhost',user='root', password='axel', db='educativa')
cur = conn.cursor()

class Ui_menucursospdf(object):

    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.setText(message)
        mess.exec_()    



    def examinarpdf(self):
        global file   
        options = QFileDialog.Options()
        
        file, _ = QFileDialog.getOpenFileName(None,"EXAMINAR PDF", getcwd(),"PDF FILES (*.PDF)", options=options)

        if file:
            print("SE HA EXAMINADO")
            file = self.pdflink.setText(file)

    def guardarpdf(self):

        nombrefile = self.pdfnombre.text()

        idcurso = self.combocurso.currentText()
        
        file2 = self.pdflink.text()

        filename = self.pdfnombre.text()
        
                
        with open(file2, 'rb') as f:
            blob = base64.b64encode(f.read())
        text_file = open('test_blob.pdf', "wb")
        text_file.write(blob)
        text_file.close()
        f2 = [x.decode('utf8').strip() for x in f.readlines()]    

        with open('test_blob.pdf', 'r') as f:
            blob=f.read()
        blob2= base64.b64decode(blob)
        f2=text_file = open(filename + ".pdf",'wb')
        text_file.write(blob)
        text_file.close() 




            



        
        data = cur.execute("INSERT INTO PDFS (pdfnombre , pdfclasenombre ,PDFARCHIVO) VALUES (%s,%s,%s)",(nombrefile,idcurso,f2))
        conn.commit()
        if(data):
            self.messagebox("ANUNCIO","EL ARCHIVO SE HA SUBIDO \n CON EXITO")

        else:
            print("error")     

    def cargaridcurso(self):

        global materiaid
        profid3 = self.usuarionick.text()

        data = cur.execute("SELECT CLASEID, CLASENOMBRE FROM CLASES,PROFESOR WHERE profesorid = %s and profesorid = claseprofesorid",(profid3))          
        materiaid = cur.fetchall()

        e = 0

        

        self.cursoid.setText(str(materiaid[e][0]))



        e = e + 1


    

    def clasecombo(self):
        global materias, i


        profid2 = self.usuarionick.text()



        data = cur.execute("SELECT CLASEID,CLASENOMBRE FROM clases,profesor WHERE profesorid = %s and profesorid = claseprofesorid",(profid2))

        materias = cur.fetchall()
        

        i = 0
        while i < len(materias):
            self.combocurso.addItem(materias[i][1])

            i = i + 1
            self.combocurso.setCurrentIndex(-1)

    def tablapdf(self):








        userid = self.usuarionick.text()
        materianombre = self.combocurso.currentText() 

     

        data = cur.execute("SELECT pdfid,clasenombre,pdfnombre,pdfarchivo from pdfs,clases,profesor where profesorid = %s and clasenombre = %s and clasenombre = pdfclasenombre;",(userid,materianombre))      
        conn.commit()


        self.tableWidget.setRowCount(0)
        for row, form in enumerate(cur):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                print(str(item))
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))


        if (data):
            self.messagebox("ANUNCIO","INFORMACION ENCONTRADA")  

        else:
            self.messagebox("ANUNCIO","NO ENCONTRADO")


    def setupUi(self, menucursospdf):
        menucursospdf.setObjectName("menucursospdf")
        menucursospdf.setWindowModality(QtCore.Qt.WindowModal)
        menucursospdf.resize(500, 500)
        menucursospdf.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(menucursospdf)
        self.centralwidget.setObjectName("centralwidget")
        self.combocurso = QtWidgets.QComboBox(self.centralwidget)
        self.combocurso.setGeometry(QtCore.QRect(10, 80, 141, 22))
        self.combocurso.setObjectName("combocurso")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 220, 461, 231))
        self.tableWidget.setStyleSheet("font: 8pt \"Arial\";")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.usuarionick = QtWidgets.QLineEdit(self.centralwidget)
        self.usuarionick.setGeometry(QtCore.QRect(10, 130, 141, 22))
        self.usuarionick.setReadOnly(True)
        self.usuarionick.setObjectName("usuarionick")
        self.cursoid = QtWidgets.QLineEdit(self.centralwidget)
        self.cursoid.setGeometry(QtCore.QRect(10, 180, 141, 22))
        self.cursoid.setReadOnly(True)
        self.cursoid.setObjectName("cursoid")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -50, 531, 121))
        self.frame.setStyleSheet("background-color: rgb(85, 0, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(130, 60, 61, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("maestrocurso.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(220, 80, 181, 16))
        self.label_6.setStyleSheet("font: 87 15pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(170, 80, 31, 23))
        self.update.setStyleSheet("")
        self.update.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update.setIcon(icon)
        self.update.setObjectName("update")
        self.update.clicked.connect(self.tablapdf)
        self.pdflink = QtWidgets.QLineEdit(self.centralwidget)
        self.pdflink.setGeometry(QtCore.QRect(270, 100, 141, 22))
        self.pdflink.setObjectName("pdflink")
        self.pdfnombre = QtWidgets.QLineEdit(self.centralwidget)
        self.pdfnombre.setGeometry(QtCore.QRect(270, 150, 141, 22))
        self.pdfnombre.setObjectName("pdfnombre")
        self.buttonexaminar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonexaminar.setGeometry(QtCore.QRect(420, 100, 31, 23))
        self.buttonexaminar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("examinaricon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonexaminar.setIcon(icon1)
        self.buttonexaminar.setObjectName("buttonexaminar")
        self.buttonexaminar.clicked.connect(self.examinarpdf)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 80, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 130, 101, 16))
        self.label_4.setObjectName("label_4")
        self.buttonguardar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonguardar.setGeometry(QtCore.QRect(460, 100, 31, 23))
        self.buttonguardar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonguardar.setIcon(icon2)
        self.buttonguardar.setObjectName("buttonguardar")
        self.buttonguardar.clicked.connect(self.guardarpdf)
        self.frame.raise_()
        self.combocurso.raise_()

        self.tableWidget.raise_()
        self.usuarionick.raise_()
        self.cursoid.raise_()
        self.update.raise_()
        self.pdflink.raise_()
        self.pdfnombre.raise_()
        self.buttonexaminar.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.buttonguardar.raise_()
        menucursospdf.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menucursospdf)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        menucursospdf.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menucursospdf)
        self.statusbar.setObjectName("statusbar")
        menucursospdf.setStatusBar(self.statusbar)
        
        self.retranslateUi(menucursospdf)
        QtCore.QMetaObject.connectSlotsByName(menucursospdf)

    def retranslateUi(self, menucursospdf):
        _translate = QtCore.QCoreApplication.translate
        menucursospdf.setWindowTitle(_translate("menucursospdf", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("menucursospdf", "PDF ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("menucursospdf", "CURSO"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("menucursospdf", "NOMBRE PDF"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("menucursospdf", "ARCHIVO"))
        self.label_6.setText(_translate("menucursospdf", "MIS CURSOS"))
        self.label.setText(_translate("menucursospdf", "ID Usuario"))
        self.label_2.setText(_translate("menucursospdf", "ID Curso"))
        self.label_3.setText(_translate("menucursospdf", "Archivo PDF"))
        self.label_4.setText(_translate("menucursospdf", "Nombre del Archivo"))
        self.usuarionick.setInputMask(_translate("menucursospdf", "99999999999"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menucursospdf = QtWidgets.QMainWindow()
    ui = Ui_menucursospdf()
    ui.setupUi(menucursospdf)
    menucursospdf.show()
    sys.exit(app.exec_())

