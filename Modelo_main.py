#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_clave(user):
    """
    Entrega la clave
    """
    con = conectar()
    c = con.cursor()
    query = 'SELECT clave FROM usuarios where usuario ="'+user+'"'
    resultado= c.execute(query)
    clave = resultado.fetchall()
    con.close()
    return clave[0][0]

def usuario_existe(user):
    """
    Revisa si el usuario esta en la base de datos
    """
    existe=False
    con = conectar()
    c = con.cursor()
    query = 'SELECT usuario FROM usuarios where usuario ="'+user+'"'
    resultado= c.execute(query)
    respuesta = resultado.fetchall()
    print len(respuesta)
    if len(respuesta)>0:
	if (respuesta[0][0] == user):
    		existe=True
    return existe
