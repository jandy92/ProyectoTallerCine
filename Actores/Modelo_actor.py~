#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_actor():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM actor"
    resultado= c.execute(query)
    actores = resultado.fetchall()
    con.close()
    return actores

def borrar(id):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM actor WHERE id = ?"
    try:
        resultado = c.execute(query, [id])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def crear_actor(nombre, birthday, genero,imagen):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO actor (nombre, birthday, genero,imagen)"
        "VALUES (?, ?, ?, ?)")
    c.execute(sql, (nombre, birthday, genero,imagen))
    con.commit()

def checkea_actor(nombre):#devuelve true si encuentra algun actor con el nombre recibido como parametro, false si no.
    existe=True
    con=conectar()
    c=con.cursor()
    query="SELECT * FROM actor WHERE nombre= ?"
    resultado=c.execute(query,[nombre])
    lista=resultado.fetchall()
    con.close()
    if(len(lista)==0):
        existe=False
    return existe

def actualiza(id,nombre, birthday, genero, imagen):
   con=conectar()
   c=con.cursor()
   sql=('UPDATE actor SET nombre="'+nombre+'", birthday="'+birthday+'", genero="'+genero+'",imagen="'+imagen+'"\
     WHERE id ="'+str(id)+'"')
   c.execute(sql)
   con.commit()


def buscar_id(num):#retorna una lista con todos los valores de la fila buscada (5 en total)
	# recibe id y devuelve arreglo con todos los datos
	con = conectar()
	c = con.cursor()
    	con.row_factory = sqlite3.Row
    	querry = "SELECT * FROM actor WHERE id = ?"
	resultado = c.execute(querry,[num])
	lista = resultado.fetchall()
	con.close();
    	l=[None,None,None,None]
	#print(len(l))
    	for i in range (0,4):#se rellena el arreglo vacío
        	l[i]=lista[0][i+1]
	return l


"""
if __name__ == "__main__":

    
    datos = buscar_id(3)
    for dt in datos:
        print dt
"""
