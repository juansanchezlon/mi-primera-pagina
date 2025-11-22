# Tarea 2 - Ejercicios Unidad 1

En esta página presento los ejercicios de la Unidad 1 con su enunciado, la solución en Python y explicaciones dentro del propio código usando comentarios.

---

## ✏️ Ejercicio 1

**Enunciado:**  
Escribe un programa en Python que pida al usuario un número y muestre si es positivo, negativo o cero.

**Código en Python (con explicación dentro del código):**

```python
# -------------------------------------------------------------
# EJERCICIO 1 - UNIDAD 1
#
# Enunciado:
# Escribe un programa en Python que pida al usuario un número 
# y muestre si es positivo, negativo o cero.
#
# Explicación:
# El programa pide un número al usuario y usa condicionales
# if, elif y else para determinar si el número es mayor que cero
# (positivo), menor que cero (negativo) o igual a cero.
# -------------------------------------------------------------

numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
