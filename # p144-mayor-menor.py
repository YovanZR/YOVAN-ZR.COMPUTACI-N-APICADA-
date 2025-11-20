from typing import List

def mayor(lista: List[float]) -> float:
    m=lista[0]
    for n in lista:
        if n>m: m=n
    return m

def menor(lista: List[float]) -> float:
    m=lista[0]
    for n in lista:
        if n<m: m=n
    return m

def captura_datos()->List[float]:
    datos=[]
    print("Ingresa números (fin para terminar)")
    while True:
        e=input("Número: ")
        if e.lower()=="fin":
            break
        try:
            datos.append(float(e))
        except:
            print("Inválido")
    return datos

nums=captura_datos()
if nums:
    print("Mayor:", mayor(nums))
    print("Menor:", menor(nums))
