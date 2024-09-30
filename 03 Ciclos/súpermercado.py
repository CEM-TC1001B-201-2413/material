# Supermercado
# Pedir precios hasta que llegue un valor negativo
# Mostrar el total a pagar
precio = 0
total = 0
while precio >= 0:
    total += precio
    precio = float(input("Ingrese el precio del producto: "))
print(f"El total a pagar es: ${total:,.2f}")