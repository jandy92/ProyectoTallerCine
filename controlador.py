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

def delete(id):
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


if __name__ == "__main__":

    actores = obtener_actor()
    for actor in actores:
        print actor["nombre"]
