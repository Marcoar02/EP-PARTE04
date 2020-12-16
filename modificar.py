# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:28:35 2020

@author: AMASIFUEN
"""


import sqlite3
conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
print("Ingrese codigo de producto:")
codigo_ingreso = input()
print("Ingrese nuevo nombre de producto:")
nombre_ingreso = str(input())
print("Ingrese nuevo precio de producto:")
precio_ingreso = input()
consulta = """
            UPDATE producto
            SET
                NOMBRE = '%n'
                precio = '%p'

            WHERE
                codigo = '%c'
            """ %(nombre_ingreso , precio_ingreso ,codigo_ingreso)
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
