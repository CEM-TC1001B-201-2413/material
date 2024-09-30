# Tabla de multiplicar
# Ingresar un número n
# Mostrar su tabla de multiplicar
# Si n = 3
# 1 x 3 = 3
# 2 x 3 = 6
# ...
# 10 x 3 = 30
n = int(input("Ingrese el valor de n: "))
for i in range(1,11):
    resultado = n * i
    print(f"{i} x {n} = {resultado}")