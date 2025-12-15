# mini_turtle/__init__.py

# 1. Importa todo lo que quieres exponer desde el módulo de lógica
from .drawer_logic import adelante, abajo, reiniciar

# 2. Define __all__ para especificar explícitamente qué funciones son la interfaz pública
# (Buena práctica para evitar que otras funciones se importen con 'from mini_turtle import *')
__all__ = [
    "adelante",
    "abajo",
    "reiniciar"
]