#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Peliculas_ui import Ui_Ventana_peliculas
from Controlador_crear_pelicula import Controlador_form_crear_pelicula
from Editar_pelicula import  Ui_formulario_editar
import Modelo_pelicula
import Editar

class Pelicula (QtGui.QMainWindow):
    table_columns = (
	(u"ID",0),
	(u"Nombre", 150),
	(u"Estreno", 150),
	(u"Pais", 150),
	(u"Descripcion", 150))

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
	self.ui = Ui_Ventana_peliculas()
	self.ui.setupUi(self)
	self.cargar_peliculas()
        self.ui.label_reparto.setText("")
        self.ui.label_imagen.setText("")
        self.ui.label_descripcion.setText("")
	#self.show()
	self.crear=Controlador_form_crear_pelicula()
	self.ui.reparto.setText("Cantidad de actores: ")
	self.editar=Editar.Editar()
	self.signals()
	
    def signals(self):
        self.editar.ui.editar_boton.clicked.connect(self.cargar_peliculas)
        self.ui.boton_editar_pelicula_.clicked.connect(self.editar_pelicula)
        self.ui.boton_crear_pelicula.clicked.connect(self.mostrar_ventana_agregar)
        self.ui.grilla.clicked.connect(self.mostrar_imagen)
        self.ui.boton_eliminar_pelicula.clicked.connect(self.elimina)
        self.crear.ui.crear_boton.clicked.connect(self.cargar_peliculas)
        self.ui.boton_filtro_actor.clicked.connect(self.filtro_actor)

    def cargar_peliculas(self):
        peliculas=Modelo_pelicula.obtener_peliculas()
	filas=len(peliculas)
	data = QtGui.QStandardItemModel(filas, len(self.table_columns))
	self.ui.grilla.setModel(data)
	self.ui.grilla.horizontalHeader().setResizeMode(0, self.ui.grilla.horizontalHeader().Stretch)

	for col, h in enumerate(self.table_columns):
	    data.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
	    self.ui.grilla.setColumnWidth(col, h[1])
	    
	for i, peli in enumerate(peliculas):
	    filas = [peli["id"],
	        peli["nombre"], peli["estreno"],
	        peli["pais"],peli["descripcion"],peli["director_id"]]
	    for j, field in enumerate(filas):
	        index = data.index(i, j, QtCore.QModelIndex())
	        data.setData(index, field)
	        
	    # Parametros ocultos
	    data.item(i).peli = peli
    
    def mostrar_imagen(self,index):
        index = index if index is not None\
            else self.ui.grilla.currentIndex()
        if index.row() == -1:
            QtGui.QMessageBox.information(
                None,
                u"Información",
                u"Por favor seleccione una orden de trabajo.")
            return
      
        data = self.ui.grilla.model()
        peli = data.item(index.row(), 0).peli
        actores=self.sum_actores(peli["id"])
        actores=str(actores)
        self.ui.label_reparto.setText(actores)
        self.ui.label_descripcion.setText(peli["descripcion"])  #recordar cambiar el label.setWordWrap True para reparto :D
        # Ahora la imagen
        img = QtGui.QPixmap(peli['imagen'])  #str[mov[poster]] da el nombre del archivo para luego usarlo como una imagen
        self.ui.label_imagen.setPixmap(img)
    
    def sum_actores(self,id_p):  #recorre la query como diccionario para luego contar los actores
        c=0
        peliculas = Modelo_pelicula.contar_actor(id_p) 
        for i, peli in enumerate(peliculas):
            c=c+1
        return(c)

    def elimina(self):              
	index =self.ui.grilla.currentIndex()
	data = self.ui.grilla.model()
	peli = data.item(index.row(),0).peli
	iD = str(peli['id'])
	Modelo_pelicula.borrar(iD);
	self.cargar_peliculas();
	#print(str(dire['imagen'])[1:])
	#self.ui.imagen.setPixmap(img)
      

    def mostrar_ventana_agregar(self):
        self.crear.show()
    
    def filtro_actor(self):
        actor=self.ui.filtro_actor.text()
        peliculas = Modelo_pelicula.filtro_pelicula(actor)
        rows = len(peliculas)
        if rows == 0:
            QtGui.QMessageBox.information(
                None,
                u"Información",
                u"No se encontro nigun actor en las peliculas.")
            return
        data = QtGui.QStandardItemModel(
            rows, len(self.table_columns))
        self.ui.grilla.setModel(data)
        self.ui.grilla.horizontalHeader().setResizeMode(
            0, self.ui.grilla.horizontalHeader().Stretch)

        for col, h in enumerate(self.table_columns):
            data.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.grilla.setColumnWidth(col, h[1])

        for i, peli in enumerate(peliculas):
            row = [
                peli["nombre"], peli["estreno"], peli["pais"],  # cambiar lo que esta dentro del parentesis dependiendo de la tabla
                peli["descripcion"], peli["director_id"]]
            for j, field in enumerate(row):
                index = data.index(i, j, QtCore.QModelIndex())
                data.setData(index, field)
            # Parametros ocultos
            data.item(i).peli = peli
        
    
    def editar_pelicula(self):             
      	index = self.ui.grilla.currentIndex()
	data = self.ui.grilla.model()
	peli = data.item(index.row(),0).peli
	id=peli['id']
	print(id)
	self.editar.setID(id)
	self.editar.show()
	


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Pelicula()
    sys.exit(app.exec_())

