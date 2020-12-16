# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:58:39 2020

@author: AMASIFUEN
"""


import sqlite3
conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
consulta = """  SELECT 
                    idproducto,
                    nombre,
                    codigo,
                    precio
                FROM 
                    producto
               
                    
            """
cursor = conexion.cursor()
cursor.execute(consulta)
productos = cursor.fetchall()

print("ID   NOMBRE  CODIGO  PRECIO")
for producto in productos:

    print(producto)

conexion.close()