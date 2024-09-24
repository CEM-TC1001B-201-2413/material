opcion = int(input("""Menú de opciones:
1) Sopa
2) Guisado
3) Postre
0) Salir
Ingresa la opción que deseas: """))
match opcion:
    case 1:
        print("Se te sirvió sopa de pasta.")
    case 2:
        print("Se te sirvió picadillo y albóndigas.")
    case 3:
        print("Se te sirvió cheesecake de Costco.")
    case 0:
        print("Hasta pronto.")
    case _: # Caso por defecto/default
        print("Ingrese un valor entre 0 y 3")