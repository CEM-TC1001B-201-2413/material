# for i in range(5)
i = 0 # inicio
while i < 5: # Condición de paro o condición de salida
    print(f"El valor de i es: {i}")
    # i = i + 1
    i += 1 # paso

# -------------

texto = "Hola mundo"
print(len(texto))
print(texto[0])

i = 0
while i < len(texto):
    print(f"El valor de texto[{i}] = {texto[i]}")
    i += 1
    
print("------------------")

centinela = 1
while centinela == 1:
    print("Haciendo cosas...")
    centinela = int(input("¿Desea continuar repitiendo? 1)Sí, 2)No: "))
print("Terminando ciclo...")
