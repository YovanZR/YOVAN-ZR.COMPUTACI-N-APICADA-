# p151-medidas-longitud.py
# Conversor de unidades de longitud:
# 1) Pulgadas a centímetros
# 2) Metros a pies

def pulgadas_a_centimetros(pulgadas: float) -> float:
    """Convierte pulgadas a centímetros."""
    return pulgadas * 2.54

def metros_a_pies(metros: float) -> float:
    """Convierte metros a pies."""
    return metros * 3.281

def main() -> None:
    print("*** Conversor de Unidades ***")
    print("1. Pulgadas a Centímetros")
    print("2. Metros a Pies")
    print("3. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        pulgadas = float(input("Introduce la cantidad en pulgadas: "))
        cm = pulgadas_a_centimetros(pulgadas)
        print(f"{pulgadas:.1f} pulgadas equivalen a {cm:.1f} centímetros.")
    elif opcion == "2":
        metros = float(input("Introduce la cantidad en metros: "))
        pies = metros_a_pies(metros)
        print(f"{metros:.2f} metros equivalen a {pies:.2f} pies.")
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Debes elegir 1, 2 o 3.")

if __name__ == "__main__":
    main()
