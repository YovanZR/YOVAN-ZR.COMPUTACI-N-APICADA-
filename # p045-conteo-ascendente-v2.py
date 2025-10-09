# p045-conteo-ascendente-v2.py
# Imprime los números de 1 a n, en incrementos de m, usando un ciclo while

print("Iniciando secuencia de conteo ascendente...")
n = int(input("¿Hasta dónde? (n): "))
m = int(input("¿De cuánto en cuánto? (m > 0): "))

if m <= 0:
    print("Error: el paso m debe ser mayor que 0.")
else:
    c = 1
    while c <= n:
        print(f"{c}", end=" ")
        c += m
    print("\n¡Secuencia completada!")
