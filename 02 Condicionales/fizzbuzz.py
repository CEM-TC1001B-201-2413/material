# FizzBuzz
# Ingrese un número entero
# Si el número es divisible entre 3 -> Fizz
# Si el número es divisible entre 5 -> Buzz
# Si el número es divisible entre 3 y 5 -> FizzBuzz
# Si el número no es divisible ni entre 3 ni entre 5 -> número
numero = int(input("Ingrese un número entero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print(numero)
    
    