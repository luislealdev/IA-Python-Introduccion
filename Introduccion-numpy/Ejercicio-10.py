import numpy as np
"""
Ejercicio 10. Elaborar un script el cual:
1. Ordene de manera aleatoria la siguiente lista con nombres:

   ['Python', 'C++', 'C', 'Fortran', 'Java', 'JavaScript', 'Kotlin']

2. Imprimir en pantalla la lista.
3. Imprimir en pantalla el arreglo desordenado.
"""

a = ['Python', 'C++', 'C', 'Fortran', 'Java', 'JavaScript', 'Kotlin']
print(a)
a = np.random.permutation(a)
print(a)