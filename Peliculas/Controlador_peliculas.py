#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Peliculas_ui import Ui_Ventana_peliculas
from Controlador_crear_pelicula import Controlador_form_crear_pelicula
import Modelo_pelicula

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
	self.cargar_peliculas();
	#self.show()
	self.crear=Controlador_form_crear_pelicula()
	#self.editar=Editar.Editar()
	self.signals()
	       
    
    def signals(self):
        self.ui.boton_crear_pelicula.clicked.connect(self.mostrar_ventana_agregar)
        self.ui.grilla.clicked.connect(self.mostrar_imagen)

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
        # Ahora la imagen
        img = QtGui.QPixmap(str(peli['imagen']))
        print(str(peli['imagen']))
        self.ui.label_imagen.setPixmap(img)

    def elimina(self):
        pass
        """
	index =self.ui.grilla.currentIndex()
	data = self.ui.grilla.model()
	dire = data.item(index.row(),0).dire
	iD = str(dire['id'])
	Modelo_director.borrar(iD);
	self.cargar_directores();
	#print(str(dire['imagen'])[1:])
	#self.ui.imagen.setPixmap(img)
        """


    def mostrar_ventana_agregar(self):
        self.crear.show()
        
    
    def editar_director(self):
        """
        pass
      	index = self.ui.grilla.currentIndex()
	data = self.ui.grilla.model()
	dire = data.item(index.row(),0).dire
	id=dire['id']
	print(id)
	self.editar.setID(id)
	self.editar.show()
	"""


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Pelicula()
    sys.exit(app.exec_())

