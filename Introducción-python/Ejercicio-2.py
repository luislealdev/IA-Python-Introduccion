"""
Ejercicio 2: Elaborar un script el cual
1. Solicite al usuario la temperatura en grados Celsius
2. Convertir los grados Celsius a grados Fahrenheit utilizando la fórmula: Fahrenheit = (9/5) * Celsius + 32
3. Imprimir en pantalla ambas temperaturas, con solo dos decimales
"""

Celsius = float(input("Temperatura en °C: "))
Fahrenheit = (9/5) * Celsius + 32
print(f'La temperatura en °C es: {Celsius} °C')
print(f'La temperatura en °F es: {Fahrenheit} °F')
