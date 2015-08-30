#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Directores_ui import Ui_Form
import Modelo_director

class Director(QtGui.QMainWindow):
    columnas_tabla = (
        (u"Nombre", 200),
        (u"Pais", 75),
        (u"Fecha_nacimiento", 120),
        (u"Fecha_defuncion", 75))

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
       #self.signals()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Director()
    sys.exit(app.exec_())