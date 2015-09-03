# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crear_pelicula_ui.ui'
#
# Created: Thu Sep  3 09:33:55 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_formulario_crear(object):
    def setupUi(self, formulario_crear):
        formulario_crear.setObjectName("formulario_crear")
        formulario_crear.resize(500, 260)
        self.centralwidget = QtGui.QWidget(formulario_crear)
        self.centralwidget.setObjectName("centralwidget")
        self.nombre_in = QtGui.QLineEdit(self.centralwidget)
        self.nombre_in.setGeometry(QtCore.QRect(170, 25, 311, 25))
        self.nombre_in.setPlaceholderText("")
        self.nombre_in.setObjectName("nombre_in")
        self.fecha_in = QtGui.QDateEdit(self.centralwidget)
        self.fecha_in.setGeometry(QtCore.QRect(360, 55, 120, 25))
        self.fecha_in.setDate(QtCore.QDate(2015, 8, 31))
        self.fecha_in.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 0)))
        self.fecha_in.setMinimumDate(QtCore.QDate(1752, 9, 14))
        self.fecha_in.setCalendarPopup(True)
        self.fecha_in.setObjectName("fecha_in")
        self.foto_label = QtGui.QLabel(self.centralwidget)
        self.foto_label.setGeometry(QtCore.QRect(10, 20, 150, 200))
        self.foto_label.setAutoFillBackground(True)
        self.foto_label.setText("")
        self.foto_label.setPixmap(QtGui.QPixmap("img/0.jpg"))
        self.foto_label.setScaledContents(True)
        self.foto_label.setObjectName("foto_label")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 60, 141, 16))
        self.label.setObjectName("label")
        self.pais_in = QtGui.QLineEdit(self.centralwidget)
        self.pais_in.setGeometry(QtCore.QRect(280, 85, 200, 25))
        self.pais_in.setObjectName("pais_in")
        self.pais_label = QtGui.QLabel(self.centralwidget)
        self.pais_label.setGeometry(QtCore.QRect(180, 90, 141, 16))
        self.pais_label.setObjectName("pais_label")
        self.boton_foto = QtGui.QToolButton(self.centralwidget)
        self.boton_foto.setGeometry(QtCore.QRect(10, 230, 150, 23))
        self.boton_foto.setObjectName("boton_foto")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 5, 141, 16))
        self.label_2.setObjectName("label_2")
        self.crear_boton = QtGui.QPushButton(self.centralwidget)
        self.crear_boton.setGeometry(QtCore.QRect(220, 230, 85, 27))
        self.crear_boton.setObjectName("crear_boton")
        self.limpiar_boton = QtGui.QPushButton(self.centralwidget)
        self.limpiar_boton.setGeometry(QtCore.QRect(310, 230, 85, 27))
        self.limpiar_boton.setObjectName("limpiar_boton")
        self.cancelar_boton = QtGui.QPushButton(self.centralwidget)
        self.cancelar_boton.setGeometry(QtCore.QRect(400, 230, 85, 27))
        self.cancelar_boton.setObjectName("cancelar_boton")
        self.descripcion_in = QtGui.QTextEdit(self.centralwidget)
        self.descripcion_in.setGeometry(QtCore.QRect(170, 150, 311, 71))
        self.descripcion_in.setObjectName("descripcion_in")
        self.descripcion_label = QtGui.QLabel(self.centralwidget)
        self.descripcion_label.setGeometry(QtCore.QRect(170, 130, 141, 16))
        self.descripcion_label.setObjectName("descripcion_label")
        formulario_crear.setCentralWidget(self.centralwidget)

        self.retranslateUi(formulario_crear)
        QtCore.QMetaObject.connectSlotsByName(formulario_crear)

    def retranslateUi(self, formulario_crear):
        formulario_crear.setWindowTitle(QtGui.QApplication.translate("formulario_crear", "Crear Pelicula", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("formulario_crear", "Año Estreno", None, QtGui.QApplication.UnicodeUTF8))
        self.pais_label.setText(QtGui.QApplication.translate("formulario_crear", "País", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_foto.setText(QtGui.QApplication.translate("formulario_crear", "Cargar poster ...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("formulario_crear", "Nombre pelicula", None, QtGui.QApplication.UnicodeUTF8))
        self.crear_boton.setText(QtGui.QApplication.translate("formulario_crear", "Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.limpiar_boton.setText(QtGui.QApplication.translate("formulario_crear", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar_boton.setText(QtGui.QApplication.translate("formulario_crear", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcion_label.setText(QtGui.QApplication.translate("formulario_crear", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))

