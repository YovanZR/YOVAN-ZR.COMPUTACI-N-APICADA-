# p063-numero-mayor.py
# Leer números hasta ingresar 0 y mostrar el mayor

while True:
    print("\n--- Número Mayor ---")
    mayor = None
    while True:
        num = int(input("Introduce un número (0 para terminar): "))
        if num == 0:
            break
        if mayor is None or num > mayor:
            mayor = num

    print("-" * 20)
    if mayor is None:
        print("No se introdujeron números válidos.")
    else:
        print(f"El número mayor fue: {mayor}")

    if input("¿Desea continuar (S/N)? ").upper() == "N":
        break
