#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Editar_pelicula import Ui_formulario_editar
import Modelo_pelicula

class Editar(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_formulario_editar()
        self.ui.setupUi(self)
        #self.show()
        self.nombre=""
        self.imagen=""
        self.estreno=""
        self.pais=""
        self.descripcion=""
        self.director_id=""
        self.id=0
        self.signals()

    def signals(self):
        """
        Conecta la base de datos con el codigo
        """
        self.ui.editar_boton.clicked.connect(self.guardar_pelicula)
        self.ui.boton_foto.clicked.connect(self.cargar_imagen)
        self.ui.cancelar_boton.clicked.connect(self.cancelar)
        self.ui.limpiar_boton.clicked.connect(self.limpiar)

    def setID(self,id):
      """
      Establece la id a editar
      """
      self.id=id
      self.obtener_datos();

    def obtener_datos(self):
        """
        Obtiene los datos de la pelicula
        y los muestra en pantalla de editar
        """
        self.nombre=""
        self.imagen=""
        self.estreno=""
        self.pais=""
        self.descripcion=""
        self.ui.id_label.setText("ID:xXxX")
        #self.datos
        if(self.id>=1):
	  self.datos=Modelo_pelicula.buscar_id(self.id)
	  print(self.datos)
	  print(len(self.datos))
	  self.ui.id_label.setText("ID:"+str(self.id))
	  self.ui.nombre_in.setText(self.datos[1])
	  y=int(self.datos[2][0:4])
	  m=int(self.datos[2][5:7])
	  d=int(self.datos[2][8:10])
	  self.ui.fecha_in.setDate(QtCore.QDate(y,m,d))#Y,M,D
	  self.ui.pais_in.setText(self.datos[3])
	 # print("---------->"+str(self.datos[4]))
          self.ui.descripcion_in.setText(self.datos[4])
	  self.ui.foto_label.setPixmap(QtGui.QPixmap(self.datos[6]))
	  self.listo=True
	  
    def guardar_pelicula(self):
        """
        Guarda la pelocula que fue editada en la base de datos
        """
	print("Guardando pelicula modificado...")
        #self.obtener_datos()
        if(len(self.ui.nombre_in.text())>0 and len(self.ui.fecha_in.text())>0 and len(self.ui.pais_in.text())>0 and  len(self.ui.descripcion_in.toPlainText())>0):#si los campos obligatorios tienen datos, se crea la pelicula
	         
	    self.ui.foto_label.pixmap().save("Peliculas/img/"+self.nombre.replace(" ","_")+".jpg","jpg")#guarda la imagen que se selecciono a la carpeta "img"
            Modelo_pelicula.actualiza(self.id,self.ui.nombre_in.text(),self.ui.fecha_in.date().toPython().strftime("%Y-%m-%d"),self.ui.pais_in.text(),self.ui.descripcion_in.toPlainText(),"Peliculas/img/"+self.nombre.replace(" ","_")+".jpg")
	    
            self.limpiar()
            self.close()
        else:#si falta algun campo obligatorio, no se creara el nuevo director
            if(len(self.nombre)>0 and len(self.descripcion)>0 and len(self.pais)>0 and len(self.estreno)>0):
                QtGui.QMessageBox.critical(self, "Pelicula Existente","Error:\nLa pelicula que intenta agregar ("+self.nombre+"), ya existe en la base de datos")
            else:
                QtGui.QMessageBox.critical(self, 'Faltan campos obligatos campos "nombre", "estreno","pais", "descripcion" son obligatorios')
  
    def cargar_imagen(self):
        """
        Carga imagen de la pelicula
        """
        print("cargar imagen")
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Seleccione una imagen de pelicula',None,
        "Archivo de imagen (*.png *.jpg)")#se abre un dialogo con un "filtro" en que solo se muestran imagenes
        print (fileName[0])
        self.ui.foto_label.setPixmap(QtGui.QPixmap(fileName[0]))

    def cancelar(self):
        """
        Limpia y cierra la ventana
        """
        self.close()
        self.limpiar()

    def limpiar(self):
        """
        "limpia" el formulario
        """
        self.ui.nombre_in.setText("")
        self.ui.pais_in.setText("")
        self.ui.descripcion_in.setText("")
        self.ui.foto_label.setPixmap(QtGui.QPixmap("Peliculas/img/0.jpg"))
      
             
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Editar()
	main.show()
	main.obtener_datos(1)
	sys.exit(app.exec_())

