# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdfsmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql.cursors



global conn,cur,data
conn = pymysql.connect(host='localhost',user='root', password='axel', db='educativa')
cur = conn.cursor()


class Ui_usermenupdf(object):

    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.setText(message)
        mess.exec_()    



    def tablapdf(self):








        userid = self.usuarionick.text()
        materianombre = self.combocurso.currentText() 

     

        data = cur.execute("SELECT claseid,clasenombre,pdfnombre,pdfarchivo from clases,clasesuser,users,pdfs where userid2 = %s and claseid = claseid2 and clasenombre = %s and clasenombre = pdfclasenombre;",(userid,materianombre))      
        conn.commit()

        if(data):
            self.messagebox("ANUNCIO","ARCHIVOS ENCONTRADOS")



        self.tableWidget.setRowCount(0)
        for row, form in enumerate(cur):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                print(str(item))
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))







    def clasecombo(self):
        global materias, i


        profid2 = self.usuarionick.text()



        data = cur.execute("SELECT usernombre,clasenombre from clases,clasesuser,users where userid2 = %s and claseid2 = claseid",(profid2))

        materias = cur.fetchall()
        

        i = 0
        while i < len(materias):
            self.combocurso.addItem(materias[i][1])

            i = i + 1
            self.combocurso.setCurrentIndex(-1)





    def setupUi(self, usermenupdf):
        usermenupdf.setObjectName("usermenupdf")
        usermenupdf.setWindowModality(QtCore.Qt.WindowModal)
        usermenupdf.resize(500, 500)
        usermenupdf.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(usermenupdf)
        self.centralwidget.setObjectName("centralwidget")
        self.combocurso = QtWidgets.QComboBox(self.centralwidget)
        self.combocurso.setGeometry(QtCore.QRect(10, 100, 141, 22))
        self.combocurso.setObjectName("combocurso")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 220, 461, 231))
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
        self.usuarionick.setGeometry(QtCore.QRect(10, 160, 141, 22))
        self.usuarionick.setObjectName("usuarionick")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 531, 81))
        self.frame.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 30, 131, 21))
        self.label.setStyleSheet("font: 87 11pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(170, 100, 31, 23))
        self.update.setStyleSheet("")
        self.update.setText("")
        self.update.clicked.connect(self.tablapdf)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update.setIcon(icon)
        self.update.setObjectName("update")
        self.frame.raise_()
        self.combocurso.raise_()
        self.tableWidget.raise_()
        self.usuarionick.raise_()
        self.update.raise_()
        usermenupdf.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(usermenupdf)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        usermenupdf.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(usermenupdf)
        self.statusbar.setObjectName("statusbar")
        usermenupdf.setStatusBar(self.statusbar)

        self.retranslateUi(usermenupdf)
        QtCore.QMetaObject.connectSlotsByName(usermenupdf)

    def retranslateUi(self, usermenupdf):
        _translate = QtCore.QCoreApplication.translate
        usermenupdf.setWindowTitle(_translate("usermenupdf", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("usermenupdf", "CURSO ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("usermenupdf", "CURSO"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("usermenupdf", "NOMBRE PDF"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("usermenupdf", "ARCHIVO"))
        self.label.setText(_translate("usermenupdf", "MIS CURSOS"))
        self.usuarionick.setInputMask(_translate("usermenupdf", "99999999999"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    usermenupdf = QtWidgets.QMainWindow()
    ui = Ui_usermenupdf()
    ui.setupUi(usermenupdf)
    usermenupdf.show()
    sys.exit(app.exec_())

