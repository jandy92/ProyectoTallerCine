#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Ui_editar_actor import Ui_editar_actor
import Modelo_actor

class Editar(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_editar_actor()
        self.ui.setupUi(self)
        #self.show()
        self.signals()
        self.nombre=""
        self.birthday=""
	self.genero=""
	self.imagen=""
        self.id=0

    def signals(self):
        self.ui.boton_imagen.clicked.connect(self.cargar_imagen)
        self.ui.boton_guardar.clicked.connect(self.guardar_actor)
        self.ui.boton_cancelar.clicked.connect(self.cancelar)
        self.ui.boton_limpiar.clicked.connect(self.limpiar)
    
    def setID(self,id):
      self.id=id
      self.obtener_datos();

    def obtener_datos(self):
        self.nombre=""
        self.birthday=""
	self.genero=""
	self.imagen=""
        self.ui.actor_id.setText("ID:XXXXXXXXXX")
        #self.datos
        if(self.id>=1):
	  self.datos=Modelo_actor.buscar_id(self.id)
	  #print(self.datos)
	  self.ui.actor_id.setText("ID:"+str(self.id))
	  self.ui.nombre_in.setText(self.datos[0])
	  y=int(self.datos[1][0:4])
	  m=int(self.datos[1][5:7])
	  d=int(self.datos[1][8:10])
	  self.ui.nacimiento_in.setDate(QtCore.QDate(y,m,d))#Y,M,D
	  self.ui.imagen_label.setPixmap(QtGui.QPixmap(self.datos[3]))
	  self.listo=True
	  


    def guardar_actor(self):
	print("Guardando actor modificado...")
        #self.obtener_datos()
        if(len(self.ui.nombre_in.text())>0 and Modelo_actor.checkea_actor(self.nombre)==False):#si los campos obligatorios tienen datos, se crea el director
	    self.ui.imagen_label.pixmap().save("Actor/img/"+self.nombre.replace(" ","_")+".jpg","jpg")#guarda la imagen que se selecciono a la carpeta "img"
            Modelo_actor.actualiza(self.id,self.ui.nombre_in.text(),self.ui.nacimiento_in.date().toPython().strftime("%Y-%m-%d"),self.ui.genero.currentText(),"Actor/img/"+self.nombre.replace(" ","_")+".jpg")
	    
            self.limpiar()
            self.close()
        else:#si falta algun campo obligatorio, no se creara el nuevo director
            if(len(self.nombre)>0):
                QtGui.QMessageBox.critical(self, "Actor Existente","Error:\nEL actor que intenta agregar ("+self.nombre+"), ya existe en la base de datos")
            else:
                QtGui.QMessageBox.critical(self, 'Faltan campos obligatorios','Error:\nLos campos "nombre" y "fecha de nacimiento" son obligatorios')


    
    def cargar_imagen(self):
        print("cargar imagen")
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de actor',None,
        "Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
        print (fileName[0])
        self.ui.imagen_label.setPixmap(QtGui.QPixmap(fileName[0]))

    def cancelar(self):
        self.close()
        self.limpiar()

    def limpiar(self):#"limpia" el formulario
        self.ui.nombre_in.setText("")
        self.ui.imagen_label.setPixmap(QtGui.QPixmap("Actor/img/0.jpg"))
       
"""
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Editar()
	main.show()
	main.obtener_datos(1)
	sys.exit(app.exec_())
"""

