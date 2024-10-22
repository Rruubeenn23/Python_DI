# %% 1. Cabecera
"""
Autor: Rubén Cereceda
Clase: Diseño de Interfaces
"""
# %% 2. Importar Módulos
import numpy as np
# %% 3. Consideraciones
# print("Hola mundo")
# %% 4. Pedir Información
# nombre = input("¿Cuál es tu nombre? ")
# edad = int(input("¿Cuál es tu edad? "))
# if edad > 25:
#     print ("Hola te llamas", nombre, "y tienes", edad, "lo que significa que eres un poco viejo")
# else:
#     print("Hola te llamas", nombre, "y tienes", edad, "lo que significa que eres un poco joven")

# %%4. Chequeo de Errores
# # Verificar nombre
# nombre = input("¿Cuál es tu nombre? ")
# if nombre.isdigit():
#     print("Error, mete un String")
#     exit()
# # Verificar número
# try:
#     edad = int(input("¿Cual es tu edad? "))
# except ValueError:
#     print("Mete un número")
#     exit()
# %%5. Tipos de datos
##################################################################
# Variables modificables #
##################################################################
"""
int, str, tuplas, float, bool
"""
# 4.1 int
# a = 10
# b = 10
# print(id(a),id(b))

# 4.2 str

# 4.3 tuplas
"""
.....
"""
# tupla = (1,2,3)
# # # print(tupla[0])
# # tupla = tupla + (4,)
# # print (tupla)

# # # Acceder a los elementos
# # E2 = tupla[1]
# # Primera funcion
# def calc_suma(a,b):
#     suma = a + b
#     resta = a - b
#     return suma, resta

# resultado = calc_suma(10, 5)

# a, b, c, d = tupla

#  4.4 Listas
# Creación
# lista = [1, 2, 3, 4]
# E0 = print(lista[0])
# Listas anidadas
# lista_anidada = [1, 2, 3, [4, 5, [6, 7]]]

# 4.5. Diccionario
# diccionario = {"nombre": "Sebastian", "edad": 19}
# print(diccionario["nombre"])
# print(diccionario["edad"])
# diccionario["gusto"] = "Jugar a Cs2"

# diccionario = {"nombre": "Sebastian", "edad": 19, "estudios": ["ESO", "SMR"]}
# claves = diccionario.keys()

# print(diccionario["estudios"][0])

# 4.6. Bases De Datos
# empleados = {
#     "empleado 1": {"nombre": "Sebastian", "Nota": -2} ,
#     "empleado 2": {"nombre": "Javi", "Nota": 1.5}
#     }
# print (empleados["empleado 1"]["Nota"])
# Valores = diccionario.values()
# print(Valores)
# edad_sebastian = diccionario.get("edad")
# print(edad_sebastian)

# print(diccionario.get("estudios"))

# print (diccionario.get("estudios")[0])

#4.7. Conjuntos
# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5}
# i = conjunto1.intersection(conjunto2)
# print(i)
# u = conjunto1.union(conjunto2)
# print(u)

# 4. 8. Booleanos
# booleano = 5 > 3

# Solicitar fecha de entrega y coste
# fecha_entrega = int(input("Introduce los días restantes para la fecha de entrega: "))
# c = int(input("Introduce el coste: "))

# # Determinar la urgencia del pedido
# if fecha_entrega < 2 and c > 100:
#     print("Es un pedido urgente.")
# elif fecha_entrega >= 2 and c > 100:
#     print("Es un pedido de prioridad media.")
# elif fecha_entrega >= 2 and c < 100 or fecha_entrega < 2 and c < 100:
#     print("El pedido se debe almacenar.")
# else:
#     print("El pedido no cumple con ninguna categoría específica.")

#Para calcularel cuadrado de algo se usa doble ** ejemplo radio**2
# Condicionales
# x = 20
# if x >10:
#     print(f"{x} es mayor que 10") #Se pone una f adelante porque formatea el texto, preguntarle a chatgpt
#     # ademas esto hace que imprima el valor de x
    
# elif x == 10:
#     print(f"{x} es igual que 10")
# else:
#     print(f"{x} es menor que 10")
# en una sola linea
# x = 5
# print(f"{x} es > que 5" if x>5 else f"{x} es menor o igual que 5")
# Condicionales y listas 
# colores = ["rojo", "azul" , "verde" , "amarillo"]
# color = "rojo"
# if color in colores:
#     print(f"El color {color} esta dentro de la lista {colores}")
# else:
#     print(f"El color {color} no esta dentro de la lista {colores}")

# colores = ["rojo", "rojo" , "rojo" , "amarillo"]

# contador_rojo = colores.count("rojo") 

# print(f"La palabra rojo aparece {contador_rojo} veces ")

# en una linea

#   print(f"La palabra rojo aparece {colores.count('rojo')} veces")


#switch-case --> match-case
# animal = "perro"
# match animal:
#     case = "gato":

# diccionario = {"Sebastian": 19, 
#                "Daniel": 21,
#                "Javier": 19,
#                "Manu": 26,
#                "Ana" : 30
#                }
# for persona in diccionario:
#     if diccionario[persona]>= 18:
#         print(f"{persona} es mayor de edad")
#     else:
#         print(f"{persona} es menor de edad")
#         #Ten cuidado con el orden
# #Si pones el else detras junto al for el else pertenecera al for y no al if siempre poner las cosas al mismo nivel

# ### all (y)y any (or) 
# x, y ,z = 5, 10, 15
# if all([x>0, y > 0, z > 0]):
#     print(f"Todos son mayores que 0")
# else:
#     print(f"Todos son menores que 0")

### all (y)y any (or) con listas

# lista = [1, -2, -3, -4]
# if all([lista[0]>0, lista[1] > 0, lista[2] > 0, lista[3] > 0]):
#     print(f"Todos son mayores que 0")
# if any([lista[0]>0, lista[1] > 0, lista[2] > 0, lista[3] > 0]):
#     print(f"Al menos uno es mayor que 0")
# else:
#     print(f"Todos son menores que 0")


##################################################################
# Variables inmodificables #
##################################################################

# %% 6. Bucles
#1. For
# frutas = ['manzana', 'cereza', 'plátano']
# for fruta in frutas:
#     print (f"Mi fruta es {fruta}")
# diccionario = {'d' : 1, 'a' : 3, 'Sebastian': 4}
# for c in diccionario: 
#     print(f"La clave es {c}")
    
# for valores in diccionario.values(): 
#     print(f"Los valores son {valores}")

# diccionario2 = {
#     'Sebastian': {'Coche': {'Marca': 'Honda', 'kms': 100000}},
#     'Javier': {'Coche': {'Marca': 'Mercedes', 'kms': 200000}},
#     'Manu': {'Coche': {'Marca': 'Ferrari', 'kms': 300000}}
# }

# for clave in diccionario:
#     print(f"La clave es {diccionario[clave]}")

# for nombre, detalle in diccionario2.items():
#     print (f"El coche de {nombre} es un {detalle['Coche']}")

# for clave in diccionario2:
#     print (f"Los kms del coche de {clave} son {diccionario2[clave]['Coche']['kms']}")
# palabra = "HoLa MuNdO"
# for letra in palabra: 
#     print(letra)

# Instrucciones especiales --> Break, continue
# n = [1, 2, 3, 4, 5]
# for numero in n:
#     if numero == 4:
#         break
#     print (numero)

# n = [1, 2, 3, 4, 5]
# for numero in n:
#     if numero == 4:
#         continue
#     print (numero)

# lista = [x**2 for x in range (1, 6)]
# print (lista)

# diccionario = {x : x**2 for x in range (1,6)}

# nombres = ["Sebastian", "Javier", "Manu"]
# edades = [19, 19, 26]
# for n, e in zip(nombres, edades):
#     print(f"La edad de {n} es {e}")

# for i in range (11, 0, -2):
#     print(i)

# %%7. Funciones
# def nombre(parametros):
#     """
#     Descripción de la funcion: .................
#     Explicación: 
#         Entradas: 
#             ---
#             ---
#         Salidas: 
#             ---
#             ---
#     """
#     #Chequeo de errores
    
# def saludar(nombre = None):
#     if nombre is None:
#         nombre = 'Amigo'
#         print("Error, no has introducido el nombre")
#     return f"Hola {nombre}"
    
    
# saludar()

# import pruebaFunciones as f

# a = 1
# b = 16

# print (f.suma(a, b))

# %%8. Clases

#Clase normal
# class Coche : 
#     def __init__(self, marca, modelo, color, cv):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.cv = cv
#     def describirCoche(self):
#         return f"Mi coche era un {self.marca} {self.modelo} de color {self.color} con {self.cv} cv"
        
#     def caballos(self):
#         return f"El coche tiene {self.cv} cv"
    
#     def cambiarColor(self, nuevoColor):
#         self.color = nuevoColor
        
# miCoche = Coche("Opel", "Astra", "Negro", 110)       
# print(miCoche.describirCoche()) 
# print(miCoche.caballos())
# miCoche.cambiarColor("Rojo")
# print(miCoche.describirCoche()) 
        

# Herencia Y Poliformismo
# class Animal : 
#     def __init__(self, nombre):
#         self.nombre = nombre
    
#     def hablar(self):
#         return f"{self.nombre} hace x sonido"
    
#     def raza(self, raza):
#         self.raza = raza
#         return f"La raza de {self.nombre} es {self.raza}"
    

# class Perro (Animal):
#     def hablar(self):
#         return f"{self.nombre} hace Guau"

# mi_perro = Animal("Lala")
# print(mi_perro.hablar())
# mi_perro2 = Perro ("Lala")
# print(mi_perro2.hablar())
# print(mi_perro2.raza("Border Collie"))


# Composición

# class Tipo_Motor:
    
#     def __init__(self, cv):
#         self.cv = cv
    
# class Coche:
    
#     def __init__(self, marca, modelo, cv):
#         self.marca = marca
#         self.modelo = modelo
#         self.cv = Tipo_Motor(cv)
        
#     def detalles (self):
#         return f"El coche es un {self.marca}, {self.modelo}, con {self.cv.cv} cv"

# coche1 = Coche("Opel", "Astra", 110)
# print(coche1.detalles())


# Agregación

# class Profesor:
#     def __init__(self, nombre):
#         self.nombre = nombre
        
# class Instituto:
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.profesores = []
    
#     def añadir_profesores(self, profesor):
#         self.profesores.append(profesor)
            
#     def mostrar_profesores(self):
#         for profesor in self.profesores:
#             print(profesor.nombre)

# instituto1 = Instituto("Las Salinas - Tarde")

# profesor1 = Profesor ("Manuel")
# profesor2 = Profesor ("Dani")
# profesor3 = Profesor ("Vicente")

# instituto1.añadir_profesores(profesor1)
# instituto1.añadir_profesores(profesor2)
# instituto1.añadir_profesores(profesor3)

# instituto1.mostrar_profesores()


# Clases Abstractas

# from abc import ABC, abstractmethod

# class Animal(ABC):
    
#     @abstractmethod
#     def sonido (self):
#         pass # Pasa al método de cada clase hija
    
#     def come(self):
#         return f"El animal está comiendo"
    
# class Perro (Animal) :
#     # def info (self, nombre):
#     #     self.nombre = nombre
#     #     return f"El animal se llama {self.nombre}"
#     def sonido(self):
#         return f"Guau"
    
# class Gato (Animal) :
#     def Saltar (self):
#         return f"El gato salta"
    
#     def sonido (self):
#         return f"Miau"
    

# perro = Perro()
# gato = Gato()
# print (perro.sonido())
# print (gato.sonido())


# Variables globales y locales

# x = 'global'

# def ejemplo ():
#     x = 'local'
#     print (x)
    
# ejemplo()
# print(x)


# Modificar la variable global

# x = 'Global'

# def cambiar_var_global():
#     global x 
#     x = 'Global_modificada'
#     print(x)

# cambiar_var_global()
# print(x)

# def externa ():
#     x = 'Externa'
    
#     def interna ():
#         nonlocal x 
#         x = 'Externa_Modificada'
#         print(x)
#     interna()
    
# externa()

# %% 9. Extraer y pedir información de ficheros, tratarla y devolverla

# 1. Extraer y tratarla
# Módulo pandas = Leer, tratar, escribir, etc. 
# import pandas as  pd

# Leer
# archivo = pd.read_csv('empleados.csv')

# Extraer información
# print("Los datos de los empleados son: ", archivo)
## Acceder a columnas
# print("\nLos nombres son: ", archivo['nombre'])
## Acceder a filas 
# primer_empleado = archivo.loc[0]
##Acceder a un valor en concreto
# valor_especifico = archivo.at[2, 'salario_mensual']
# print("El salario del tercer empleado es: ", valor_especifico, "€")

# 2. Pedir información por pantalla y cargarla
# nueva_fila = {
#     'nombre': 'Javier', 
#     'Edad' : 19,
#     'id_empleado' : 105,
#     'horas_trabajadas': 20,
#     'tarifa_hora' : 20,
#     'salario' : None
#     }
# nueva_fila_df = pd.DataFrame([nueva_fila])
# archivo = pd.concat([archivo, nueva_fila_df], ignore_index=True)

# Cargar Información
# from tkinter import Tk
# import pandas
# from tkinter.filedialog import askopenfilename

# Tk(). withdraw()

# # Pedimos al usuario que seleccione el archivo.csv
# file_path = askopenfilename(
#     title = 'Selecciona un archivo.csv' ,
#     filetypes = [("CSV files", "*.csv")])

# if file_path:
#     df = pd.read_csv(file_path)
# else:
#     print ("No has seleccionado ningún archivo")
    

# 3. Crear un archivo y grabarlo
# from tkinter import Tk
# import pandas
# from tkinter.filedialog import askdirectory
# import os 
# nombre_archivo = 'Empleados2.csv'
# data = {
#         'nombre': ['Sebastian', 'Javier', 'Manu', 'Iván'],
#         'edad': [19, 19, 26, 19],
#         'salario': [None, 1650, 1799, 4000]
#         }
# # Convertir a dataframe
# df = pd.DataFrame(data)
# carpeta_select = askdirectory(title = 'Selecciona una carpeta')
# if carpeta_select:
#     file_path = os.path.join(carpeta_select, nombre_archivo)
#     # Guardar dataframe
#     df.to_csv(file_path, index=False)
# else:
#     print("No has seleccionado ninguna carpeta")


# %% 9. Conexion a Bases de Datos 
"""Relacionales ----> MYSQLO/POSTGRESQL"""
# # pip install mysql-connector-python
# import mysql.connector
# from mysql.connector import Error
# import pandas as pd

# # Que necesitamos para una bdd: el host, database, user, password, port 

# # Funcion para conectar
# def connect_BD(host, database, user, password, port):
#     try:
#         connection = mysql.connector.connect(
#             host = host,
#             database = database,
#             user = user,
#             password = password,
#             port = port
#             )
#         if connection.is_connected():
#             print(f"La conexion ha sido realizada {database}")
#             return connection
#     except Error as e:
#             print(f"Error al conectarse: {e}")
#             return None

# # Funcion para leer    
# def read_BD(connection, tabla, columnas, limite_filas):
#     try:
#         cursor = connection.cursor()
#         # Peticion, Convertir la lista de columnas en cadena
#         columnas_str = ','.join(columnas)
#         query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"
#         # Ejecutamos la peticion
#         cursor.execute(query)
#         # Resultados 
#         resultados = cursor.fetchall()
#         # Obtener 
#         columna_resultado = [i[0] for i in cursor.description]
#         # Nos creamos el DataFrame
#         df = pd.DataFrame(resultados, columns = columna_resultado)
#         return df
#     except Error as e:
#         print(f"Error al leer la BD: {e}")
#         return None
        
# # Ejecutar
# if __name__ == '__main__':
#     # Parametros de conexion
#     host = 'mysql-rfam-public.ebi.ac.uk'
#     database = 'Rfam'
#     user = 'rfamro'
#     password = '' # No requiere contraseña 
#     port = 4497
#     tabla = 'family' # Tabla a consultar
#     #Columnas que quieres extraer
#     columnas = ['rfam_acc', 'rfam_id', 'description']
#     limite_filas = 5 #Numero de filas que quieres extraer
#     #Conectar a la BD
#     conexion = connect_BD(host, database, user, password, port)
#     if conexion:
#         # Leer 
#         df_BD = read_BD(connection, tabla, columnas, limite_filas)
#         if df_BD is not None:
#             print(df_BD)
#         conexion.close()
        
# import mysql.connector
# from mysql.connector import Error
# import pandas as pd

# # Función para conectar
# def connect_BD(host, database, user, password, port):
#     try:
#         connection = mysql.connector.connect(
#             host=host,
#             database=database,
#             user=user,
#             password=password,
#             port=port
#         )
#         if connection.is_connected():
#             print(f"La conexión ha sido realizada a {database}")
#             return connection
#     except Error as e:
#         print(f"Error al conectarse: {e}")
#         return None

# Función para leer    
# def read_BD(connection, tabla, columnas, limite_filas):
#     try:
#         cursor = connection.cursor()
#         # Petición, convertir la lista de columnas en cadena
#         columnas_str = ','.join(columnas)
#         query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"  # Espacio corregido en LIMIT
#         # Ejecutamos la petición
#         cursor.execute(query)
#         # Resultados 
#         resultados = cursor.fetchall()
#         # Obtener nombres de las columnas
#         columna_resultado = [i[0] for i in cursor.description]
#         # Nos creamos el DataFrame
#         df = pd.DataFrame(resultados, columns=columna_resultado)  # Corregido a 'columns'
#         return df
#     except Error as e:
#         print(f"Error al leer la BD: {e}")
#         return None

# # Ejecutar
# if __name__ == '__main__':
#     # Parámetros de conexión
#     host = 'mysql-rfam-public.ebi.ac.uk'
#     database = 'Rfam'
#     user = 'rfamro'
#     password = ''  # No requiere contraseña 
#     port = 4497
#     tabla = 'family'  # Tabla a consultar
#     # Columnas que quieres extraer
#     columnas = ['rfam_acc', 'rfam_id', 'description']
#     limite_filas = 5  # Número de filas que quieres extraer
#     # Conectar a la BD
#     conexion = connect_BD(host, database, user, password, port)
#     if conexion:
#         # Leer
#         df_BD = read_BD(conexion, tabla, columnas, limite_filas)
#         if df_BD is not None:
#             print(df_BD)
#         conexion.close()


# Conexión Mongodb
# mongodb+srv://ruben:<db_password>@rubencereceda.5qjcx.mongodb.net/?retryWrites=true&w=majority&appName=RubenCereceda
# import pymongo
# import pandas as pd

# try:
#     cliente = pymongo.MongoClient("mongodb+srv://ruben:<db_password>@rubencereceda.5qjcx.mongodb.net/?retryWrites=true&w=majority&appName=RubenCereceda")
#     print ("Conexión establecida")
    
# except Exception as e: 
#     print (f"Error en la conexión {e}")
#     exit()
    
# # Extraer información
# db = cliente["sample_mflix"]
# coleccion = db["movies"]

# # Hacer la consulta
# try:
#     resultados = coleccion.find().limit(10)
#     lista_resultados = list(resultados)
#     # Verificar si se extraen los resultados
#     if not lista_resultados:
#         print("No se han encontrado datos")
#     else:
#         print(f"Se han encontrado {len(lista_resultados)} documentos")
#         df = pd.DataFrame(lista_resultados)

# except Exception as e:
#     print(f"Error al realizar la consulta: {e}")


# %% 10. Consumo y creacion de APIs
# import requests
# # url
# url = "https://pokeapi.co/api/v2/pokemon?limit=150"
# # Respuesta
# respuesta = requests.get(url)

# lista_pokemon = respuesta.json()["results"]

# for pokemon in lista_pokemon:
#     print(pokemon["name"])        
        


# mongodb+srv://ruben:<db_password>@rubencereceda.5qjcx.mongodb.net/?retryWrites=true&w=majority&appName=RubenCereceda
# import pymongo
# import pandas as pd

# try:
#     cliente = pymongo.MongoClient("mongodb+srv://ruben:<db_password>@rubencereceda.5qjcx.mongodb.net/?retryWrites=true&w=majority&appName=RubenCereceda")
#     print ("Conexión establecida")
    
# except Exception as e: 
#     print (f"Error en la conexión {e}")
#     exit()
    
# # Extraer información
# db = cliente["sample_mflix"]
# coleccion = db["movies"]

# # Hacer la consulta
# try:
#     resultados = coleccion.find().limit(10)
#     lista_resultados = list(resultados)
#     # Verificar si se extraen los resultados
#     if not lista_resultados:
#         print("No se han encontrado datos")
#     else:
#         print(f"Se han encontrado {len(lista_resultados)} documentos")
#         df = pd.DataFrame(lista_resultados)

# except Exception as e:
#     print(f"Error al realizar la consulta: {e}")

# Creación Apis
# PVGIS
# import requests
# import json
# # URL
# url = "https://re.jrc.ec.europa.eu/api/v5_2/PVcalc?"

# # Parámetros
# params = {
#     'lat': 38.6759, 
#     'lon': -4.159, 
#     'peakpower': 1, 
#     'pvtechchoice': 'crystSi',
#     'loss': 14,
#     'outputformat': 'json'}

# # Realizar consulta
# respuesta = requests.get(url, params=params)
# data = json.loads(respuesta.text)

# print(f"La energía diaria estimada es: {data['outputs']['totals']['fixed']['E_d']} KWh")


# Crear APIs
# Crear la API

from flask import Flask, jsonify

app = Flask(__name__)

# Lista 1. 

@app.route('/api/lista1', methods=['GET'])

def obtener_lista1():
    datos = {
        "nombre": "Sebastian", 
        "edad": 19, 
        "residencia": "Seseña"}
    return jsonify(datos)
    
# Lista 2. 

@app.route('/api/lista2', methods=['GET'])

def obtener_lista2():
    lista_datos = [
        {"nombre": "Sebastian", "edad": 19, "residencia": "Seseña"},
        {"nombre": "Javier", "edad": 19, "residencia": "Seseña"},
        {"nombre": "Manu", "edad": 26, "residencia": "Cuidad Real"},
        {"nombre": "Tymur", "edad": 20, "residencia": "Seseña"}]
    return jsonify(lista_datos)

# Ejecutar la API
if __name__ == '__main__':
    app.run(debug=True)
    








