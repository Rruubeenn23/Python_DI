# %% 1. Cabecera
"""
Autor: Rubén Cereceda
Clase: Diseño de Interfaces
"""
# %% 2. Importar Módulos
import numpy as np

# %% 3. Declaramos Variables

n_filas1, n_columnas1 = 4, 2
n_filas2, n_columnas2 = 2, 2
n_filas3, n_columnas3 = 4, 3

# %% 4. Programa a pelo

# M = []  #Inicializamos la matriz
#

# for i in range (n_filas1):
#     filai1 = []
#     for j in range (n_columnas1):
#         filai1.append(c)
#         c += 1
#     M.append(filai1)

# %% 5. Programa Bonito
# M = [[0 for _ in range (n_columnas1)]
#      for _ in range (n_filas1)]
# for i in range (n_filas1):
#     for j in range (n_columnas1):
#         M[i][j] = [[0 for _ in range (n_columnas2)] for _ in range (n_filas2)]
#         for ii in range (n_filas2):
#             for jj in range (n_columnas2):
#                 M[i][j][ii][jj] = [[0 for _ in range (n_columnas3)] for _ in range (n_filas3)]
#                 c = 1 #Contador
#                 for iii in range (n_filas3):
#                     for jjj in range (n_columnas3):
#                         M[i][j][ii][jj][iii][jjj] = c
#                         c += 1
                        
# print (M[1][1][1][1][1][1])

# %% 6. Programa con Numpy
MatrizNumpy = np.arange(1, n_filas1 * n_columnas1 * n_filas2 * n_columnas2 * n_filas3 * n_columnas3 + 1)
MatrizNumpy = np.reshape(MatrizNumpy, (n_filas1, n_columnas1, n_filas2, n_columnas2, n_filas3, n_columnas3))
