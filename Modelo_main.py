#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_clave(user):
    con = conectar()
    c = con.cursor()
    query = 'SELECT clave FROM usuarios where usuario ="'+user+'"'
    resultado= c.execute(query)
    clave = resultado.fetchall()
    con.close()
    return clave[0][0]

def usuario_existe(user):
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

"""
if __name__ == '__main__':
   esta = usuario_existe("HumbertoCampos")
   if esta:
	print "esta"
   else:
	print "nop"
"""
