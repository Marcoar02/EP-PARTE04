# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:22:29 2020

@author: AMASIFUEN
"""


import sqlite3
conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()

print("Ingrese codigo de producto:")
codigo_ingreso = input()
consulta = """
            DELETE FROM producto
            WHERE
            codigo = '%s'
            """ % codigo_ingreso
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()