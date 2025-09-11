# p018-area-volumen-cilindro.py
# Calcular el área lateral, área total y volumen de un cilindro

import math

print("=" * 50)
print(" ÁREA Y VOLUMEN DE UN CILINDRO ")
print("=" * 50)

r = float(input("Radio (r): "))
h = float(input("Altura (h): "))

area_lateral = 2 * math.pi * r * h
area_total = 2 * math.pi * r * (h + r)
volumen = math.pi * r**2 * h

print("-" * 50)
print(f"Radio = {r}, Altura = {h}")
print(f"Área lateral = {area_lateral:.4f}")
print(f"Área total   = {area_total:.4f}")
print(f"Volumen      = {volumen:.4f}")
print("=" * 50)
