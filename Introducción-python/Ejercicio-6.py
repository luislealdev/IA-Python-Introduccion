"""
Ejercicio 4: Elaborar un script el cual
1. Tenga una función llamada menor_funcion(num_1, num_2) y reciba dos
parámetros de entrada
2. Retorne el valor más pequeño.
3. Imprimir en pantalla el resultado utilizando el comando str
"""


def menor_funcion(num_1, num_2):
    if (num_1 < num_2):
        valor_menor = num_1
    else:
        valor_menor = num_2
    return valor_menor


num_1 = float(input("Ingrese número 1: "))
num_2 = float(input("Ingrese número 2: "))

print(f"El valor menor es {str(menor_funcion(num_1, num_2))}")
