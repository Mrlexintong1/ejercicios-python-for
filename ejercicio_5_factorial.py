# Ejercicio 5: Calcular el factorial
numero = int(input("Ingrese un número entero: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es {factorial}.")
