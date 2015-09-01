#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
"""
El formulario, dado una ID, se autocompleta con los datos correspondiente al director de dicha ID
dando la posibilidad de modificar estos datos y los reemplaza en la base de datos
"""
def conectar():
    con = sqlite3.connect('../ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def buscar_id(num):#retorna una lista con todos los valores de la fila buscada (5 en total)
	# recibe id y devuelve arreglo con todos los datos
	con = conectar()
	c = con.cursor()
    	con.row_factory = sqlite3.Row
    	querry = "SELECT * FROM director WHERE id = ?"
	resultado = c.execute(querry,[num])
	lista = resultado.fetchall()
	con.close();
    	l=[None,None,None,None,None]
	#print(len(l))
    	for i in range (0,5):#se rellena el arreglo vacío
        	l[i]=lista[0][i+1]
	return l



def obtener_directores():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM director"
    resultado= c.execute(query)
    directores = resultado.fetchall()
    con.close()
    return directores

def borrar(id):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM director WHERE id = ?"
    try:
        resultado = c.execute(query, [id])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def crear_director(nombre, pais, fecha_nacimiento,fecha_defuncion,imagen):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO director (nombre, pais, fecha_nacimiento,fecha_defuncion,imagen)"
        "VALUES (?, ?, ?, ?,?)")
    c.execute(sql, (nombre, pais, fecha_nacimiento,fecha_defuncion,imagen))
    con.commit()

def checkea_director(nombre):#devuelve true si encuentra algun director del nombre recibido como parametro, false si no.
    existe=True
    con=conectar()
    c=con.cursor()
    query="SELECT * FROM director WHERE nombre= ?"
    resultado=c.execute(query,[nombre])
    lista=resultado.fetchall()
    con.close()
    if(len(lista)==0):
        existe=False
    return existe
  
def actualiza(id,nombre, pais, fecha_nacimiento,fecha_defuncion,imagen):
   con=conectar()
   c=con.cursor()
   sql=('UPDATE director SET nombre="'+nombre+'", pais="'+pais+'", fecha_nacimiento="'+fecha_nacimiento+'",fecha_defuncion="'+fecha_defuncion+'",imagen="'+imagen+'"\
     WHERE id ="'+str(id)+'"')
   c.execute(sql)
   con.commit()
   

#if __name__ == "__main__":
    #print("Recibe dato")
   # recibe_dato(5,"ale", "chile", "1992-11-26","","")