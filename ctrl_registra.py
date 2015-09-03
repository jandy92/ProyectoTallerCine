#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Ui_registra import Ui_Registra
import Modelo_registra

class registra(QtGui.QMainWindow):

    def __init__(self, parent=None):
	QtGui.QMainWindow.__init__(self, parent)
	self.ui = Ui_Registra()
	self.ui.setupUi(self)
	self.show()
	self.signals()

    def signals(self):
	self.ui.boton_ingresar.clicked.connect(self.regiatrando)

    def regiatrando(self):
	#guarda nuevo usuario en base de datos
	self.usuario = self.ui.nuevo_usuario_in.text()
	self.clave = self.ui.nueva_contrasea_in.text()
	print len(self.usuario)
	print len(self.clave)
	if(len(self.usuario)>0 and len(self.clave)>0):
		Modelo_registra.agrega_usuario(self.usuario, self.clave)
		QtGui.QMessageBox.critical(self, "Se guardaron los datos","Exito:\nSe han guardado los datos correctamente.")
		self.close()
		self.limpiar()
	
	else:
		QtGui.QMessageBox.critical(self, "Faltan datos","Error:\nNo ha ingresado todos los datos requeridos.")




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = registra()
    sys.exit(app.exec_())
