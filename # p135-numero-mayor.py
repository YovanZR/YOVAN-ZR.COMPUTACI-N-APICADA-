def numero_mayor(n1: int, n2: int, n3: int) -> int:
    mayor = n1
    if n2 > mayor: mayor = n2
    if n3 > mayor: mayor = n3
    return mayor

print('Dame 3 números:')
a=int(input()); b=int(input()); c=int(input())
print(f'El mayor es {numero_mayor(a,b,c)}')
