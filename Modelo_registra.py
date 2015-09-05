#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('ProyectoCine.db')
    con.row_factory = sqlite3.Row
    return con

def agrega_usuario(nu_usuario, nu_clave):
    """
    Ingresa al usuario a la base de datos
    """
    con = conectar()
    c = con.cursor()
    sql = ("INSERT INTO usuarios (usuario, clave)"
        "VALUES (?, ?)")
    c.execute(sql, (nu_usuario, nu_clave))
    con.commit()  

if __name__ == '__main__':
   agrega_usuario("Acdoisanc", "123321123")
