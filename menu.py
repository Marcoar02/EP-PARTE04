# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:33:50 2020

@author: AMASIFUEN
"""

import os

def listar():
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
    
def agregar():
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

def eliminar():
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
    
def modificar():
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
    
    

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Datos Producto"
            "\t1 - Listar"
            "\t2 - Agregar"
            "\t3 - Eliminar"
            "\t4 - Modificar"
            "\t5 - Salir")


 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = str(input("inserta un numero valor >> "))
 
	if opcionMenu=="1":
		listar()
	elif opcionMenu=="2":
		agregar()
	elif opcionMenu=="3":
		eliminar()
	elif opcionMenu=="4":
		modificar()

	else:
		break
	

