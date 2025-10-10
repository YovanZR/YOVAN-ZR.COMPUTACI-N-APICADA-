# p071-arriba-abajo.py
while True:
    print('Imprimir numeros usando ciclo for - Arriba o Abajo')
    print('[1] Imprimir de 1 a n ')
    print('[2] Imprimir de n a 1 ')
    op = int(input('Que eliges ? '))
    if op == 1:
        n = int(input('Hasta donde ? '))
        for x in range(1, n+1):
            print(x, end=' ')
    elif op == 2:
        n = int(input('Desde donde ? '))
        for x in range(n, 0, -1):
            print(x, end=' ')
    else:
        print('Opción no válida')
    if input('\n¿Deseas continuar (S/N)? ').upper() == 'N':
        break
