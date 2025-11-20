# p149-numero-menor.py
# Pide 3 números enteros al usuario mediante una función y devuelve el menor de ellos.

def numero_menor() -> int:
    """Pide tres números enteros al usuario y regresa el menor de ellos."""
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    n3 = int(input("Introduce el tercer número: "))

    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor


def main() -> None:
    menor = numero_menor()
    print(f"El número menor es: {menor}")


if __name__ == "__main__":
    main()
