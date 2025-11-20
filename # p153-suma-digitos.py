# p153-suma-digitos.py
# Procesa una lista de números para obtener la suma de sus dígitos.

from typing import List

def leer_lista_enteros() -> List[int]:
    """Lee una línea de números separados por espacio y regresa una lista de enteros."""
    linea = input("Dame los números (separados por espacio): ")
    partes = linea.split()
    numeros: List[int] = []
    for p in partes:
        numeros.append(int(p))
    return numeros

def suma_digitos(numero: int) -> int:
    """Regresa la suma de los dígitos de un número entero."""
    numero = abs(numero)
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def procesa_lista(lista: List[int]) -> List[int]:
    """Regresa una nueva lista con la suma de dígitos de cada número de la lista original."""
    resultado: List[int] = []
    for n in lista:
        resultado.append(suma_digitos(n))
    return resultado

def main() -> None:
    numeros = leer_lista_enteros()
    lista_sumas = procesa_lista(numeros)
    print(f"La lista de números original : {numeros}")
    print(f"La lista con las suma de dígitos de los números: {lista_sumas}")

if __name__ == "__main__":
    main()
