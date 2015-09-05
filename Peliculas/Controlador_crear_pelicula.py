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
        self.descripcion=""
        self.director_id=""
        self.signals()
        self.listo=False

    def signals(self):
        """
        Conecta la base de datos con el codigo
        """
        self.ui.crear_boton.clicked.connect(self.crear_pelicula)
        self.ui.boton_foto.clicked.connect(self.cargar_imagen)
        self.ui.cancelar_boton.clicked.connect(self.cancelar)
        self.ui.limpiar_boton.clicked.connect(self.limpiar)


    def obtener_datos(self):
        """
        Retorna los datos de una pelicula con la id que recibe
        """
    
        self.nombre=""
        self.imagen=""
        self.estreno=""
        self.pais=""
        self.descripcion=""
        self.director_id=""
        self.nombre=self.ui.nombre_in.text()#obligatorio
        self.pais=self.ui.pais_in.text()#obligatorio
        self.estreno=self.ui.fecha_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
        self.descripcion=self.ui.descripcion_in.toPlainText()
        if(len(self.nombre)!=0 and len(self.descripcion)!=0 and len(self.pais)!=0 and len(self.estreno)!=0):#True: si los campos obligatorios estan definidos, False: si no
            self.listo=True
            
    def crear_pelicula(self):
        """
        Crea una nueva pelicula en la base de datos
        """
        self.obtener_datos()
        if(len(self.ui.nombre_in.text())>0 and len(self.ui.fecha_in.date().toPython().strftime("%Y-%m-%d"))>0 and len(self.ui.pais_in.text())>0 and len(self.ui.descripcion_in.toPlainText())>0 and Modelo_pelicula.checkea_pelicula(self.nombre)==False):#si los campos obligatorios tienen datos, se crea la pelicula
            print("Creando nueva pelicula ...")
                           #crear_pelicula(nombre,estreno, pais, descripcion, director_id)
            Modelo_pelicula.crear_pelicula(self.nombre,self.estreno, self.pais, self.descripcion,"Peliculas/img/"+self.nombre.replace(" ","_")+".jpg")
            self.ui.foto_label.pixmap().save("Peliculas/img/"+self.nombre.replace(" ","_")+".jpg","jpg")#guarda la imagen que se selecciono a la carpeta "img"
            self.limpiar()
            self.close()
        else:#si falta algun campo obligatorio, no se creara el nuevo director           
            QtGui.QMessageBox.critical(self, 'Faltan campos obligatorios','Error:\nLos campos "nombre", "estreno","pais y  descripcion" son campos obligatorios')
       
    def cargar_imagen(self):
        """
        Carga la imagen que es seleccionada por el usuario
        """
        print("cargar imagen")
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de la pelicula',None,
        "Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
        print (fileName[0])
        self.ui.foto_label.setPixmap(QtGui.QPixmap(fileName[0]))

    def cancelar(self):
        """
        Limpia y cierra la ventana
        """
	self.limpiar()
        self.close()

    def limpiar(self):
        """
        "limpia" el formulario
        """
        self.ui.nombre_in.setText("")
        self.ui.pais_in.setText("")
        self.ui.descripcion_in.setText("")
        self.ui.foto_label.setPixmap(QtGui.QPixmap("Peliculas/img/0.jpg"))
      
