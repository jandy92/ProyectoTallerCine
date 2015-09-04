#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Ui_registra import Ui_Registra
import Modelo_registra
import Modelo_main

class registra(QtGui.QMainWindow):

    def __init__(self, parent=None):
	QtGui.QMainWindow.__init__(self, parent)
	self.ui = Ui_Registra()
	self.ui.setupUi(self)
	#self.show()
	self.signals()

    def signals(self):
	self.ui.boton_ingresar.clicked.connect(self.registrando)

    def registrando(self):
	#guarda nuevo usuario en base de datos
	registrado=False
	self.usuario = self.ui.nuevo_usuario_in.text()
	self.clave = self.ui.nueva_contrasea_in.text()
	self.clave2 = self.ui.nueva_contrasea2_in.text()
	print len(self.usuario)
	print len(self.clave)
        if(len(self.usuario)>0):
            if(len(self.clave)>0):
                if(len(self.clave2)>0):
                    if(self.clave==self.clave2):
                        if(Modelo_main.usuario_existe(self.usuario)==False):
                            Modelo_registra.agrega_usuario(self.usuario, self.clave)
                            QtGui.QMessageBox.critical(self, "Se guardaron los datos","Exito:\nSe han guardado los datos correctamente.")
                            self.close()
                            #self.limpiar()
                        else:
                            QtGui.QMessageBox.critical(self, u"Usuario ya existe",u"Error:\nEl usuario ingresado ya está ingresado en la base de datos.")
                    else:
                        QtGui.QMessageBox.critical(self, u"Contraseñas no coinciden",u"Error:\nLas contraseñas ingresadas deben ser identicas.")
                        
                else:
                    QtGui.QMessageBox.critical(self, u"Ingrese una contraseña",u"Error:\nDebe reingresar la contraseña.")
            
            else:
                QtGui.QMessageBox.critical(self, u"Ingrese una contraseña",u"Error:\nDebe ingresar una contraseña.")
        else:
                QtGui.QMessageBox.critical(self, "Ingrese un nombre de usuario","Error:\nDebe ingresar un nombre de usuario.")	
        
	
	







if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = registra()
    sys.exit(app.exec_())
