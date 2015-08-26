#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_pelicula():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM pelicula"
    resultado= c.execute(query)
    actores = resultado.fetchall()
    con.close()
    return peliculas

def delete(id):
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

def crear_director(nombre, estreno, pais, descripcion, director_id):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO director (nombre, estreno, pais, descripcion, director_id)"
        "VALUES (?, ?, ?, ?, ?)")
    c.execute(sql, (nombre, estreno, pais, descripcion, director_id))
    con.commit()

if __name__ == "__main__":

    peliculas = obtener_pelicula()
    for pelicula in peliculas:
        print pelicula["nombre"]
