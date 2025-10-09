# p058-impares-ascendente.py
# Imprimir números impares desde 1 hasta n y calcular su suma

while True:
    print("\n--- Impares Ascendentes ---")
    n = int(input("Introduce un número límite: "))
    c = 1
    suma = 0
    print("Números impares:", end=" ")
    while c <= n:
        if c % 2 != 0:
            print(c, end=", ")
            suma += c
        c += 1
    print(f"\nLa suma de los impares es: {suma}")

    if input("¿Desea continuar (S/N)? ").upper() == "N":
        break
