# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Actores.ui'
#
# Created: Fri Sep  4 13:20:11 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(631, 499)
        self.edit_actor = QtGui.QPushButton(Form)
        self.edit_actor.setGeometry(QtCore.QRect(20, 20, 98, 27))
        self.edit_actor.setObjectName("edit_actor")
        self.agre_actor = QtGui.QPushButton(Form)
        self.agre_actor.setGeometry(QtCore.QRect(140, 20, 98, 27))
        self.agre_actor.setObjectName("agre_actor")
        self.elim_actor = QtGui.QPushButton(Form)
        self.elim_actor.setGeometry(QtCore.QRect(260, 20, 98, 27))
        self.elim_actor.setObjectName("elim_actor")
        self.img_actor = QtGui.QLabel(Form)
        self.img_actor.setGeometry(QtCore.QRect(480, 150, 131, 211))
        self.img_actor.setText("")
        self.img_actor.setScaledContents(True)
        self.img_actor.setObjectName("img_actor")
        self.tabla_actor = QtGui.QTableView(Form)
        self.tabla_actor.setGeometry(QtCore.QRect(10, 110, 451, 371))
        self.tabla_actor.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_actor.setObjectName("tabla_actor")
        self.filtro_box = QtGui.QComboBox(Form)
        self.filtro_box.setEnabled(True)
        self.filtro_box.setGeometry(QtCore.QRect(20, 60, 441, 27))
        self.filtro_box.setMinimumSize(QtCore.QSize(441, 27))
        self.filtro_box.setEditable(True)
        self.filtro_box.setObjectName("filtro_box")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(470, 400, 91, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(510, 430, 81, 17))
        self.label_2.setObjectName("label_2")
        self.numero_actuaciones = QtGui.QLabel(Form)
        self.numero_actuaciones.setGeometry(QtCore.QRect(570, 400, 41, 20))
        self.numero_actuaciones.setText("")
        self.numero_actuaciones.setObjectName("numero_actuaciones")
        self.boton_filtrar = QtGui.QPushButton(Form)
        self.boton_filtrar.setGeometry(QtCore.QRect(500, 60, 99, 27))
        self.boton_filtrar.setObjectName("boton_filtrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Actores", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_actor.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.agre_actor.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.elim_actor.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Participo en ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "peliculas.", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_filtrar.setText(QtGui.QApplication.translate("Form", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))

