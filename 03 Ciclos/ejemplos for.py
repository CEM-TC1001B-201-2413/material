
# range(inicio) -> Genera una secuencia numérica que inicia en 0,
# avanza de uno en uno y se detiene antes de inicio
print("range(5)")
for i in range(5): # i = 0, 1, 2, 3, 4
    print(f"El valor de i es: {i}")

print("----------------------------")
# range(inicio, final) -> Genera una secuencia numérica que inicia en
# inicio, avanza de uno en uno y se detiene antes de final
print("range(5,10)")
for i in range(5,10): # i = 5, 6, 7, 8, 9
    print(f"El valor de i es: {i}")
    
print("----------------------------")

# range(inicio, final, paso) -> Genera una secuencia numérica que inicia
# en inicio, avanza de paso en paso y se detiene antes de final
print("range(5,15,3)")
for i in range(5,15,3): # i = 5, 8, 11, 14
    print(f"El calor de i es: {i}")
    
print("----------------------------")

for i in range(5,10,-1):
    print(f"El valor de i es: {i}")

print("----------------------------")

texto = "Hola mundo"
for i in texto: # i = "H", "o", "l", "a", " ", "m", "u", "n", "d", "o"
    print(f"El valor de i es: {i}")
    
print("----------------------------")

lista = [1, True, 5.7, [5,8,1], False, "Hola"]
for i in lista: # i = 1, True, 5.7, [5,8,1], False, "Hola"
    print(f"El valor de i es: {i}")