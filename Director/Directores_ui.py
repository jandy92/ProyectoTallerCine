# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Directores.ui'
#
# Created: Sat Aug 29 21:57:05 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 80, 631, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grillaDirectores = QtGui.QGridLayout(self.gridLayoutWidget)
        self.grillaDirectores.setContentsMargins(0, -1, -1, -1)
        self.grillaDirectores.setObjectName("grillaDirectores")
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
        self.silla_imagen.setGeometry(QtCore.QRect(670, 450, 121, 141))
        self.silla_imagen.setText("")
        self.silla_imagen.setPixmap(QtGui.QPixmap("Silla.png"))
        self.silla_imagen.setScaledContents(True)
        self.silla_imagen.setObjectName("silla_imagen")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Directores", None, QtGui.QApplication.UnicodeUTF8))
        self.editarDirector.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.agregarDirector.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminarDirector.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

