# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulario.ui'
#
# Created: Tue Sep  1 04:39:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form_crear(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 640)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 121, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 111, 21))
        self.label_6.setObjectName("label_6")
        self.peli_pais = QtGui.QLineEdit(Form)
        self.peli_pais.setGeometry(QtCore.QRect(140, 130, 141, 27))
        self.peli_pais.setObjectName("peli_pais")
        self.peli_fecha = QtGui.QLineEdit(Form)
        self.peli_fecha.setGeometry(QtCore.QRect(140, 80, 141, 27))
        self.peli_fecha.setObjectName("peli_fecha")
        self.peli_nombre = QtGui.QLineEdit(Form)
        self.peli_nombre.setGeometry(QtCore.QRect(140, 30, 141, 27))
        self.peli_nombre.setObjectName("peli_nombre")
        self.peli_desc = QtGui.QLineEdit(Form)
        self.peli_desc.setGeometry(QtCore.QRect(140, 180, 141, 27))
        self.peli_desc.setObjectName("peli_desc")
        self.peli_director = QtGui.QLineEdit(Form)
        self.peli_director.setGeometry(QtCore.QRect(140, 230, 141, 27))
        self.peli_director.setObjectName("peli_director")
        self.ingresar_pelicula = QtGui.QPushButton(Form)
        self.ingresar_pelicula.setGeometry(QtCore.QRect(100, 330, 98, 27))
        self.ingresar_pelicula.setObjectName("ingresar_pelicula")
        self.btn_cancelar = QtGui.QPushButton(Form)
        self.btn_cancelar.setGeometry(QtCore.QRect(170, 610, 98, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.limpiar_pelicula = QtGui.QPushButton(Form)
        self.limpiar_pelicula.setGeometry(QtCore.QRect(220, 330, 98, 27))
        self.limpiar_pelicula.setObjectName("limpiar_pelicula")
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(180, 0, 111, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(170, 370, 81, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 410, 91, 21))
        self.label_9.setObjectName("label_9")
        self.actor_nombre = QtGui.QLineEdit(Form)
        self.actor_nombre.setGeometry(QtCore.QRect(140, 410, 141, 27))
        self.actor_nombre.setObjectName("actor_nombre")
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 460, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(20, 510, 111, 21))
        self.label_11.setObjectName("label_11")
        self.actor_personaje = QtGui.QLineEdit(Form)
        self.actor_personaje.setGeometry(QtCore.QRect(140, 460, 141, 27))
        self.actor_personaje.setObjectName("actor_personaje")
        self.actor_desc = QtGui.QLineEdit(Form)
        self.actor_desc.setGeometry(QtCore.QRect(140, 510, 141, 27))
        self.actor_desc.setObjectName("actor_desc")
        self.ingresar_actor = QtGui.QPushButton(Form)
        self.ingresar_actor.setGeometry(QtCore.QRect(100, 560, 98, 27))
        self.ingresar_actor.setObjectName("ingresar_actor")
        self.limpiar_actor = QtGui.QPushButton(Form)
        self.limpiar_actor.setGeometry(QtCore.QRect(230, 560, 98, 27))
        self.limpiar_actor.setObjectName("limpiar_actor")
        self.btn_imagen = QtGui.QPushButton(Form)
        self.btn_imagen.setGeometry(QtCore.QRect(140, 280, 141, 27))
        self.btn_imagen.setObjectName("btn_imagen")
        self.label_imagen = QtGui.QLabel(Form)
        self.label_imagen.setGeometry(QtCore.QRect(305, 246, 101, 81))
        self.label_imagen.setText("")
        self.label_imagen.setObjectName("label_imagen")
        self.label_imagen.setScaledContents(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Fecha Estreno", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "País", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Director", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.ingresar_pelicula.setText(QtGui.QApplication.translate("Form", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.limpiar_pelicula.setText(QtGui.QApplication.translate("Form", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Pelicula", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Actor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Personaje", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Descripcion Rol", None, QtGui.QApplication.UnicodeUTF8))
        self.ingresar_actor.setText(QtGui.QApplication.translate("Form", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.limpiar_actor.setText(QtGui.QApplication.translate("Form", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_imagen.setText(QtGui.QApplication.translate("Form", "Cargar Imagen", None, QtGui.QApplication.UnicodeUTF8))

