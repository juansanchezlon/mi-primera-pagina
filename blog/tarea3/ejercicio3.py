# -------------------------------------------------------------
# EJERCICIO 3 - UNIDAD 1
#
# Enunciado:
# Escribe un programa que pida al usuario un número entero y 
# determine si es par o impar.
#
# Explicación:
# El programa usa el operador módulo (%). 
# Si el número módulo 2 es igual a 0, entonces el número es par;
# de lo contrario, es impar.
# -------------------------------------------------------------

n = int(input("Ingresa un número entero: "))

if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
