# p072-suma-pares-impares.py
while True:
    n = int(input('Dame el valor final ? '))
    sp = si = 0
    cp = ci = ""
    for i in range(1, n+1):
        if i % 2 == 0:
            cp += " " + str(i)
            sp += i
        else:
            ci += " " + str(i)
            si += i
    print(f'Los pares : {cp} = {sp}')
    print(f'Los impares : {ci} = {si}')
    if input('Deseas continuar (S/N)? ').upper() == 'N':
        break
