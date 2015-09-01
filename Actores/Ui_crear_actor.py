# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crear_actor.ui'
#
# Created: Tue Sep  1 01:20:24 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_crear_actor(object):
    def setupUi(self, crear_actor):
        crear_actor.setObjectName("crear_actor")
        crear_actor.resize(500, 301)
        self.centralWidget = QtGui.QWidget(crear_actor)
        self.centralWidget.setObjectName("centralWidget")
        self.imagen_label = QtGui.QLabel(self.centralWidget)
        self.imagen_label.setGeometry(QtCore.QRect(10, 20, 151, 201))
        self.imagen_label.setText("")
        self.imagen_label.setPixmap(QtGui.QPixmap("img/0.jpg"))
        self.imagen_label.setScaledContents(True)
        self.imagen_label.setWordWrap(False)
        self.imagen_label.setObjectName("imagen_label")
        self.nombre_in = QtGui.QLineEdit(self.centralWidget)
        self.nombre_in.setGeometry(QtCore.QRect(172, 70, 311, 27))
        self.nombre_in.setObjectName("nombre_in")
        self.boton_imagen = QtGui.QPushButton(self.centralWidget)
        self.boton_imagen.setGeometry(QtCore.QRect(10, 250, 161, 27))
        self.boton_imagen.setObjectName("boton_imagen")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 201, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 151, 17))
        self.label_3.setObjectName("label_3")
        self.nacimiento_in = QtGui.QDateEdit(self.centralWidget)
        self.nacimiento_in.setGeometry(QtCore.QRect(330, 120, 110, 21))
        self.nacimiento_in.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 8, 31), QtCore.QTime(7, 0, 0)))
        self.nacimiento_in.setMaximumDate(QtCore.QDate(7915, 8, 31))
        self.nacimiento_in.setMinimumDate(QtCore.QDate(1753, 9, 14))
        self.nacimiento_in.setObjectName("nacimiento_in")
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(170, 160, 67, 17))
        self.label_4.setObjectName("label_4")
        self.boton_crear = QtGui.QPushButton(self.centralWidget)
        self.boton_crear.setGeometry(QtCore.QRect(190, 230, 81, 27))
        self.boton_crear.setObjectName("boton_crear")
        self.boton_limpiar = QtGui.QPushButton(self.centralWidget)
        self.boton_limpiar.setGeometry(QtCore.QRect(300, 230, 81, 27))
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.boton_cancelar = QtGui.QPushButton(self.centralWidget)
        self.boton_cancelar.setGeometry(QtCore.QRect(400, 230, 81, 27))
        self.boton_cancelar.setObjectName("boton_cancelar")
        self.genero = QtGui.QComboBox(self.centralWidget)
        self.genero.setGeometry(QtCore.QRect(250, 160, 211, 27))
        self.genero.setObjectName("genero")
        self.genero.addItem("")
        self.genero.addItem("")
        crear_actor.setCentralWidget(self.centralWidget)

        self.retranslateUi(crear_actor)
        QtCore.QMetaObject.connectSlotsByName(crear_actor)

    def retranslateUi(self, crear_actor):
        crear_actor.setWindowTitle(QtGui.QApplication.translate("crear_actor", "crear_actor", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_imagen.setText(QtGui.QApplication.translate("crear_actor", "Agregar imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("crear_actor", "Nombre del actor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("crear_actor", "Fecha de nacimiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("crear_actor", "Genero:", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_crear.setText(QtGui.QApplication.translate("crear_actor", "Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_limpiar.setText(QtGui.QApplication.translate("crear_actor", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_cancelar.setText(QtGui.QApplication.translate("crear_actor", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.genero.setItemText(0, QtGui.QApplication.translate("crear_actor", "Hombre", None, QtGui.QApplication.UnicodeUTF8))
        self.genero.setItemText(1, QtGui.QApplication.translate("crear_actor", "Mujer", None, QtGui.QApplication.UnicodeUTF8))

