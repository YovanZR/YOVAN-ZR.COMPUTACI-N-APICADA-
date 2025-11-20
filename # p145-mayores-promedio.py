from typing import List

def promedio_lista(lista: List[float])->float:
    if not lista: return 0.0
    return sum(lista)/len(lista)

def mayores_al_promedio(lista: List[float])->List[float]:
    prom=promedio_lista(lista)
    return [n for n in lista if n>prom]

nums=[1.5,2.3,3.7,4.0,5.5]
print("Mayores al promedio:", mayores_al_promedio(nums))
