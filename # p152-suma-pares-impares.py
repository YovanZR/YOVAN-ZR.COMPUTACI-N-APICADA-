# p152-suma-pares-impares.py
# Suma números pares o impares en un rango, según lo indique el usuario.

def suma_en_rango(inicio: int, fin: int, tipo: str) -> int:
    """Suma los números pares ('P') o impares ('I') en el rango [inicio, fin]."""
    if inicio > fin:
        # Intercambia si vienen al revés
        inicio, fin = fin, inicio

    tipo = tipo.upper()
    suma = 0
    for numero in range(inicio, fin + 1):
        if tipo == "P" and numero % 2 == 0:
            suma += numero
        elif tipo == "I" and numero % 2 != 0:
            suma += numero
    return suma

def main() -> None:
    print("*** Suma en Rango ***")
    inicio = int(input("Introduce el número inicial: "))
    fin = int(input("Introduce el número final: "))
    tipo = input("¿Qué deseas sumar? (P)ares o (I)mpares: ").strip().upper()

    if tipo not in ("P", "I"):
        print("Opción inválida. Debes escribir 'P' o 'I'.")
        return

    resultado = suma_en_rango(inicio, fin, tipo)

    if tipo == "P":
        print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
    else:
        print(f"La suma de los números impares entre {inicio} y {fin} es: {resultado}")

if __name__ == "__main__":
    main()
