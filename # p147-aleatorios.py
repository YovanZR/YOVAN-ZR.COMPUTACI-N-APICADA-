import random
from typing import List

def generar_numeros_aleatorios(n:int,mini:int,maxi:int)->List[int]:
    return [random.randint(mini,maxi) for _ in range(n)]

def sumar_listas(a:List[int],b:List[int])->List[int]:
    return [x+y for x,y in zip(a,b)]

l1=generar_numeros_aleatorios(5,1,10)
l2=generar_numeros_aleatorios(5,50,100)
l3=sumar_listas(l1,l2)
print(l1,l2,l3)
