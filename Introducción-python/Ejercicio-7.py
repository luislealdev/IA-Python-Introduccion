"""
Ejercicio 5: Elaborar un script el cual
1. Tenga una función llamada comparador_funcion(num_1, num_2) y reciba dos
parámetros de entrada
2. La función debe imprimir la relación entre los dos números: menor que,
mayor que o igual que.
3. La función no retorna ningún valor
"""


def comparador_funcion(num_1, num_2):
    if (num_1 < num_2):
        aux = "menor"
    elif (num_1 > num_2):
        aux = "mayor"
    else:
        aux = "igual"

    print(f"El número {num_1} es {aux} al número {num_2}")


num_1 = float(input("Ingrese número 1: "))
num_2 = float(input("Ingrese número 2: "))

comparador_funcion(num_1, num_2)
