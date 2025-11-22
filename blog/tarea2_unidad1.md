import turtle

t = turtle.Turtle()   # Crea una tortuga
t.forward(100)        # Avanza 100 unidades
turtle.done()         # Mantiene la ventana abierta




# Reto 1 - Tortuga simple

#Enunciado: Simula el movimiento de una tortuga hacia adelante usando únicamente texto.

print("Creando una tortuga simulada...")
pasos = int(input("¿Cuántos pasos debe avanzar? "))
print("La tortuga avanza... de a 1 paso.")
print("." * pasos)

#El programa pide un número de pasos y dibuja una línea de puntos representando el movimiento.

# Reto 2 - Tortuga bajando

#Simula el rastro de una tortuga moviéndose hacia abajo usando solo texto.

print("Creando tortuga que baja...")
pasos = int(input("¿Cuántos pasos baja la tortuga? "))
for i in range(pasos):
    print("|")
print("V")

#El programa imprime una columna (|) para cada paso y al final una (V) indicando la dirección hacia abajo.

# Reto 3 - Girar y dibujar una L

#Ahora la tortuga avanza y luego gira para dibujar una "L".

print("Simulando una tortuga que dibuja una L...")
pasos1 = int(input("¿Cuántos pasos hacia adelante? "))
pasos2 = int(input("¿Cuántos pasos hacia abajo? "))


print("-" * pasos1 + ">")
for i in range(pasos2):
  print(" " * pasos1 + "|")
print(" " * pasos1 + "V")

#Dibuja una línea horizontal y luego una línea vertical hacia abajo, formando una "L".

pos_x = 0

#Crea funciones adelante(n) y abajo(n) que dibujen los trazos.

def adelante(n):
    global pos_x
    print("-" * n + ">")
    pos_x += n


def abajo(n):
    global pos_x
    # El bucle y la impresión del palito vertical (|) están indentados
    for i in range(n):
        print(" " * pos_x + "|")
    # La impresión de la flecha hacia abajo (V) está al mismo nivel que el bucle
    print(" " * pos_x + "V")


# Ejemplo de uso
adelante(5)
abajo(3)

#Las funciones mantienen la posición horizontal acumulada para que los trazos se dibujen en el lugar correcto.

pos_x = 0

#Ahora se deben combinar ambos movimientos para dibujar varios escalones.

def adelante(n):
    global pos_x
    print("-" * n + ">")
    pos_x += n


def abajo(n):
    global pos_x
    for i in range(n):
        print(" " * pos_x + "|")
    print(" " * pos_x + "V")


# Ejemplo de escaleras (genera una escalera descendente)
adelante(5)
abajo(2)
adelante(5)
abajo(2)
adelante(5)
abajo(2)

#Cada escalón conserva la posición horizontal acumulada y dibuja correctamente tramo horizontal y vertical.
 
 #------------------------------------------------------------------------------------

## Referencias de IA
#Para transparencia en el uso de herramientas asistidas por IA:


### Referencias de IA
# **ChatGPT:** se utilizó una conversacion para generar explicaciones y el código de los retos .
##**Otras herramientas:** no se utilizaron.

