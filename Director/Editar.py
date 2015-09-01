#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Editar_director import Ui_formulario_editar
import Modelo_director

class Editar(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_formulario_editar()
        self.ui.setupUi(self)
        #self.show()
        self.signals()
        self.nombre=""
        self.imagen=""
        self.nacimiento=""
        self.defuncion=""
        self.pais=""
        self.id=0

    def signals(self):
        self.ui.boton_foto.clicked.connect(self.cargar_imagen)
        self.ui.difunto_check.clicked.connect(self.difunto_check_clicked)
        self.ui.guardar_boton.clicked.connect(self.guardar_director)
        self.ui.cancelar_boton.clicked.connect(self.cancelar)
        self.ui.limpiar_boton.clicked.connect(self.limpiar)
    
    def setID(self,id):
      self.id=id
      self.obtener_datos();

    def obtener_datos(self):
        self.nombre=""
        self.imagen=""
        self.nacimiento=""
        self.defuncion=""
        self.pais=""
        self.ui.id_label.setText("ID:xXxX")
        #self.datos
        if(self.id>=1):
	  self.datos=Modelo_director.buscar_id(self.id)
	  #print(self.datos)
	  self.ui.id_label.setText("ID:"+str(self.id))
	  self.ui.nombre_in.setText(self.datos[0])
	  self.ui.pais_in.setText(self.datos[1])
	  if(self.datos[0]!=""):
	    self.ui.difunto_check.setChecked(False)
	  else:
	    self.ui.difunto_check.setChecked(True)
	    y=int(self.datos[3][0:4])
	    m=int(self.datos[3][5:7])
	    d=int(self.datos[3][8:10])
	    self.ui.defuncion_in.setDate(QtCore.QDate(y,m,d))#Y,M,D
	  y=int(self.datos[2][0:4])
	  m=int(self.datos[2][5:7])
	  d=int(self.datos[2][8:10])
	  self.ui.nacimiento_in.setDate(QtCore.QDate(y,m,d))#Y,M,D
	  self.ui.foto_label.setPixmap(QtGui.QPixmap(self.datos[4]))
	  self.listo=True
	  


    def guardar_director(self):
	print("Guardando director modificado...")
        #self.obtener_datos()
        if(len(self.ui.nombre_in.text())>0 and Modelo_director.checkea_director(self.nombre)==False):#si los campos obligatorios tienen datos, se crea el director
	    defuncion=""
	    if(self.ui.difunto_check.isChecked()):#si el director esta muerto, se guardará la fecha de defuncion
	      defuncion=self.ui.defuncion_in.date().toPython().strftime("%Y-%m-%d")
	      
	    self.ui.foto_label.pixmap().save("img/"+self.nombre.replace(" ","_")+".jpg","jpg")#guarda la imagen que se selecciono a la carpeta "img"
            Modelo_director.actualiza(self.id,self.ui.nombre_in.text(),self.ui.pais_in.text(),self.ui.nacimiento_in.date().toPython().strftime("%Y-%m-%d"),defuncion,"img/"+self.nombre.replace(" ","_")+".jpg")
	    
            self.limpiar()
            self.close()
        else:#si falta algun campo obligatorio, no se creara el nuevo director
            if(len(self.nombre)>0):
                QtGui.QMessageBox.critical(self, "Director Existente","Error:\nEL director que intenta agregar ("+self.nombre+"), ya existe en la base de datos")
            else:
                QtGui.QMessageBox.critical(self, 'Faltan campos obligatorios','Error:\nLos campos "nombre" y "fecha de nacimiento" son obligatorios')


    def difunto_check_clicked(self):#si "difunto" esta chequeado activa el ingreso de fecha de defuncion, de lo contrario, la desactiva
        #print(self.ui.difunto_check.isChecked())
        self.ui.defuncion_in.setEnabled(self.ui.difunto_check.isChecked())

    def cargar_imagen(self):
        print("cargar imagen")
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione imagen de director',None,
        "Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
        print (fileName[0])
        self.ui.foto_label.setPixmap(QtGui.QPixmap(fileName[0]))

    def cancelar(self):
        self.close()
        self.limpiar()

    def limpiar(self):#"limpia" el formulario
        self.ui.nombre_in.setText("")
        self.ui.pais_in.setText("")
        self.ui.difunto_check.setChecked(False)
        self.ui.defuncion_in.setEnabled(False)
        self.ui.foto_label.setPixmap(QtGui.QPixmap("img/0.jpg"))
       

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Editar()
	main.show()
	main.obtener_datos(1)
	sys.exit(app.exec_())

