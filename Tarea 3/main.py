#             ^^^^^^^^^^
# Asegúrate de que el nombre del paquete coincida con el nombre de la carpeta (mini_turtle)
# Estado Global: Posición actual de la "tortuga" en el eje X
from mini_turtle import adelante, abajo, reiniciar

posicion_x = 0

def adelante(pasos=1):
    """Mueve la tortuga hacia adelante e imprime la acción."""
    global posicion_x
    posicion_x += pasos
    print(f"La tortuga avanzó {pasos} pasos. Nueva posición: {posicion_x}")

def abajo():
    """Mueve la tortuga hacia abajo (simplemente imprime la acción, no afecta a posicion_x)."""
    print("La tortuga se movió hacia abajo (cambio de nivel).")

# main.py

# Importa las funciones directamente desde el paquete mini_turtle
from mini_turtle import adelante, abajo, reiniciar

print("--- Dibujando la Escalera ---")
# Dibuja una "escalera"
adelante()
abajo()
adelante()
abajo()
adelante()
abajo()

print("\n--- Reiniciando para dibujar algo nuevo ---")
# Usa la nueva función de reinicio
reiniciar()

print("\n--- Dibujando algo nuevo (Linea en 0) ---")
# Dibuja una línea en la posición 0
abajo()
adelante()
abajo()