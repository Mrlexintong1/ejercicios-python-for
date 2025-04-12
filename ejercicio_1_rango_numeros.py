# Ejercicio 1: Rango entre dos números
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

if inicio > fin:
    inicio, fin = fin, inicio

for numero in range(inicio, fin + 1):
    print(numero)
