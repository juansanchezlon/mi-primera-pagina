pos_x = 0


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