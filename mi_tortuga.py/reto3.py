# Reto 3 - Girar y dibujar una L
print("Simulando una tortuga que dibuja una L...")
pasos1 = int(input("¿Cuántos pasos hacia adelante? "))
pasos2 = int(input("¿Cuántos pasos hacia abajo? "))


print("-" * pasos1 + ">")
for i in range(pasos2):
  print(" " * pasos1 + "|")
print(" " * pasos1 + "V")