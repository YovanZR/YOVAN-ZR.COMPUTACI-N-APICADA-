# p009-promedio-de-calificaciones.py
# Objetivo: Calcular el promedio de tres calificaciones ingresadas por el usuario.

print("=" * 50)
print(" PROMEDIO DE TRES CALIFICACIONES ")
print("=" * 50)

print("Dame 3 calificaciones separadas por espacios:")
cal1, cal2, cal3 = input().split()

# Convertir a enteros (o float si manejas decimales)
cal1, cal2, cal3 = float(cal1), float(cal2), float(cal3)

promedio = (cal1 + cal2 + cal3) / 3

print("-" * 50)
print(f"Las calificaciones son: {cal1}, {cal2}, {cal3}")
print(f"El promedio de las calificaciones es: {promedio:.2f}")
print("=" * 50)
