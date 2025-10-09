# p055-tabla-multiplicar-while-v2.py
# Imprime todas las tablas desde 1 hasta n; cada una hasta el múltiplo m.

while True:
    print('\033[H\033[J', end='')
    print("Tablas de Multiplicar (1..n)")
    print("-" * 35)

    # Captura y validación
    while True:
        try:
            n = int(input("¿Hasta qué tabla (n > 0)? "))
            m = int(input("¿Hasta qué múltiplo (m > 0)? "))
            if n > 0 and m > 0:
                break
            print("Error: n y m deben ser enteros > 0.")
        except ValueError:
            print("Error: ingresa enteros válidos.")

    # Impresión con while anidados
    t = 1
    while t <= n:
        print(f"\nTabla del {t}")
        print("-" * 15)
        c = 1
        while c <= m:
            print(f"{t} x {c} = {t * c}")
            c += 1
        t += 1

    if input("\n¿Deseas generar otro conjunto (S/N)? ").strip().upper() == 'N':
        print("\nGracias por utilizar este programa...")
        break
