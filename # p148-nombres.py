from typing import List

def une_procesa(a:List[str],b:List[str])->List[str]:
    un=a+b
    inv=un[::-1]
    return [n.upper() for n in inv]

def entrda()->List[str]:
    datos=[]
    print("Introduce nombres (vacío para terminar)")
    while True:
        n=input("Nombre: ")
        if n=="": break
        datos.append(n)
    return datos

n1=["Ana","Luis","Carlos","Marta","Sofía"]
n2=entrda()
print(une_procesa(n1,n2))
