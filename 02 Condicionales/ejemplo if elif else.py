calificacion = float(input("Ingresa tu calificación: "))
if calificacion > 90:
    print("A")
if calificacion > 80 and calificacion <= 90:
    print("B")
if calificacion > 70 and calificacion <= 80:
    print("C")
if calificacion > 60 and calificacion <= 70:
    print("D")
if calificacion <= 60:
    print("F")
    
# -------------------------

if calificacion > 90:
    print("A")
else:
    if calificacion > 80:
        print("B")
    else:
        if calificacion > 70:
            print("C")
        else:
            if calificacion > 60:
                print("D")
            else:
                print("F")
                    
# -------------------------

if calificacion > 90:
    print("A")
elif calificacion > 80:
    print("B")
elif calificacion > 70:
    print("C")
elif calificacion > 60:
    print("D")
else: # Caso por defecto/default
    print("F")

                