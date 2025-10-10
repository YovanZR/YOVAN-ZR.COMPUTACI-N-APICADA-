# p076-tablas-todas.py
# Imprime las tablas de multiplicar de 1 a n, hasta m

print('\033[H\033[J')

n = int(input("¿Hasta qué tabla de multiplicar deseas generar? "))
m = int(input("¿Hasta qué número deseas multiplicar cada tabla? "))

print("\n--- Generando Tablas de Multiplicar ---")

for i in range(1, n + 1):           # Bucle exterior -> número de la tabla
    print(f"\n--- Tabla del {i} ---")
    for j in range(1, m + 1):       # Bucle interior -> multiplicadores
        print(f"{i} x {j} = {i * j}")
