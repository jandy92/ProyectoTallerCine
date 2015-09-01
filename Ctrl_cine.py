#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Ui_ProyectoTallerCine import Ui_Form
from Actores.Ctrl_actores import Actores
from Director.Controlador_director import Director
from Peliculas.controladorPeliculas import Movies


class cine(QtGui.QMainWindow):
	
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
	self.ui = Ui_Form()
	self.ui.setupUi(self)
	self.d=Director()
	self.a=Actores()
	self.p=Movies()
	self.show()
	self.signals()

    def signals(self):
	self.ui.Actores.clicked.connect(self.trae_actores)
	self.ui.Director.clicked.connect(self.trae_director)
	self.ui.Peliculas.clicked.connect(self.trae_peliculas)

    def trae_actores(self):
	self.a.show();
    def trae_director(self):
	self.d.show();
    def trae_peliculas(self):
	self.p.show();	



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = cine()
    sys.exit(app.exec_())
