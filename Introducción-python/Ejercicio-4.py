"""
Ejercicio 4: Elaborar un script el cual:
1. Genere la función de nombre fahrenheit
2. Reciba el párametro c, de temperatura en grados C
3. Calcule la temperatura en grados Fahrenheit
4. Imprima la temperatura en grados Fahrenheit
"""

def fahrenheit(c):
  c = float(input('Ingrese el valor en grados centigrados: '))
  F = (9/5) * c +32
  print(F)

fahrenheit(98)