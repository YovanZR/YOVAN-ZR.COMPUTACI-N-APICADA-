# p155-estadisticas-basicas.py
# Calcula estadísticas básicas (poblacionales) de una lista de números.

from typing import List
import math

def leer_lista_enteros() -> List[int]:
    """Lee una línea de números separados por espacio y regresa una lista de enteros."""
    linea = input("Dame números (separados por espacio): ")
    partes = linea.split()
    numeros: List[int] = []
    for p in partes:
        numeros.append(int(p))
    return numeros

def media(lista: List[int]) -> float:
    return sum(lista) / len(lista)

def mayor(lista: List[int]) -> int:
    maximo = lista[0]
    for n in lista:
        if n > maximo:
            maximo = n
    return maximo

def menor(lista: List[int]) -> int:
    minimo = lista[0]
    for n in lista:
        if n < minimo:
            minimo = n
    return minimo

def varianza_poblacional(lista: List[int]) -> float:
    """Calcula la varianza poblacional de una lista de números."""
    mu = media(lista)
    suma_cuadrados = 0.0
    for x in lista:
        suma_cuadrados += (x - mu) ** 2
    return suma_cuadrados / len(lista)

def desviacion_estandar_poblacional(lista: List[int]) -> float:
    """Calcula la desviación estándar poblacional de una lista de números."""
    return math.sqrt(varianza_poblacional(lista))

def main() -> None:
    numeros = leer_lista_enteros()
    if not numeros:
        print("No se capturaron datos.")
        return

    mu = media(numeros)
    maximo = mayor(numeros)
    minimo = menor(numeros)
    var = varianza_poblacional(numeros)
    desv = desviacion_estandar_poblacional(numeros)

    print(f"Lista de números: {numeros}")
    print("Estadísticas:")
    print(f"Media             : {mu:.3f}")
    print(f"Mayor             : {maximo}")
    print(f"Menor             : {minimo}")
    print(f"Varianza          : {var:.3f}")
    print(f"Desviación estándar: {desv:.3f}")

if __name__ == "__main__":
    main()
