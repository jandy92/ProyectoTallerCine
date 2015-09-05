#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    """
    se conecta con la base de datos
    """
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_actor():
    """
    obtiene todos los actores de la base de datos
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM actor"
    resultado= c.execute(query)
    actores = resultado.fetchall()
    con.close()
    return actores

def num_peli():
  """
  cuenta la cantidad de peliculas
  """
  con = conectar()
  c = con.cursor()
  query = "SELECT COUNT(*) FROM pelicula"
  resultado = c.execute(query)
  num=resultado.fetchall()
  return num[0][0]

def actuaciones(actor):
	"""
	cuenta la candidad de peliculas en las que se actuado un actor
	"""  
	con = conectar()
	c = con.cursor()
	query = "SELECT COUNT(*) FROM elenco WHERE actor_id= ?"
	resultado = c.execute(query, [actor])
	num=resultado.fetchall()
	return num[0][0]

def llena_box():
	"""
	retorna un arreglo con los nombres de las peliculas que hay en la base de datos
	"""
	con = conectar()
	c = con.cursor()
	query = "SELECT nombre FROM pelicula"
	resultado = c.execute(query)
	pelicula=resultado.fetchall()	
	return pelicula

def peli_id(pelicula):
	"""
	retorna la id de una pelicula pedida
	"""
	con = conectar()
	c = con.cursor()
	#query=("SELECT id FROM pelicula")
	query = ('SELECT ID FROM pelicula WHERE nombre='+'"'+pelicula+'"')
	result = c.execute(query)
	id = result.fetchall()
	#print("----------------------------------"+result)
	return id[0][0]

def filtro_actor(pelicula):
	"""
	retorna un arreglo con la informacion de los actores
	"""
	con = conectar()
	c = con.cursor()
	pelicula_id = peli_id(pelicula)
	query = ("SELECT actor_id FROM elenco WHERE pelicula_id= ?" )
	result = c.execute(query, [pelicula_id])
	actores = result.fetchall()
	
	for i in range (0,len(actores)):
	  #print(actores[i][0])
	  actores[i]=actores[i][0]
	query2=("SELECT * from actor where id IN (")
	for i in range (0,len(actores)):
	  if(i==0):
	    query2+=str(actores[i])
	  else:
	    query2+=","+str(actores[i])
	    
	query2+=")"
	print(query2)
	result2 = c.execute(query2)
	actores2 = result2.fetchall()
	print (actores2)
	return actores2
"""
def filtro_pelicula(pelicula):
    con = conectar()
    c = con.cursor()
    pelicula="'"+pelicula+"'))"
    query = ("SELECT * FROM actor "
             "WHERE ID IN (SELECT actor_id FROM elenco "
             "WHERE pelicula_id IN "
             "(SELECT id FROM pelicula "
             "WHERE nombre="+pelicula+" COLLATE NOCASE"
         )
    result = c.execute(query)
    actores = result.fetchall()
    return actores  
"""

def borrar(id):
    """
    borra un actor de la base de datos
    """
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
    """
    crea un actor en la base de datos con los datos entregados
    """
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO actor (nombre, birthday, genero,imagen)"
        "VALUES (?, ?, ?, ?)")
    c.execute(sql, (nombre, birthday, genero,imagen))
    con.commit()

def checkea_actor(nombre):
    """ 
    devuelve true si encuentra algun actor con el nombre recibido como parametro, false si no.
    """
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
   """
   actualiza el actor en la base de datos
   """
   con=conectar()
   c=con.cursor()
   sql=('UPDATE actor SET nombre="'+nombre+'", birthday="'+birthday+'", genero="'+genero+'",imagen="'+imagen+'"\
     WHERE id ="'+str(id)+'"')
   c.execute(sql)
   con.commit()


def buscar_id(num):
	"""
	retorna una lista con todos los valores de la fila buscada (5 en total)
	recibe id y devuelve arreglo con todos los datos
	"""
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
	#print filtro_pelicula("Pulp Fiction")	
	print peli_id('Lucy')
    	print filtro_actores('Lucy')


"""







