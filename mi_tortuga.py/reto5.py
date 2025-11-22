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



