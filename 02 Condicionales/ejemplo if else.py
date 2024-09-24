edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Ya eres mayor de edad.")
else:
    faltantes = 18 - edad
    print(f"Te faltan {faltantes} años para poder votar.")
print("Terminó nuestro bloque condicional...")