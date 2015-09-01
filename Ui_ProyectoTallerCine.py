# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProyectoTallerCine2.ui'
#
# Created: Tue Sep  1 11:20:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Director = QtGui.QPushButton(Form)
        self.Director.setGeometry(QtCore.QRect(150, 230, 101, 29))
        self.Director.setObjectName("Director")
        self.Actores = QtGui.QPushButton(Form)
        self.Actores.setGeometry(QtCore.QRect(20, 230, 106, 29))
        self.Actores.setObjectName("Actores")
        self.Peliculas = QtGui.QPushButton(Form)
        self.Peliculas.setGeometry(QtCore.QRect(280, 230, 106, 29))
        self.Peliculas.setObjectName("Peliculas")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 80, 411, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 441, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Menú Principal", None, QtGui.QApplication.UnicodeUTF8))
        self.Director.setText(QtGui.QApplication.translate("Form", "Director", None, QtGui.QApplication.UnicodeUTF8))
        self.Actores.setText(QtGui.QApplication.translate("Form", "Actores", None, QtGui.QApplication.UnicodeUTF8))
        self.Peliculas.setText(QtGui.QApplication.translate("Form", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Sistemas de administracion de peliculas y sus elencos", None, QtGui.QApplication.UnicodeUTF8))

