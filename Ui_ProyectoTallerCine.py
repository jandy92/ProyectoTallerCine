# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProyectoTallerCine2.ui'
#
# Created: Tue Sep  1 05:53:56 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Director = QtGui.QPushButton(Form)
        self.Director.setGeometry(QtCore.QRect(70, 170, 101, 29))
        self.Director.setObjectName("Director")
        self.Actores = QtGui.QPushButton(Form)
        self.Actores.setGeometry(QtCore.QRect(70, 240, 106, 29))
        self.Actores.setObjectName("Actores")
        self.Peliculas = QtGui.QPushButton(Form)
        self.Peliculas.setGeometry(QtCore.QRect(230, 210, 106, 29))
        self.Peliculas.setObjectName("Peliculas")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.Director.setText(QtGui.QApplication.translate("Form", "Director", None, QtGui.QApplication.UnicodeUTF8))
        self.Actores.setText(QtGui.QApplication.translate("Form", "Actores", None, QtGui.QApplication.UnicodeUTF8))
        self.Peliculas.setText(QtGui.QApplication.translate("Form", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))

