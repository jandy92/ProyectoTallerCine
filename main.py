#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Ui_login import Ui_Form
#from Ui_registra import Ui_Registra
from ctrl_registra import registra
from Ctrl_cine import cine
import Modelo_main
import Modelo_registra

class login(QtGui.QMainWindow):
	
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
	self.ui = Ui_Form()
	self.ui.setupUi(self)
	self.dialogo_cine=cine()
	self.diag_crea=registra()
	self.show()
	self.signals()

    def signals(self):
        """
        Conecta la base de datos con el codigo
        """
	self.ui.boton_login.clicked.connect(self.hacer_login)
	self.ui.boton_registrar.clicked.connect(self.hacer_registro)


    def hacer_login(self):
	"""
	comprueba si el usuario y su clave coinciden con la base de datos
	"""
	self.nombre=self.ui.usuario_in.text()
	self.clave=self.ui.contrasea_in.text()
	self.clave_compara=""
	if(len(self.nombre)>0):
            if(len(self.clave)>0):
                    #si el usuario esta en la base de datos
                    if (Modelo_main.usuario_existe(self.nombre)):
                            self.clave_compara = Modelo_main.obtener_clave(self.nombre)
                            if(self.clave_compara == self.clave):
                                    self.dialogo_cine.show();
                                    self.close()
                    else:
                            QtGui.QMessageBox.critical(self, "No existe usuario","Error:\nEl usuario no existe en la base de datos.")
            else:
                QtGui.QMessageBox.critical(self, u"Ingrese una contraseña",u"Error:\nDebe ingresar una contraseña.")
        else:
                QtGui.QMessageBox.critical(self, "Ingrese un nombre de usuario","Error:\nDebe ingresar un nombre de usuario.")


    def hacer_registro(self):
        self.diag_crea.show()
	
	

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = login()
    sys.exit(app.exec_())
