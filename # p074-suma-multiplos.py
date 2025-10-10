# p074-suma-multiplos.py
while True:
    n = int(input('Hasta donde ? '))
    m = int(input('Que múltiplos quieres ? '))
    cm = sm = 0
    for i in range(1, n+1):
        if i % m == 0:
            print(i, end=' ')
            sm += i
            cm += 1
    print(f'\nFueron {cm} múltiplos, suman {sm}')
    if input('Deseas continuar (S/N)? ').upper() == 'N':
        break
