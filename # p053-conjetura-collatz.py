# p053-conjetura-collatz.py
# Calcula y muestra la secuencia de la conjetura de Collatz para un entero positivo.

while True:
    print('\033[H\033[J', end='')
    print("Conjetura de Collatz")
    print("-" * 30)

    # Captura y validación
    while True:
        try:
            num = int(input("Ingresa un número entero positivo: "))
            if num > 0:
                break
            print("Error: el número debe ser mayor que 0.")
        except ValueError:
            print("Error: ingresa un entero válido.")

    # Secuencia
    print("\nSecuencia:")
    print(num, end=" ")
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        print(num, end=" ")
    print("\n\n¡Secuencia terminada!")

    if input("¿Probar otro número (S/N)? ").strip().upper() == 'N':
        print("Gracias por usar este programa. Vuelve pronto.")
        break
