# p021-distancia-entre-puntos.py
# Calcular la distancia entre dos puntos (x1, y1) y (x2, y2)

import math

print("=" * 50)
print(" DISTANCIA ENTRE DOS PUNTOS ")
print("=" * 50)

x1 = float(input("Coordenada x1: "))
y1 = float(input("Coordenada y1: "))
x2 = float(input("Coordenada x2: "))
y2 = float(input("Coordenada y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("-" * 50)
print(f"Punto 1 = ({x1}, {y1})")
print(f"Punto 2 = ({x2}, {y2})")
print(f"Distancia = {distancia:.4f}")
print("=" * 50)
