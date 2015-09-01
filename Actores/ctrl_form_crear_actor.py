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
	self.sexo=""
	self.imagen=""
	self.signals()

    def signals(self):  
    	self.ui.boton_imagen.clicked.connect(self.cargar_imagen)
    	self.ui.boton_crear.clicked.connect(self.crear_actor)
    	self.ui.boton_limpiar.clicked.connect(self.limpiar)
    	self.ui.boton_cancelar.clicked.connect(self.cancelar)
    

    def obtener_datos(self):
      self.listo = False
      self.nombre=""
      self.birthday=""
      self.sexo=""
      self.imagen=""
      self.nombre=self.ui.nombre_in.text()#obligatorio
      self.birthday=self.ui.nacimiento_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string1
      print str(self.ui.genero.currentText())
      print self.nombre
      self.sexo=self.ui.genero.currentText()
      if(len(self.nombre))>0:
	   self.listo=True
      if(len(self.nombre))<0:
	   QtGui.QMessageBox.critical(self, "No ha ingresado un numbre.")
      

    def crear_actor(self):
    	self.obtener_datos()
    	if(self.listo==True and Modelo_actor.checkea_actor(self.nombre)==False):#si los campos obligatorios tienen datos, se crea el director
    		print("Creando nuevo actor ...")
    		               
    		Modelo_actor.crear_actor(self.nombre,self.birthday,self.sexo,"img/"+self.nombre.replace(" ","_")+".jpg")
    		self.ui.imagen_label.pixmap().save("img/"+self.nombre.replace(" ","_")+".jpg","jpg")
    	else:#si falta algun campo obligatorio, no se creara el nuevo director
    		QtGui.QMessageBox.critical(self, "No hay nombre","Error:\nNo ha ingresado ningun nombre ")
    
    
    
    
    def cargar_imagen(self):
    	print("cargar imagen")
    	fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de director',None,
    	"Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
    	print (fileName[0])
    	#img = QtGui.QPixmap(fileName)
        self.ui.foto_label.setPixmap(QtGui.QPixmap(fileName[0]))
     
    def cancelar(self):
        self.close()
        self.limpiar()
    	
    def limpiar(self):#"limpia" el formulario
        self.ui.nombre_in.setText("")
        self.ui.imagen_label.setPixmap(QtGui.QPixmap("img/0.jpg"))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = ctrl_form_actor()
    sys.exit(app.exec_())
