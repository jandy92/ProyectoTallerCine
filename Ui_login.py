# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Thu Sep  3 00:48:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 273)
        self.usuario = QtGui.QLabel(Form)
        self.usuario.setGeometry(QtCore.QRect(40, 40, 67, 17))
        self.usuario.setObjectName("usuario")
        self.contrasea = QtGui.QLabel(Form)
        self.contrasea.setGeometry(QtCore.QRect(40, 120, 81, 17))
        self.contrasea.setObjectName("contrasea")
        self.boton_login = QtGui.QPushButton(Form)
        self.boton_login.setGeometry(QtCore.QRect(110, 190, 99, 27))
        self.boton_login.setObjectName("boton_login")
        self.usuario_in = QtGui.QLineEdit(Form)
        self.usuario_in.setGeometry(QtCore.QRect(150, 40, 291, 27))
        self.usuario_in.setObjectName("usuario_in")
        self.contrasea_in = QtGui.QLineEdit(Form)
        self.contrasea_in.setGeometry(QtCore.QRect(150, 110, 291, 27))
        self.contrasea_in.setObjectName("contrasea_in")
        self.boton_registrar = QtGui.QPushButton(Form)
        self.boton_registrar.setGeometry(QtCore.QRect(310, 190, 99, 27))
        self.boton_registrar.setObjectName("boton_registrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Menú Principal", None, QtGui.QApplication.UnicodeUTF8))
        self.usuario.setText(QtGui.QApplication.translate("Form", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.contrasea.setText(QtGui.QApplication.translate("Form", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_login.setText(QtGui.QApplication.translate("Form", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_registrar.setText(QtGui.QApplication.translate("Form", "Registrar", None, QtGui.QApplication.UnicodeUTF8))

