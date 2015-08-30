#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Directores_ui import Ui_Form
import Modelo_director

class Director(QtGui.QMainWindow):
    table_columns = (
        (u"Nombre", 0),
        (u"Pais", 150),
        (u"Fecha nacimiento", 150),
        (u"Fecha defunción", 150))

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.cargar_directores();
        self.show()
       #self.signals()
        
    def cargar_directores(self):
        directores=Modelo_director.obtener_directores()
        filas=len(directores)
        data = QtGui.QStandardItemModel(filas, len(self.table_columns))
        self.ui.grilla.setModel(data)
        self.ui.grilla.horizontalHeader().setResizeMode(0, self.ui.grilla.horizontalHeader().Stretch)

        for col, h in enumerate(self.table_columns):
            data.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.grilla.setColumnWidth(col, h[1])
            """
        for i, director in enumerate(Director):
            filas = [director["nombre"], director["pais"], director["fecha_nacimiento"],director["fecha_defuncion"]]
            for j, field in enumerate(filas):
                index = data.index(i, j, QtCore.QModelIndex())
                data.setData(index, field)
            # Parametros ocultos
            data.item(i).director = director
            """


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Director()
    sys.exit(app.exec_())