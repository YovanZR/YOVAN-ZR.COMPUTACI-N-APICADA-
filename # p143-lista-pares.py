from typing import List

def lista_pares(lista: List[int]) -> List[int]:
    pares=[]
    for n in lista:
        if n%2==0:
            pares.append(n)
    return pares

nums=[1,2,3,4,5,6,7,8,9,10]
print(lista_pares(nums))
