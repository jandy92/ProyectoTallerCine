#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Ui_actores import Ui_Form
import Modelo_actor


class Actores(QtGui.QMainWindow):

    tabla_columnas = (
        (u"Nombre", 200),
        (u"Birtday", 150),
        (u"Genero", 150))

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.carga_actores()
        self.show()
        self.signals()

    def signals(self):
        self.ui.tabla_actor.clicked.connect(self.show_poster)

    def show_poster(self, index):
        index = index if index is not None\
            else self.ui.tabla_actor.currentIndex()
        if index.row() == -1:
            QtGui.QMessageBox.information(
                None,
                u"Información",
                u"Por favor seleccione una orden de trabajo.")
            return
        data = self.ui.tabla_actor.model()
        mov = data.item(index.row(), 0).mov

       
        # Ahora la imagen
        img = QtGui.QPixmap(str(mov['imagen']))
        print str(mov['imagen'])
        self.ui.img_actor.setPixmap(img)

    def carga_actores(self):
        actores = Modelo_actor.obtener_actor()
        rows = len(actores)
        data = QtGui.QStandardItemModel(
        	rows, len(self.tabla_columnas))
        self.ui.tabla_actor.setModel(data)
        self.ui.tabla_actor.horizontalHeader().setResizeMode(
            0, self.ui.tabla_actor.horizontalHeader().Stretch)

        for col, h in enumerate(self.tabla_columnas):
            data.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.tabla_actor.setColumnWidth(col, h[1])

        for i, mov in enumerate(actores):
            row = [
                mov["nombre"], mov["birthday"], mov["genero"],
                mov["imagen"]]
            for j, field in enumerate(row):
                index = data.index(i, j, QtCore.QModelIndex())
                data.setData(index, field)
            # Parametros ocultos
            data.item(i).mov = mov


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Actores()
    sys.exit(app.exec_())