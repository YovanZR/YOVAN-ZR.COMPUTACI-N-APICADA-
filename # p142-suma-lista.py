from typing import List

def suma_lista(lista: List[float]) -> float:
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros=[1.5,2.3,3.7,4.0]
print("La suma de la lista es:", suma_lista(numeros))
