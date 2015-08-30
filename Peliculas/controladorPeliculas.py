#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Peliculas import Ui_Form
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
        self.ui.setupUi(self)
        self.load_movies()
        self.show()
        self.signals()
       

    def signals(self):
        self.ui.grilla.clicked.connect(self.show_poster) #table_movies es temporal
        self.ui.btn_eliminar.clicked.connect(self.delete)
        self.ui.btn_filtro.clicked.connect(self.load_filtered_movies)
        self.ui.btn_crear.clicked.connect(self.prueba)
    def prueba(self):
        asd=self.ui.filtro_actor.text()
        print(asd)
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

        # Colocamos la información en los labels
  #      self.ui.lbl_stars.setText(mov["stars"])
        self.ui.label_desc.setText(mov["descripcion"])  #recordar cambiar el label.setWordWrap True para reparto :D
        # Ahora la imagen
  #      img = QtGui.QPixmap(str(mov['poster']))  #str[mov[poster]] da el nombre del archivo para luego usarlo como una imagen
  #      self.ui.lbl_image.setPixmap(img)

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
        
        movies = model.filter_movie()
        
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

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Movies()
    sys.exit(app.exec_())
