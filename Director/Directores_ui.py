# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Directores.ui'
#
# Created: Fri Sep  4 00:17:13 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(774, 600)
        self.editarDirector = QtGui.QPushButton(Form)
        self.editarDirector.setGeometry(QtCore.QRect(520, 500, 98, 27))
        self.editarDirector.setObjectName("editarDirector")
        self.agregarDirector = QtGui.QPushButton(Form)
        self.agregarDirector.setGeometry(QtCore.QRect(140, 500, 98, 27))
        self.agregarDirector.setObjectName("agregarDirector")
        self.eliminarDirector = QtGui.QPushButton(Form)
        self.eliminarDirector.setGeometry(QtCore.QRect(330, 500, 98, 27))
        self.eliminarDirector.setObjectName("eliminarDirector")
        self.silla_imagen = QtGui.QLabel(Form)
        self.silla_imagen.setGeometry(QtCore.QRect(660, 470, 121, 141))
        self.silla_imagen.setText("")
        self.silla_imagen.setPixmap(QtGui.QPixmap("Silla.png"))
        self.silla_imagen.setScaledContents(True)
        self.silla_imagen.setObjectName("silla_imagen")
        self.grilla = QtGui.QTableView(Form)
        self.grilla.setGeometry(QtCore.QRect(30, 190, 711, 281))
        self.grilla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.grilla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla.setObjectName("grilla")
        self.imagen = QtGui.QLabel(Form)
        self.imagen.setGeometry(QtCore.QRect(40, 10, 131, 171))
        self.imagen.setStyleSheet("")
        self.imagen.setText("")
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.label_numero_peli = QtGui.QLabel(Form)
        self.label_numero_peli.setGeometry(QtCore.QRect(240, 60, 151, 21))
        self.label_numero_peli.setObjectName("label_numero_peli")
        self.cantidad_peliculas_dirigidas = QtGui.QLabel(Form)
        self.cantidad_peliculas_dirigidas.setGeometry(QtCore.QRect(410, 50, 81, 41))
        self.cantidad_peliculas_dirigidas.setText("")
        self.cantidad_peliculas_dirigidas.setObjectName("cantidad_peliculas_dirigidas")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Directores", None, QtGui.QApplication.UnicodeUTF8))
        self.editarDirector.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.agregarDirector.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminarDirector.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_numero_peli.setText(QtGui.QApplication.translate("Form", "Nº peliculas dirgidas", None, QtGui.QApplication.UnicodeUTF8))

