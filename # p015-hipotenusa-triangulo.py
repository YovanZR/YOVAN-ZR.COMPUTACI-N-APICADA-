# p015-hipotenusa-triangulo.py
# Calcular la hipotenusa de un triángulo rectángulo dados sus catetos

import math

print("=" * 50)
print(" HIPOTENUSA DE UN TRIÁNGULO RECTÁNGULO ")
print("=" * 50)

a = float(input("Longitud del lado 1 (cateto a): "))
b = float(input("Longitud del lado 2 (cateto b): "))

hipotenusa = math.sqrt(a**2 + b**2)

print("-" * 50)
print(f"Lados: a = {a}, b = {b}")
print(f"Hipotenusa = {hipotenusa:.4f}")
print("=" * 50)
