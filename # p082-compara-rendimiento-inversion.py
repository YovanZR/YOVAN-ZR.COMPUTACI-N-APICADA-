# p082-compara-rendimiento-inversion.py
# Comparar crecimiento de dos fondos de inversión

print("--- Fondo de Inversión A ---")
monto_a = float(input("Monto inicial: "))
tasa_a = float(input("Tasa de interés anual (%): "))

print("--- Fondo de Inversión B ---")
monto_b = float(input("Monto inicial: "))
tasa_b = float(input("Tasa de interés anual (%): "))

anios = int(input("Años a proyectar: "))

print("--- Comparación de Rendimientos Anuales ---")
print("Año | Fondo A | Fondo B")
print("-------------------------------------------")

anio = 1
while anio <= anios:
    monto_a = monto_a * (1 + tasa_a / 100.0)
    monto_b = monto_b * (1 + tasa_b / 100.0)
    print(f"{anio} | $ {monto_a:0.2f} | $ {monto_b:0.2f}")
    anio = anio + 1

print()
if monto_a > monto_b:
    print(f"Resultado final: El Fondo A (${'{:.2f}'.format(monto_a)}) superó al Fondo B (${'{:.2f}'.format(monto_b)}).")
elif monto_b > monto_a:
    print(f"Resultado final: El Fondo B (${'{:.2f}'.format(monto_b)}) superó al Fondo A (${'{:.2f}'.format(monto_a)}).")
else:
    print(f"Resultado final: Ambos fondos terminaron iguales con $ {'{:.2f}'.format(monto_a)}.")
