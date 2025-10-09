# p059-pares-descendente.py
# Imprimir números pares desde 100 hasta n y calcular su suma

while True:
    print("\n--- Pares Descendentes ---")
    n = int(input("Introduce un número límite (menor a 100): "))
    c = 100
    suma = 0
    print("Números pares:", end=" ")
    while c >= n:
        if c % 2 == 0:
            print(c, end=", ")
            suma += c
        c -= 2
    print(f"\nLa suma de los pares es: {suma}")

    if input("¿Desea continuar (S/N)? ").upper() == "N":
        break
