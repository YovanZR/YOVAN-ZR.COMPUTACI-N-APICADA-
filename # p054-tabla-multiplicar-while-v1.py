# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla de multiplicar de t hasta el múltiplo n.

while True:
    print('\033[H\033[J', end='')
    print("Tabla de Multiplicar (una tabla)")
    print("-" * 35)

    # Captura y validación
    while True:
        try:
            t = int(input("¿Qué tabla quieres (t > 0)? "))
            n = int(input("¿Hasta dónde (n > 0)? "))
            if t > 0 and n > 0:
                break
            print("Error: t y n deben ser enteros > 0.")
        except ValueError:
            print("Error: ingresa enteros válidos.")

    # Impresión con while
    c = 1
    while c <= n:
        print(f"{t} x {c} = {t * c}")
        c += 1

    if input("¿Deseas otra tabla (S/N)? ").strip().upper() == 'N':
        print("\nGracias por utilizar este programa...")
        break
