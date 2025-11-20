from typing import List, Tuple

def separar_pares_impares(lista: List[int])->Tuple[List[int],List[int]]:
    pares=[]
    imp=[]
    for n in lista:
        if n%2==0: pares.append(n)
        else: imp.append(n)
    return pares, imp

nums=[1,2,3,4,5,6,7,8,9,10]
p,i=separar_pares_impares(nums)
print("Pares:",p)
print("Impares:",i)
