# -------------------------------------------------------------
# EJERCICIO 2 - UNIDAD 1
#
# Enunciado:
# Escribe un programa que pida al usuario dos números y muestre 
# cuál es mayor o si son iguales.
#
# Explicación:
# El programa solicita dos números al usuario y luego usa 
# condicionales para comparar ambos valores. Dependiendo de la 
# comparación, indica cuál número es mayor o si ambos son iguales.
# -------------------------------------------------------------

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if a > b:
    print("El primer número es mayor")
elif b > a:
    print("El segundo número es mayor")
else:
    print("Ambos números son iguales")
