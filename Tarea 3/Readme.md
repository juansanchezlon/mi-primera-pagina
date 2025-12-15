# 🐢 `mini-turtle`

## Introducción

`mini-turtle` es un paquete de Python desarrollado como un ejercicio de **modularidad**. Su objetivo principal es demostrar la **separación de la lógica de estado (en `drawer_logic.py`) de la interfaz pública (en `__init__.py`)**.

El paquete implementa un sistema simple de movimiento horizontal (`posicion_x`).

---

## 🚀 Estructura del Proyecto

La modularidad se logra mediante la siguiente estructura de archivos:
#mini_turtle_task/ ├── mini_turtle/ <-- Directorio del Paquete │ ├── init.py <-- Interfaz Pública: Expone las funciones. │ └── drawer_logic.py <-- Lógica: Contiene el estado (posicion_x) y la implementación. └── main.py <-- Script de Prueba del Usuario.

## 🛠️ Uso

El paquete está diseñado para ser importado con una interfaz limpia, permitiendo a los usuarios acceder a las funciones directamente:

```python
from mini_turtle import adelante, abajo, reiniciar

##🔑 Funciones Principales de mini-turtle

##Función,Descripción,Efecto en el Estado Global (posicion_x)
##adelante(),Mueve la tortuga un paso a la derecha.,Incrementa posicion_x en 1.
##abajo(),Simula un paso vertical (como dibujar).,Ninguno (solo imprime el valor actual de posicion_x).
##reiniciar(),Resetea la posición horizontal de la tortuga.,Establece posicion_x a 0.

##Prueba

# main.py

# Importa las funciones directamente desde el paquete mini_turtle
from mini_turtle import adelante, abajo, reiniciar

print("--- Dibujando la Escalera ---")
# Dibuja una "escalera"
adelante()  # x = 1
abajo()     # Bajando desde 1
adelante()  # x = 2
abajo()     # Bajando desde 2
adelante()  # x = 3
abajo()     # Bajando desde 3

print("\n--- Reiniciando para dibujar algo nuevo ---")
# Usa la nueva función de reinicio (x se vuelve 0)
reiniciar()

print("\n--- Dibujando algo nuevo (Linea en 0) ---")
# Dibuja una línea
abajo()     # Bajando desde 0
adelante()  # x = 1
abajo()     # Bajando desde 1

##Resultado de la ejecución

--- Dibujando la Escalera ---
Adelante! Nueva posicion_x: 1
Bajando desde posicion_x: 1
Adelante! Nueva posicion_x: 2
Bajando desde posicion_x: 2
Adelante! Nueva posicion_x: 3
Bajando desde posicion_x: 3

--- Reiniciando para dibujar algo nuevo ---
--- Posición Reiniciada ---

--- Dibujando algo nuevo (Linea en 0) ---
Bajando desde posicion_x: 0
Adelante! Nueva posicion_x: 1
Bajando desde posicion_x: 1