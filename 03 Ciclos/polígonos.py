import turtle
# Dibujar un polígono regular cualquiera indicando el tamaño
# de su lado y el número de lados
tamaño = int(input("Ingresa el tamaño del lado: "))
numero_lados = int(input("Ingresa el número de lados: "))
for i in range(numero_lados):
    turtle.forward(tamaño)
    turtle.right(360/numero_lados)
turtle.mainloop()