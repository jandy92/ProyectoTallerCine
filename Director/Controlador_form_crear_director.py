#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Crear_director import Ui_formulario_crear
import Modelo_director

class Controlador_form_crear_director(QtGui.QMainWindow):
	
    def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui=Ui_formulario_crear()
		self.ui.setupUi(self)
		self.show()
		self.signals()
		self.nombre=""
		self.imagen=""
		self.nacimiento=""
		self.defuncion=""
		self.pais=""

    def signals(self):
    	self.ui.difunto_check.clicked.connect(self.difunto_check_clicked)


    def difunto_check_clicked(self):#si "difunto" esta chequeado activa el ingreso de fecha de defuncion, de lo contrario, la desactiva
    	#print(self.ui.difunto_check.isChecked())
    	self.ui.defuncion_in.setEnabled(self.ui.difunto_check.isChecked())
    	self.obtener_datos()

    def obtener_datos(self):
    	self.nombre=self.ui.nombre_in.text()#obligatorio
    	self.pais=self.ui.pais_in.text()#obligatorio
    	self.nacimiento=self.ui.nacimiento_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
    	self.defuncion=self.ui.defuncion_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
    	#print(self.nacimiento)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Controlador_form_crear_director()
    sys.exit(app.exec_())