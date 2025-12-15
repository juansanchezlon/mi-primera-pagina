# mini_turtle/drawer_logic.py

# 1. Variable de estado global
posicion_x = 0

def adelante():
    """Mueve la 'tortuga' un paso a la derecha."""
    global posicion_x
    posicion_x += 1
    print(f"Adelante! Nueva posicion_x: {posicion_x}")

def abajo():
    """Simula dibujar una línea hacia abajo (para la escalera)."""
    # Esta función no modifica posicion_x, solo imprime
    print(f"Bajando desde posicion_x: {posicion_x}")

# 2. Nueva función para resetear el estado
def reiniciar():
    """Resetea la posicion_x a 0."""
    global posicion_x
    posicion_x = 0
    print("--- Posición Reiniciada ---")