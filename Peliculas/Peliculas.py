# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Peliculas.ui'
#
# Created: Sat Aug 29 23:23:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 444)
        self.btn_eliminar = QtGui.QPushButton(Form)
        self.btn_eliminar.setGeometry(QtCore.QRect(10, 20, 98, 27))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_editar = QtGui.QPushButton(Form)
        self.btn_editar.setGeometry(QtCore.QRect(250, 20, 98, 27))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_crear = QtGui.QPushButton(Form)
        self.btn_crear.setGeometry(QtCore.QRect(130, 20, 98, 27))
        self.btn_crear.setObjectName("btn_crear")
        self.btn_filtro = QtGui.QPushButton(Form)
        self.btn_filtro.setGeometry(QtCore.QRect(10, 100, 98, 27))
        self.btn_filtro.setObjectName("btn_filtro")
        self.filtro_actor = QtGui.QLineEdit(Form)
        self.filtro_actor.setGeometry(QtCore.QRect(130, 100, 201, 27))
        self.filtro_actor.setObjectName("filtro_actor")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(380, 300, 141, 17))
        self.label.setObjectName("label")
        self.label_desc = QtGui.QLabel(Form)
        self.label_desc.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_desc.setGeometry(QtCore.QRect(380, 330, 141, 91))
        self.label_desc.setObjectName("label_desc")
        self.label_desc.setWordWrap(True)
        self.label_reparto = QtGui.QLabel(Form)
        self.label_reparto.setGeometry(QtCore.QRect(380, 206, 141, 81))
        self.label_reparto.setObjectName("label_reparto")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 170, 131, 17))
        self.label_4.setObjectName("label_4")
        self.label_imagen = QtGui.QLabel(Form)
        self.label_imagen.setGeometry(QtCore.QRect(380, 30, 141, 121))
        self.label_imagen.setObjectName("label_imagen")
        self.label_imagen.setScaledContents(True)
        self.grilla = QtGui.QTableView(Form)
        self.grilla.setGeometry(QtCore.QRect(10, 150, 341, 281))
        self.grilla.setObjectName("grilla")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_crear.setText(QtGui.QApplication.translate("Form", "Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_filtro.setText(QtGui.QApplication.translate("Form", "Filtro", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_desc.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_reparto.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Reparto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_imagen.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

