# Sumatoria de 1 hasta n
# Resultado = 1+2+3+4+5+...+n
# n = 5 -> 15

n = int(input("Ingresa el valor de n: "))
resultado = 0
for i in range(1,n+1):
    resultado = resultado + i
print(f"El resultado de la suma de 1 hasta {n} es: {resultado}")
# i = 1
# resultado = 0 + 1 = 1
# ---------
# i = 2
# resultado = 1 + 2 = 3
# ---------
# i = 3
# resultado = 3 + 3 = 6
# ---------
# i = 4
# resultado = 6 + 4 = 10
# ---------
# i = 5
# resultado = 10 + 5 = 15