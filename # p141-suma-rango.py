def suma_rango(i:int,f:int)->int:
    return sum(range(i,f+1))

i=int(input('Inicio: '))
f=int(input('Fin: '))
print(suma_rango(i,f))
