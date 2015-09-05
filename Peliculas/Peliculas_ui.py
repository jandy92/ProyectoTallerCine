# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Peliculas.ui'
#
# Created: Sat Sep  5 04:31:10 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Ventana_peliculas(object):
    def setupUi(self, Ventana_peliculas):
        Ventana_peliculas.setObjectName("Ventana_peliculas")
        Ventana_peliculas.resize(640, 480)
        self.boton_eliminar_pelicula = QtGui.QPushButton(Ventana_peliculas)
        self.boton_eliminar_pelicula.setGeometry(QtCore.QRect(60, 440, 98, 27))
        self.boton_eliminar_pelicula.setObjectName("boton_eliminar_pelicula")
        self.boton_editar_pelicula_ = QtGui.QPushButton(Ventana_peliculas)
        self.boton_editar_pelicula_.setGeometry(QtCore.QRect(300, 440, 98, 27))
        self.boton_editar_pelicula_.setObjectName("boton_editar_pelicula_")
        self.boton_crear_pelicula = QtGui.QPushButton(Ventana_peliculas)
        self.boton_crear_pelicula.setGeometry(QtCore.QRect(180, 440, 98, 27))
        self.boton_crear_pelicula.setObjectName("boton_crear_pelicula")
        self.boton_filtro_actor = QtGui.QPushButton(Ventana_peliculas)
        self.boton_filtro_actor.setGeometry(QtCore.QRect(10, 30, 98, 27))
        self.boton_filtro_actor.setObjectName("boton_filtro_actor")
        self.filtro_actor = QtGui.QLineEdit(Ventana_peliculas)
        self.filtro_actor.setGeometry(QtCore.QRect(130, 30, 331, 27))
        self.filtro_actor.setObjectName("filtro_actor")
        self.descripcion = QtGui.QLabel(Ventana_peliculas)
        self.descripcion.setGeometry(QtCore.QRect(470, 270, 141, 17))
        self.descripcion.setObjectName("descripcion")
        self.label_descripcion = QtGui.QLabel(Ventana_peliculas)
        self.label_descripcion.setGeometry(QtCore.QRect(470, 290, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_descripcion.setFont(font)
        self.label_descripcion.setText("")
        self.label_descripcion.setScaledContents(False)
        self.label_descripcion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descripcion.setWordWrap(True)
        self.label_descripcion.setObjectName("label_descripcion")
        self.label_reparto = QtGui.QLabel(Ventana_peliculas)
        self.label_reparto.setGeometry(QtCore.QRect(470, 230, 41, 41))
        self.label_reparto.setText("")
        self.label_reparto.setObjectName("label_reparto")
        self.reparto = QtGui.QLabel(Ventana_peliculas)
        self.reparto.setGeometry(QtCore.QRect(470, 210, 131, 17))
        self.reparto.setObjectName("reparto")
        self.label_imagen = QtGui.QLabel(Ventana_peliculas)
        self.label_imagen.setGeometry(QtCore.QRect(480, 20, 141, 181))
        self.label_imagen.setText("")
        self.label_imagen.setScaledContents(True)
        self.label_imagen.setObjectName("label_imagen")
        self.grilla = QtGui.QTableView(Ventana_peliculas)
        self.grilla.setGeometry(QtCore.QRect(10, 80, 451, 341))
        self.grilla.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.EditKeyPressed)
        self.grilla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla.setObjectName("grilla")

        self.retranslateUi(Ventana_peliculas)
        QtCore.QMetaObject.connectSlotsByName(Ventana_peliculas)

    def retranslateUi(self, Ventana_peliculas):
        Ventana_peliculas.setWindowTitle(QtGui.QApplication.translate("Ventana_peliculas", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_eliminar_pelicula.setText(QtGui.QApplication.translate("Ventana_peliculas", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_editar_pelicula_.setText(QtGui.QApplication.translate("Ventana_peliculas", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_crear_pelicula.setText(QtGui.QApplication.translate("Ventana_peliculas", "Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_filtro_actor.setText(QtGui.QApplication.translate("Ventana_peliculas", "Filtro", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcion.setText(QtGui.QApplication.translate("Ventana_peliculas", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.reparto.setText(QtGui.QApplication.translate("Ventana_peliculas", "Reparto", None, QtGui.QApplication.UnicodeUTF8))

