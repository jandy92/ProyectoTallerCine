#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def connect():
    con = sqlite3.connect('../ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con
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
    print(query)
    result = c.execute(query)
    movies = result.fetchall()
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
        " director_id FROM pelicula ORDER BY id ASC")
    result = c.execute(query)
    movies = result.fetchall()
    return movies
