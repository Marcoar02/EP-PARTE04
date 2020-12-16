# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:05:00 2020

@author: AMASIFUEN
"""


import sqlite3
conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()

print(f"Ingrese nombre del producto:")
nombre = str(input())

print(f"Ingrese codigo del producto: ")
codigo = input()

print(f"Ingrese precio del producto:")
precio = input()

lista = [(nombre, codigo, precio)]
consulta = """  INSERT INTO PRODUCTO(NOMBRE,CODIGO,PRECIO)
                VALUES(?,?,?)
            """
cursor = conexion.cursor()
cursor.executemany(consulta, lista)
conexion.commit()

conexion.close()