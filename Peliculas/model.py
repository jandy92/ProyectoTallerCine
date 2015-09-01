#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def connect():
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con
def crear_pelicula(nombre, estreno, pais,descripcion,director_id,imagen):
    con = connect()
    c = con.cursor()
    sql = (
        "INSERT INTO pelicula (nombre, estreno, pais,descripcion,director_id,imagen)"
        "VALUES (?, ?, ?, ?,?,?)")
    c.execute(sql, (nombre, estreno, pais,descripcion,director_id,imagen))
    con.commit()

def crear_elenco(personaje, descripcion_rol, actor_nombre,pelicula_nombre):
    con = connect()
    c = con.cursor()
    actor_id=actor_nombre
    pelicula_id=pelicula_nombre
    sql = (
        "INSERT INTO elenco (personaje, descripcion_rol, actor_id,pelicula_id)"
        "VALUES (?, ?, ?, ?)")
    c.execute(sql, (personaje, descripcion_rol, actor_id,pelicula_id))
    con.commit()
def find_id_movie(movie):
    
    con = connect()
    c = con.cursor()
    movie="'"+movie+"'"
  
    query = (
             "SELECT id FROM actor "
             "WHERE nombre="+movie
         )
    
    result = c.execute(query)

    return result
def find_id_actor(actor):
    
    con = connect()
    c = con.cursor()
    
    actor="'"+actor+"'"
  
    query = (
             "SELECT id FROM actor "
             "WHERE nombre="+actor
         )
    
    result = c.execute(query)
    return result
def filter_movie(actor):
    
    con = connect()
    c = con.cursor()
    
    actor="'"+actor+"'))"
  
    query = ("SELECT * FROM pelicula "
             "WHERE ID IN (SELECT pelicula_id FROM elenco "
             "WHERE actor_id IN "
             "(SELECT id FROM actor "
             "WHERE nombre="+actor
         )
    
    result = c.execute(query)

    movies = result.fetchall()
    return movies
def actor_count(id_p):
    
    con = connect()
    c = con.cursor()
    id_p=str(id_p)
    id_p="'"+id_p+"'"
  
    query = ("SELECT * FROM elenco "
             "WHERE pelicula_id ="+id_p
         )
    
    result = c.execute(query)
    movies = result.fetchall()
     #recordar cambiar el nombre del retorno
    return movies

def delete_movie(nombre):
    
    con = connect()
    c = con.cursor()
    nombre="'"+nombre+"'"
    nombre="WHERE nombre="+nombre
    
    print(nombre)
    
    query = (
        "DELETE FROM pelicula "
        +nombre)
    result = c.execute(query)
    movies = result.fetchall()
    con.commit()
    return movies
def get_movies():
    con = connect()
    c = con.cursor()
    query = (
        "SELECT id, nombre, estreno, pais,"
        " descripcion,"
        " director_id, imagen FROM pelicula ORDER BY id ASC")
    result = c.execute(query)
    movies = result.fetchall()
    return movies
if __name__ == "__main__":
    find_id_movie("Iron Man")
	
