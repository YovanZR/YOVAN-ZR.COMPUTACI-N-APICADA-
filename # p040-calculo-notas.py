# p040-calculo-notas.py
# Problema: Calcular promedio de 5 calificaciones

suma = 0
for i in range(1, 6):
    cal = float(input(f"Ingrese la calificación {i}: "))
    suma += cal

promedio = suma / 5

print(f"Tu promedio es {promedio:.2f}.")

if promedio < 6:
    print("Quedas reprobado")
elif promedio < 7:
    print("Pasas de panzazo")
elif promedio < 8:
    print("Muy bien, puedes mejorar")
elif promedio < 9:
    print("Excelente, sigue así")
else:
    print("Perfecto, tu esfuerzo valió la pena")
