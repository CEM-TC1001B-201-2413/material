udf1 = float(input("Ingresa la calificación de tu uf1: "))
udf2 = float(input("Ingresa la calificación de tu uf2: "))
udf3 = float(input("Ingresa la calificación de tu uf3: "))
udf4 = float(input("Ingresa la calificación de tu uf4: "))
udf5 = float(input("Ingresa la calificación de tu uf5: "))
udf6 = float(input("Ingresa la calificación de tu uf6: "))
udf7 = float(input("Ingresa la calificación de tu uf7: "))
promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7) / 7
print(f"El promedio de tu semestre fue: {promedio:,.2f}")
if promedio >= 95:
    print("Excelente semestre A+.")
elif promedio >= 85:
    print("Buen semestre.")
elif promedio >= 70:
    print("Pasaste, pero puedes mejorar.")
else:
    print("Reprobaste, suerte para la próxima.")