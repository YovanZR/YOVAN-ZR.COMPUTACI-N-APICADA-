# Multiplicar elementos de dos listas de 5 elementos
print('\033[H\033[J')

print("Introduzca 5 números para la Lista A:")
lista_a = [int(input(f"A[{i}] = ")) for i in range(5)]

print("\nIntroduzca 5 números para la Lista B:")
lista_b = [int(input(f"B[{i}] = ")) for i in range(5)]

lista_c = [lista_a[i] * lista_b[i] for i in range(5)]

print("\n--- Resultados ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C (A * B): {lista_c}")
