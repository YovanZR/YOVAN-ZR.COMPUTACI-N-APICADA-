# p060-promedio-suma.py
# Leer números hasta que el usuario ingrese 0 y calcular promedio y suma

while True:
    print("\n--- Promedio y Suma ---")
    suma = 0
    cuenta = 0
    while True:
        num = int(input("Introduce un número (0 para terminar): "))
        if num == 0:
            break
        suma += num
        cuenta += 1

    print("-" * 20)
    print(f"Se introdujeron {cuenta} números.")
    print(f"La suma es: {suma}")
    if cuenta > 0:
        print(f"El promedio es: {suma / cuenta:.2f}")
    else:
        print("No se introdujeron números válidos.")

    if input("¿Desea continuar (S/N)? ").upper() == "N":
        break
