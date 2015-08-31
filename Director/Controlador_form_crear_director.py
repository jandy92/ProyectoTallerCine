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
		self.listo=False;#True: los datos obligatorios existen, False:si no
		self.nombre=""
		self.imagen=""
		self.nacimiento=""
		self.defuncion=""
		self.pais=""
		self.signals()

    def signals(self):
    	self.ui.boton_foto.clicked.connect(self.cargar_imagen)
    	self.ui.difunto_check.clicked.connect(self.difunto_check_clicked)
    	self.ui.crear_boton.clicked.connect(self.crear_director)

    def difunto_check_clicked(self):#si "difunto" esta chequeado activa el ingreso de fecha de defuncion, de lo contrario, la desactiva
    	#print(self.ui.difunto_check.isChecked())
    	self.ui.defuncion_in.setEnabled(self.ui.difunto_check.isChecked())

    def obtener_datos(self):
    	self.nombre=""
    	self.imagen=""
    	self.nacimiento=""
    	self.defuncion=""
    	self.pais=""
    	self.nombre=self.ui.nombre_in.text()#obligatorio
    	self.pais=self.ui.pais_in.text()#obligatorio
    	self.nacimiento=self.ui.nacimiento_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
    	if(self.ui.difunto_check.isChecked()):
    		self.defuncion=self.ui.defuncion_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
    	self.listo=False
    	print(len(self.nacimiento))
    	if(len(self.nombre)!=0 and len(self.nacimiento)!=0):#True: si los campos obligatorios estan definidos, False: si no
    		self.listo=True

    def crear_director(self):
    	self.obtener_datos()
    	if(self.listo==True):#si los campos obligatorios tienen datos, se crea el director
    		print("Creando nuevo director ...")
    		               #crear_director(nombre, pais, fecha_nacimiento,fecha_defuncion):
    		Modelo_director.crear_director(self.nombre,self.pais,self.nacimiento,self.defuncion,"img/"+self.nombre.replace(" ","_")+".jpg")
    		self.ui.foto_label.pixmap().save("img/"+self.nombre.replace(" ","_")+".jpg","jpg")
    	else:#si falta algun campo obligatorio, no se creara el nuevo director
    		print("Faltan datos obligatorios, no se ha creado un nuevo director.")

    def cargar_imagen(self):
    	print("cargar imagen")
    	fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de director',None,
    	"Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
    	print (fileName[0])
    	#img = QtGui.QPixmap(fileName)
        self.ui.foto_label.setPixmap(QtGui.QPixmap(fileName[0]))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Controlador_form_crear_director()
    sys.exit(app.exec_())