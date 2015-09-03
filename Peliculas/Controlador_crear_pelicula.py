#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from crear_pelicula import Ui_formulario_crear
import Modelo_pelicula
class Controlador_form_crear_pelicula(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui=Ui_formulario_crear()
        self.ui.setupUi(self)
        #self.show()
        self.nombre=""
        self.imagen=""
        self.estreno=""
        self.pais=""
        self.signals()

    def signals(self):
        pass


    def obtener_datos(self):
        pass
        """
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
        #print(len(self.nacimiento))
        if(len(self.nombre)!=0 and len(self.nacimiento)!=0):#True: si los campos obligatorios estan definidos, False: si no
            self.listo=True
        """
        
    def crear_director(self):
        pass
        """
        self.obtener_datos()
        if(self.listo==True and Modelo_director.checkea_director(self.nombre)==False):#si los campos obligatorios tienen datos, se crea el director
            print("Creando nuevo director ...")
                           #crear_director(nombre, pais, fecha_nacimiento,fecha_defuncion):
            Modelo_director.crear_director(self.nombre,self.pais,self.nacimiento,self.defuncion,"Director/img/"+self.nombre.replace(" ","_")+".jpg")
            self.ui.foto_label.pixmap().save("Director/img/"+self.nombre.replace(" ","_")+".jpg","jpg")#guarda la imagen que se selecciono a la carpeta "img"
            self.limpiar()
            self.close()
        else:#si falta algun campo obligatorio, no se creara el nuevo director
            if(len(self.nombre)>0):
                QtGui.QMessageBox.critical(self, "Director Existente","Error:\nEL director que intenta agregar ("+self.nombre+"), ya existe en la base de datos")
            else:
                QtGui.QMessageBox.critical(self, 'Faltan campos obligatorios','Error:\nLos campos "nombre" y "fecha de nacimiento" son obligatorios')
        """

    def cargar_imagen(self):
        print("cargar imagen")
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de director',None,
        "Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
        print (fileName[0])
        self.ui.foto_label.setPixmap(QtGui.QPixmap(fileName[0]))

    def cancelar(self):
	self.limpiar()
        self.close()

    def limpiar(self):#"limpia" el formulario
        pass
        """
        self.ui.nombre_in.setText("")
        self.ui.pais_in.setText("")
        self.ui.difunto_check.setChecked(False)
        self.ui.defuncion_in.setEnabled(False)
        self.ui.foto_label.setPixmap(QtGui.QPixmap("Director/img/0.jpg"))
        """
