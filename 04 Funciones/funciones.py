# Entradas -> Parámetros
# Salida -> Valor de retorno

# Sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")

# Con parámetros y sin valor de retorno
def suma2(x : float, y : float):
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")

# Con parámetros y con valor de retorno
def suma3(x : float, y : float) -> float:
    resultado = x + y
    return resultado

#suma1()
#print(resultado)
#suma2(10, 5)
#a = float(input("Ingresa x: "))
#b = float(input("Ingresa y: "))
#suma2(a, b)
#suma2("hola", "mundo")
res = suma3(4,5)
print(f"El resultado es: {res}")