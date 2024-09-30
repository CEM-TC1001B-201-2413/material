alumnos = ["Damián", "Ernesto", "Diego", "Naomi", "Fernanda"]
nombre = input("Indica el nombre del alumno a buscar: ")
encontrado = False
for alumno in alumnos:
    if nombre == alumno:
        encontrado = True
if encontrado:
    print(f"El alumno {nombre} está en la lista.")
else:
    print(f"El alumno {nombre} no está en la lista.")

# -------------------------------------

# break -> Detiene por completo el ciclo
# continue -> Detiene la repetición actual y pasa a la siguiente
# else -> Se ejecuta si el ciclo no se detuvo con un break
for alumno in alumnos:
    if nombre == alumno:
        print(f"El alumno {nombre} está en la lista.")
        break
else:
    print(f"El alumno {nombre} no está en la lista.")