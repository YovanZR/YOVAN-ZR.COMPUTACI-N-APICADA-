# p047-conteo-descendente-v2.py
# Imprime los números de n a 1, en decrementos de m, usando un ciclo while

print("Iniciando cuenta regresiva...")
n = int(input("¿Desde dónde? (n): "))
m = int(input("¿De cuánto en cuánto? (m > 0): "))

if m <= 0:
    print("Error: el paso m debe ser mayor que 0.")
else:
    c = n
    while c >= 1:
        print(f"{c}", end=" ")
        c -= m
    print("\n¡Despegue!")
