# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Actores.ui'
#
# Created: Sun Aug 30 02:07:47 2015
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
        self.img_actor.setScaledContents(True)
        self.img_actor.setObjectName("img_actor")
        self.tabla_actor = QtGui.QTableView(Form)
        self.tabla_actor.setGeometry(QtCore.QRect(10, 60, 451, 421))
        self.tabla_actor.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_actor.setObjectName("tabla_actor")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_actor.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.agre_actor.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.elim_actor.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.img_actor.setText(QtGui.QApplication.translate("Form", "img_actor", None, QtGui.QApplication.UnicodeUTF8))

