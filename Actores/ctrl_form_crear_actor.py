#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Ui_crear_actor import Ui_crear_actor
import Modelo_actor

class ctrl_form_actor(QtGui.QMainWindow):
	
    def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui=Ui_crear_actor()
		self.ui.setupUi(self)
		self.show()
		self.listo=False;#True: los datos obligatorios existen, False:si no
		self.nombre=""
		self.birthday=""
		self.genero=""
		self.imagen=""
		self.signals()

    def signals(self):
    	self.ui.boton_imagen.clicked.connect(self.cargar_imagen)
    	#self.ui.check_hombre.clicked.connect(self.check_hombre_clicked)
    	#self.ui.check_mujer.connect(self.check_mujer_clicked)
    	self.ui.boton_crear.clicked.connect(self.boton_crear)
    	#self.ui.cancelar_boton.clicked.connect(self.lalala);
	"""
    def check_hombre_clicked(self):
    	self.ui.check_hombre.isChecked()

    def check_mujer_clicked(self):
    	self.ui.check_mujer.isChecked()
	"""
	
	def boton_crear(self):
		#graba la info en la base de datos.

	def obtener_datos(self):
    	self.nombre=""
		self.birthday=""
		self.genero=""
		self.imagen=""
    	self.nombre=self.ui.nombre_in.text()#obligatorio
    	self.nacimiento=self.ui.nacimiento_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
    	if(self.ui.check_hombre.isChecked()):
    		self.defuncion=self.ui.defuncion_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
    	self.listo=False
    	#print(len(self.nacimiento))
    	if(len(self.nombre)!=0 and len(self.nacimiento)!=0):#True: si los campos obligatorios estan definidos, False: si no
    		self.listo=True

    def crear_actor(self):
    	self.obtener_datos()
    	if(self.listo==True and Modelo_actor.checkea_actor(self.nombre)==False):#si los campos obligatorios tienen datos, se crea el director
    		print("Creando nuevo actor ...")
    		               
    		Modelo_actor.crear_actor(self.nombre,self.birthday,self.nacimiento,"img/"+self.nombre.replace(" ","_")+".jpg")
    		self.ui.imagen_label.pixmap().save("img/"+self.nombre.replace(" ","_")+".jpg","jpg")
    	else:#si falta algun campo obligatorio, no se creara el nuevo director
    		QtGui.QMessageBox.critical(self, "Director Existente","Error:\nEL director que intenta agregar ("+self.nombre+"), ya existe en la base de datos")

    def cargar_imagen(self):
    	print("cargar imagen")
    	fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de director',None,
    	"Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
    	print (fileName[0])
    	#img = QtGui.QPixmap(fileName)
        self.ui.foto_label.setPixmap(QtGui.QPixmap(fileName[0]))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = ctrl_form_actor()
    sys.exit(app.exec_())
