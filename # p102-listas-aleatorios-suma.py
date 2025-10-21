# Generar 2 listas aleatorias y sumar solo si ambos son impares
import random

print('\033[H\033[J')

lista_a = [random.randint(1, 20) for _ in range(10)]
lista_b = [random.randint(1, 20) for _ in range(10)]

lista_c = []
for i in range(10):
    if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0:
        lista_c.append(lista_a[i] + lista_b[i])
    else:
        lista_c.append(0)

print("--- Listas Generadas ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print("\n--- Resultados ---")
print(f"Lista C: {lista_c}")
