"""
Ejercicio 5: Elaborar un script el cual
1. Tenga una función llamada sumador_funcion(num_1, num_2)
y reciba dos parámetros de entrada
2. Retorne el valor de la suma.
3. Imprimir en pantalla el resultado, con solo tres dígitos
"""


def sumador_funcion(num_1, num_2):
    return round(num_1+num_2, 3)


num_1 = float(input("Ingrese número 1: "))
num_2 = float(input("Ingrese número 2: "))

print(f"{num_1}+{num_2} = {sumador_funcion(num_1, num_2)}")
