#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import os.path
"""
El formulario, dado una ID, se autocompleta con los datos correspondiente a la pelicula de dicha ID
dando la posibilidad de modificar estos datos y los reemplaza en la base de datos
"""
def conectar():
    print(os.path.dirname(__file__))
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def buscar_id(num):
        """
        retorna una lista con todos los valores de la fila buscada (5 en total)
	recibe id y devuelve arreglo con todos los datos
	"""
	con = conectar()
	c = con.cursor()
    	con.row_factory = sqlite3.Row
    	querry = "SELECT * FROM pelicula WHERE id = ?"
	resultado = c.execute(querry,[num])
	lista = resultado.fetchall()
	con.close();
    	l=[None,None,None,None,None,None,None]
	#print(len(l))
    	for i in range (0,7):#se rellena el arreglo vacío
        	l[i]=lista[0][i]
	return l



def obtener_peliculas():
    """
    Obtiene los datos de peliculas
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM pelicula"
    resultado= c.execute(query)
    peliculas = resultado.fetchall()
    con.close()
    return peliculas

def borrar(id):
    """
    Borra de pelicula buscando la id
    """
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM pelicula WHERE id = ?"
    try:
        resultado = c.execute(query, [id])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def crear_pelicula(nombre,estreno, pais, descripcion,imagen):
    """
    Inserta una pelicula nueva a la base de datos
    """
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO pelicula (nombre,estreno, pais, descripcion,imagen)"
        "VALUES (?, ?, ?, ?,?)")
    c.execute(sql,(nombre,estreno, pais, descripcion,imagen))
    con.commit()

def checkea_pelicula(nombre):
    """
    Devuelve true si encuentra alguna pelicula del nombre recibido como parametro, false si no.
    """
    existe=True
    con=conectar()
    c=con.cursor()
    query="SELECT * FROM pelicula WHERE nombre= ?"
    resultado=c.execute(query,[nombre])
    lista=resultado.fetchall()
    con.close()
    if(len(lista)==0):
        existe=False
    return existe
  
def actualiza(id,nombre,estreno, pais, descripcion,imagen):
   """
   Actualiza el valor editado por el usuario
   """
   con=conectar()
   c=con.cursor()
   sql=('UPDATE pelicula SET nombre="'+nombre+'", estreno="'+estreno+'", pais="'+pais+'",descripcion="'+descripcion+'",imagen="'+imagen+'"\
     WHERE id ="'+str(id)+'"')
   c.execute(sql)
   con.commit()
  
def filtro_pelicula(actor):
    """
    Recibe un actor mostrando todas las peliculas donde a estado ese actor
    """
    con = conectar()
    c = con.cursor()
    actor="'"+actor+"'))"
    query = ("SELECT * FROM pelicula "
             "WHERE ID IN (SELECT pelicula_id FROM elenco "
             "WHERE actor_id IN "
             "(SELECT id FROM actor "
             "WHERE nombre="+actor+" COLLATE NOCASE"
         )
    result = c.execute(query)
    peliculas = result.fetchall()
    return peliculas  

def contar_actor(id_p):
    """
    Cuenta la cantidad de actores que tiene una peliculas
    """
    con = conectar()
    c = con.cursor()
    id_p=str(id_p)
    id_p="'"+id_p+"'"
    query = ("SELECT * FROM elenco "
             "WHERE pelicula_id ="+id_p
         )
    result = c.execute(query)
    peliculas = result.fetchall()
     #recordar cambiar el nombre del retorno
    return peliculas
