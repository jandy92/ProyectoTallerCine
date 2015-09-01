#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Directores_ui import Ui_Form
from Crear_director import Ui_formulario_crear
from Editar_director import  Ui_formulario_editar
import Modelo_director
import Editar

class Director(QtGui.QMainWindow):
    table_columns = (
	(u"Nombre", 0),
	(u"Pais", 150),
	(u"Fecha nacimiento", 150),
	(u"Fecha defunción", 150))

    def __init__(self, parent=None):
	QtGui.QMainWindow.__init__(self, parent)
	self.ui = Ui_Form()
	self.ui.setupUi(self)
	self.cargar_directores();
	self.show()
	self.dialogo=Controlador_form_crear_director()
	self.editar=Editar.Editar()
	self.signals()
	       
    
    def signals(self):
	self.ui.grilla.clicked.connect(self.mostrar_imagen)
	self.ui.eliminarDirector.clicked.connect(self.elimina)
	self.ui.agregarDirector.clicked.connect(self.mostrar_ventana_agregar)
	self.dialogo.ui.crear_boton.clicked.connect(self.cargar_directores)
	self.ui.editarDirector.clicked.connect(self.editar_director)

    def cargar_directores(self):
	directores=Modelo_director.obtener_directores()
	filas=len(directores)
	data = QtGui.QStandardItemModel(filas, len(self.table_columns))
	self.ui.grilla.setModel(data)
	self.ui.grilla.horizontalHeader().setResizeMode(0, self.ui.grilla.horizontalHeader().Stretch)

	for col, h in enumerate(self.table_columns):
	    data.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
	    self.ui.grilla.setColumnWidth(col, h[1])
	    
	for i, dire in enumerate(directores):
	    filas = [
	        dire["nombre"], dire["pais"],
	        dire["fecha_nacimiento"],dire["fecha_defuncion"]]
	    for j, field in enumerate(filas):
	        index = data.index(i, j, QtCore.QModelIndex())
	        data.setData(index, field)
	    # Parametros ocultos
	    data.item(i).dire = dire

    def mostrar_imagen(self, index):
	index = index if index is not None\
	    else self.ui.grilla.currentIndex()
	if index.row() == -1:
	    QtGui.QMessageBox.information(
		None,
		u"Información",
		u"Por favor seleccione una orden de trabajo.")
	    return
	data = self.ui.grilla.model()
	dire = data.item(index.row(),0).dire
	img = QtGui.QPixmap(str(dire['imagen']))
	#print(str(dire['imagen'])[1:])
	self.ui.imagen.setPixmap(img)

    def elimina(self):
	index =self.ui.grilla.currentIndex()
	data = self.ui.grilla.model()
	dire = data.item(index.row(),0).dire
	iD = str(dire['id'])
	Modelo_director.borrar(iD);
	self.cargar_directores();
	#print(str(dire['imagen'])[1:])
	#self.ui.imagen.setPixmap(img)



    def mostrar_ventana_agregar(self):
       self.dialogo.show()
    
    def editar_director(self):
	self.editar.show()
	pass


class Controlador_form_crear_director(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui=Ui_formulario_crear()
        self.ui.setupUi(self)
        #self.show()
        self.listo=False;#True: los datos obligatorios existen, False:si no
        self.nombre=""
        self.imagen=""
        self.nacimiento=""
        self.defuncion=""
        self.pais=""
        self.signals()

    def signals(self):
        self.ui.boton_foto.clicked.connect(self.cargar_imagen)
        self.ui.difunto_check.clicked.connect(self.difunto_check_clicked)
        self.ui.crear_boton.clicked.connect(self.crear_director)
        self.ui.cancelar_boton.clicked.connect(self.cancelar)
        self.ui.limpiar_boton.clicked.connect(self.limpiar)

    def difunto_check_clicked(self):#si "difunto" esta chequeado activa el ingreso de fecha de defuncion, de lo contrario, la desactiva
        #print(self.ui.difunto_check.isChecked())
        self.ui.defuncion_in.setEnabled(self.ui.difunto_check.isChecked())

    def obtener_datos(self):
        self.nombre=""
        self.imagen=""
        self.nacimiento=""
        self.defuncion=""
        self.pais=""
        self.nombre=self.ui.nombre_in.text()#obligatorio
        self.pais=self.ui.pais_in.text()#obligatorio
        self.nacimiento=self.ui.nacimiento_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
        if(self.ui.difunto_check.isChecked()):
            self.defuncion=self.ui.defuncion_in.date().toPython().strftime("%Y-%m-%d")#transformar de fecha en QT a fecha en python a string
        self.listo=False
        #print(len(self.nacimiento))
        if(len(self.nombre)!=0 and len(self.nacimiento)!=0):#True: si los campos obligatorios estan definidos, False: si no
            self.listo=True

    def crear_director(self):
        self.obtener_datos()
        if(self.listo==True and Modelo_director.checkea_director(self.nombre)==False):#si los campos obligatorios tienen datos, se crea el director
            print("Creando nuevo director ...")
                           #crear_director(nombre, pais, fecha_nacimiento,fecha_defuncion):
            Modelo_director.crear_director(self.nombre,self.pais,self.nacimiento,self.defuncion,"img/"+self.nombre.replace(" ","_")+".jpg")
            self.ui.foto_label.pixmap().save("img/"+self.nombre.replace(" ","_")+".jpg","jpg")#guarda la imagen que se selecciono a la carpeta "img"
            self.limpiar()
            self.close()
        else:#si falta algun campo obligatorio, no se creara el nuevo director
            if(len(self.nombre)>0):
                QtGui.QMessageBox.critical(self, "Director Existente","Error:\nEL director que intenta agregar ("+self.nombre+"), ya existe en la base de datos")
            else:
                QtGui.QMessageBox.critical(self, 'Faltan campos obligatorios','Error:\nLos campos "nombre" y "fecha de nacimiento" son obligatorios')

    def cargar_imagen(self):
        print("cargar imagen")
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de director',None,
        "Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
        print (fileName[0])
        self.ui.foto_label.setPixmap(QtGui.QPixmap(fileName[0]))

    def cancelar(self):
	self.limpiar()
        self.close()

    def limpiar(self):#"limpia" el formulario
        self.ui.nombre_in.setText("")
        self.ui.pais_in.setText("")
        self.ui.difunto_check.setChecked(False)
        self.ui.defuncion_in.setEnabled(False)
        self.ui.foto_label.setPixmap(QtGui.QPixmap("img/0.jpg"))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Director()
    sys.exit(app.exec_())

