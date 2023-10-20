import numpy as np

"""
Ejercicio 2. Elaborar un script el cual:
1. Genere el siguiente array 2D:

   [5  10 15 20
    25 30 35 40
    45 50 55 60
    65 70 75 80]

   de 2-D de manera manual.
2. Imprimir en pantalla el array.
"""

a = np.array([np.arange(5, 25, 5), np.arange(25, 45, 5),
             np.arange(45, 65, 5), np.arange(65, 85, 5)])

print(a)
