#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_director():
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

def crear_director(nombre, pais, fecha_nacimiento,fecha_defuncion):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO director (nombre, pais, fecha_nacimiento,fecha_defuncion)"
        "VALUES (?, ?, ?, ?)")
    c.execute(sql, (nombre, pais, fecha_nacimiento,fecha_defuncion))
    con.commit()

if __name__ == "__main__":

    directores = obtener_director()
    for director in directores:
        print director["nombre"]

