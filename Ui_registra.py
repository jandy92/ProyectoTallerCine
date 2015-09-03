# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registra.ui'
#
# Created: Thu Sep  3 20:11:44 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Registra(object):
    def setupUi(self, Registra):
        Registra.setObjectName("Registra")
        Registra.resize(507, 273)
        self.usuario = QtGui.QLabel(Registra)
        self.usuario.setGeometry(QtCore.QRect(40, 40, 67, 17))
        self.usuario.setObjectName("usuario")
        self.contrasea = QtGui.QLabel(Registra)
        self.contrasea.setGeometry(QtCore.QRect(40, 90, 81, 17))
        self.contrasea.setObjectName("contrasea")
        self.nuevo_usuario_in = QtGui.QLineEdit(Registra)
        self.nuevo_usuario_in.setGeometry(QtCore.QRect(150, 40, 291, 27))
        self.nuevo_usuario_in.setObjectName("nuevo_usuario_in")
        self.nueva_contrasea_in = QtGui.QLineEdit(Registra)
        self.nueva_contrasea_in.setGeometry(QtCore.QRect(150, 90, 291, 27))
        self.nueva_contrasea_in.setObjectName("nueva_contrasea_in")
        self.boton_ingresar = QtGui.QPushButton(Registra)
        self.boton_ingresar.setGeometry(QtCore.QRect(180, 200, 161, 27))
        self.boton_ingresar.setObjectName("boton_ingresar")
        self.contrasea_2 = QtGui.QLabel(Registra)
        self.contrasea_2.setGeometry(QtCore.QRect(40, 140, 81, 41))
        self.contrasea_2.setObjectName("contrasea_2")
        self.nueva_contrasea2_in = QtGui.QLineEdit(Registra)
        self.nueva_contrasea2_in.setGeometry(QtCore.QRect(150, 150, 291, 27))
        self.nueva_contrasea2_in.setObjectName("nueva_contrasea2_in")

        self.retranslateUi(Registra)
        QtCore.QMetaObject.connectSlotsByName(Registra)

    def retranslateUi(self, Registra):
        Registra.setWindowTitle(QtGui.QApplication.translate("Registra", "Registrar usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.usuario.setText(QtGui.QApplication.translate("Registra", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.contrasea.setText(QtGui.QApplication.translate("Registra", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_ingresar.setText(QtGui.QApplication.translate("Registra", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.contrasea_2.setText(QtGui.QApplication.translate("Registra", "Reingresar\n"
"contraseña", None, QtGui.QApplication.UnicodeUTF8))

