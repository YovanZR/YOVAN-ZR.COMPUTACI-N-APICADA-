def suma_digitos(n:int)->int:
    s=0
    while n!=0:
        s+=n%10
        n//=10
    return s

n=int(input('Número: '))
print(suma_digitos(n))
