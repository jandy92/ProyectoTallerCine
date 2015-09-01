#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Peliculas import Ui_Form
from formulario import Ui_Form_crear
import model   #cambiar el nombre del model conforme a lo que se necesite


class Movies(QtGui.QMainWindow):

    table_columns = (
        (u"Título", 200),
        (u"Estreno", 75),
        (u"Pais", 120),
        (u"Descripcion", 75),
        (u"Director_id", 60)) #por ahora, luego remplazar por solo director

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Form()
        self.dialogo=Controlador_form_crear()
        
        self.ui.setupUi(self)
        self.load_movies()
        #self.show()
        self.signals()
        self.ui.label_reparto.setText("")
        self.ui.label_imagen.setText("")
        self.ui.label_desc.setText("")
        self.ui.label_4.setText("Cantidad de actores: ")
    def signals(self):
        self.ui.grilla.clicked.connect(self.show_poster)
        self.ui.btn_eliminar.clicked.connect(self.delete)
        self.ui.btn_filtro.clicked.connect(self.load_filtered_movies)
        self.ui.btn_crear.clicked.connect(self.mostrar_ventana_agregar)

    def delete(self):
        index=self.ui.grilla.currentIndex()
        data = self.ui.grilla.model()
        mov = data.item(index.row(), 0).mov
        model.delete_movie(mov["nombre"])
        self.load_movies()
        return
    def show_poster(self, index):
        
        index = index if index is not None\
            else self.ui.grilla.currentIndex()
        if index.row() == -1:
            QtGui.QMessageBox.information(
                None,
                u"Información",
                u"Por favor seleccione una orden de trabajo.")
            return
      
        data = self.ui.grilla.model()
        mov = data.item(index.row(), 0).mov
        actores=self.sum_actores(mov["id"])
        actores=str(actores)
        self.ui.label_reparto.setText(actores)
        self.ui.label_desc.setText(mov["descripcion"])  #recordar cambiar el label.setWordWrap True para reparto :D
        # Ahora la imagen
        img = QtGui.QPixmap(mov['imagen'])  #str[mov[poster]] da el nombre del archivo para luego usarlo como una imagen
        self.ui.label_imagen.setPixmap(img)
    def sum_actores(self,id_p):  #recorre la query como diccionario para luego contar los actores
        contador_actores=0
        movies = model.actor_count(id_p) #cambiar el nombre del model dependiendo de lo que se necesite 
        for i, mov in enumerate(movies):
            contador_actores=contador_actores+1
        
        return(contador_actores)
    def load_movies(self):
        movies = model.get_movies() #cambiar el nombre del model dependiendo de lo que se necesite
        rows = len(movies)
        data = QtGui.QStandardItemModel(
            rows, len(self.table_columns))
        
        self.ui.grilla.setModel(data)
        self.ui.grilla.horizontalHeader().setResizeMode(
            0, self.ui.grilla.horizontalHeader().Stretch)

        for col, h in enumerate(self.table_columns):
            data.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.grilla.setColumnWidth(col, h[1])

        for i, mov in enumerate(movies):
            row = [
                mov["nombre"], mov["estreno"], mov["pais"],  # cambiar lo que esta dentro del parentesis dependiendo de la tabla
                mov["descripcion"], mov["director_id"]]
            for j, field in enumerate(row):
                index = data.index(i, j, QtCore.QModelIndex())
                data.setData(index, field)
            # Parametros ocultos
            data.item(i).mov = mov
    def load_filtered_movies(self):
        actor=self.ui.filtro_actor.text()
        movies = model.filter_movie(actor)
        
        rows = len(movies)
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

        for i, mov in enumerate(movies):
            row = [
                mov["nombre"], mov["estreno"], mov["pais"],  # cambiar lo que esta dentro del parentesis dependiendo de la tabla
                mov["descripcion"], mov["director_id"]]
            for j, field in enumerate(row):
                index = data.index(i, j, QtCore.QModelIndex())
                data.setData(index, field)
            # Parametros ocultos
            data.item(i).mov = mov
    def mostrar_ventana_agregar(self):
       self.dialogo.show();

class Controlador_form_crear(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui=Ui_Form_crear()
        self.ui.setupUi(self)
        #self.show()
        self.nombre=""
        self.fecha=""
        self.pais=""
        self.descripcion=""
        self.director=""
        self.nombre_actor=""
        self.personaje=""
        self.desc_actor=""
        self.listo=True
        self.listo_pelicula=False #  revisa si la pelicula fue creada para poder ingresar el elenco
        self.signals()

    def signals(self):
        self.ui.btn_cancelar.clicked.connect(self.cancelar)
        self.ui.btn_imagen.clicked.connect(self.cargar_imagen)
        self.ui.ingresar_pelicula.clicked.connect(self.crear_pelicula)
        self.ui.limpiar_pelicula.clicked.connect(self.limpiar_peli)
        self.ui.ingresar_actor.clicked.connect(self.crear_elenco)
        self.ui.limpiar_actor.clicked.connect(self.limpiar_actor)
    def obtener_datos(self):
        lista=list()
        self.nombre=""
        self.fecha=""
        self.pais=""
        self.descripcion=""
        self.director=""
        self.imagen=""
        self.nombre=self.ui.peli_nombre.text()
        self.pais=self.ui.peli_pais.text()
        self.descripcion=self.ui.peli_desc.text()
        self.director=self.ui.peli_director.text()
        self.fecha=self.ui.peli_fecha.text()

        
        lista.append(self.nombre)
        lista.append(self.pais)
        lista.append(self.descripcion)
        lista.append(self.director)
        lista.append(self.fecha)
        for x in lista: #si hay algun campo que esta vacio entregara error
            print(self.listo)
            if len(x)==0:
                self.listo=False
                return
    def obtener_datos_actor(self):
        
        self.nombre_actor=""
        self.personaje=""
        self.desc_actor=""
        
        self.nombre_actor=self.ui.actor_nombre.text()
        self.personaje=self.ui.actor_personaje.text()
        self.desc_actor=self.ui.actor_desc.text()


        if(len(self.personaje)==0 ):
            self.listo=False
            return
        if(len(self.nombre_actor)==0):
            self.listo=False
            return
            
    def crear_pelicula(self):
        self.obtener_datos()
        if(self.listo==True):#si los campos obligatorios tienen datos, se crea la pelicula
            print("Creando nueva pelicula ...")
                           #crear_director(nombre, pais, fecha_nacimiento,fecha_defuncion):
            model.crear_pelicula(self.nombre,self.pais,self.fecha,self.descripcion,self.director,
                                           "img/"+self.nombre.replace(" ","_")+".jpg")
            self.ui.label_imagen.pixmap().save("img/"+self.nombre.replace(" ","_")+".jpg","jpg")#guarda la imagen que se selecciono a la carpeta "img"
            self.listo_pelicula=True
            self.listo=True
        else:#si falta algun campo obligatorio, no se creara la nueva pelicula
            self.listo=True
            QtGui.QMessageBox.critical(self, 'Faltan campos obligatorios','Error:\nTodos los campos de pelicula son obligatorios')
    def crear_elenco(self):
        print(self.listo)
        print(self.listo_pelicula)
        self.obtener_datos_actor()
        if(self.listo==True and self.listo_pelicula==True):#si los campos obligatorios tienen datos, se crea la pelicula
            print("Ingresando elenco ...")
                    
            model.crear_elenco(self.personaje,self.desc_actor,self.nombre_actor,self.nombre)
            self.limpiar(actor)
        else:#si falta algun campo obligatorio, no se creara la nueva pelicula
            if(self.listo):
                self.listo=True
                QtGui.QMessageBox.critical(self, 'Faltan campos obligatorios','Error:\nEl campo personaje y nombre actor es obligatorio')
            else:
                QtGui.QMessageBox.critical(self, 'Falta crear la pelicula','Error:\nDebe crear primero la pelicula')
    def cargar_imagen(self):
        print("cargar imagen")      
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de director',None,
        "Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
        print (fileName[0])
        self.ui.label_imagen.setPixmap(QtGui.QPixmap(fileName[0]))    

    def cancelar(self):
        self.limpiar_peli()
        self.limpiar_actor()
        self.close()

    def limpiar_peli(self):#"limpia" el formulario
        self.ui.peli_nombre.setText("")
        self.ui.peli_pais.setText("")
        self.ui.peli_desc.setText("")
        self.ui.peli_director.setText("")
        self.ui.peli_fecha.setText("")
    def limpiar_actor(self):
        self.ui.actor_nombre.setText("")
        self.ui.actor_personaje.setText("")
        self.ui.actor_desc.setText("")
        



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Movies()
    sys.exit(app.exec_())
