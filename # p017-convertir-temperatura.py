# p017-convertir-temperatura.py
# Convertir temperatura de °C a °F

print("=" * 50)
print(" CONVERSIÓN DE TEMPERATURA °C → °F ")
print("=" * 50)

c = float(input("Temperatura en °C: "))
f = (c * 9/5) + 32

print("-" * 50)
print(f"{c:.2f} °C equivalen a {f:.2f} °F")
print("=" * 50)
