def dibuja_cuadro(renglones: int, columnas: int, caracter: str) -> None:
    for r in range(renglones):
        for c in range(columnas):
            print(caracter, end='')
        print('')

r = int(input('Renglones: '))
c = int(input('Columnas: '))
ch = input('Caracter: ')
dibuja_cuadro(r,c,ch)
