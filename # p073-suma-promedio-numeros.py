# p073-suma-promedio-numeros.py
while True:
    cuantos = int(input('Cuantos números deseas procesar ? '))
    suma = 0
    cadnum = ""
    for i in range(1, cuantos+1):
        n = int(input(f'Número[{i}] = '))
        suma += n
        cadnum += ' ' + str(n)
    print(f'Los números que introdujiste fueron: {cadnum}')
    print(f'La suma es {suma}, el promedio es {suma / cuantos}')
    if input('Deseas continuar (S/N)? ').upper() == 'N':
        break
