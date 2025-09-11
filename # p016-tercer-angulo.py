# p016-tercer-angulo.py
# Calcular el tercer ángulo de un triángulo

print("=" * 50)
print(" TERCER ÁNGULO DE UN TRIÁNGULO ")
print("=" * 50)

ang1 = float(input("Ángulo 1 (en grados): "))
ang2 = float(input("Ángulo 2 (en grados): "))

ang3 = 180 - (ang1 + ang2)

print("-" * 50)
print(f"Ángulos dados: {ang1}°, {ang2}°")
print(f"Tercer ángulo = {ang3:.2f}°")
print("=" * 50)
