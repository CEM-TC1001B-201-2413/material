udf1 = float(input("Ingresa la calificación de tu uf1: "))
udf2 = float(input("Ingresa la calificación de tu uf2: "))
udf3 = float(input("Ingresa la calificación de tu uf3: "))
udf4 = float(input("Ingresa la calificación de tu uf4: "))
udf5 = float(input("Ingresa la calificación de tu uf5: "))
udf6 = float(input("Ingresa la calificación de tu uf6: "))
udf7 = float(input("Ingresa la calificación de tu uf7: "))
promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7) / 7
print("El promedio de tu semestre fue:", promedio)
print("El promedio de tu semestre fue: " + str(promedio))
print("El promedio de tu semestre fue: {0:,.2f}".format(promedio))
# La manera actual: f-strings
# : -> formato especial
# , -> separador de miles
# .2 -> redondear a 2 decimales
# f -> usar formato float en lugar de formato científico
print(f"El promedio de tu semestre fue: {promedio:,.2f}")