# p052-tabla-conversion.py
# Tabla de conversión de Pesos (MXN) a Dólares (USD) con tipo de cambio fijo.

TC = 20.71  # pesos por dólar

while True:
    print('\033[H\033[J', end='')  # Limpia pantalla (opcional)
    print("Tabla de Conversión Peso → Dólar")
    print(f"Tipo de cambio: {TC} pesos por 1 dólar")
    print("-" * 40)

    # Captura y validación de rango
    while True:
        try:
            pi = float(input("Valor inicial en pesos: "))
            pf = float(input("Valor final en pesos:   "))
            if (pi > 0 and pf > 0) and (pi <= pf):
                break
            print("Error: ambos deben ser > 0 y el inicial ≤ final.")
        except ValueError:
            print("Error: ingresa números válidos.")

    # Impresión de tabla (paso = 1 peso)
    c = pi
    print("\nPesos\t\tDólares")
    print("-" * 40)
    while c <= pf + 1e-9:
        print(f"{c:.2f}\t\t{(c/TC):.2f}")
        c += 1
    print("-" * 40)

    res = input("¿Deseas generar otra tabla (S/N)? ").strip().upper()
    if res == 'N':
        print("Gracias por usar el conversor. ¡Hasta luego!")
        break
