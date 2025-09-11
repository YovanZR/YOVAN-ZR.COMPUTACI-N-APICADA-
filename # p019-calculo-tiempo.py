# p019-calculo-tiempo.py
# Convertir horas en días, minutos y segundos

print("=" * 50)
print(" CÁLCULO DE TIEMPO ")
print("=" * 50)

horas = int(input("Cantidad de horas (entero): "))

dias = horas / 24
minutos = horas * 60
segundos = minutos * 60

print("-" * 50)
print(f"Horas: {horas}")
print(f"Días: {dias:.4f}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")
print("=" * 50)
