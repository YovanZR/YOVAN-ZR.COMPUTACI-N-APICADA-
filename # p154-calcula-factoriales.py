# p154-calcula-factoriales.py
# Calcula el factorial de cada número en una lista.

from typing import List

def leer_lista_enteros() -> List[int]:
    """Lee una línea de números separados por espacio y regresa una lista de enteros."""
    linea = input("Dame los números (separados por espacio): ")
    partes = linea.split()
    numeros: List[int] = []
    for p in partes:
        numeros.append(int(p))
    return numeros

def factorial(numero: int) -> int:
    """Calcula el factorial de un número entero no negativo."""
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

def lista_factoriales(lista: List[int]) -> List[int]:
    """Regresa una nueva lista con el factorial de cada número de la lista original."""
    resultado: List[int] = []
    for n in lista:
        resultado.append(factorial(n))
    return resultado

def main() -> None:
    numeros = leer_lista_enteros()
    factoriales = lista_factoriales(numeros)
    print(f"La lista de números originales: {numeros}")
    print(f"La lista con los factoriales: {factoriales}")

if __name__ == "__main__":
    main()
