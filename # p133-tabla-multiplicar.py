def tabla_multiplicar(tabla: int, limite: int) -> None:
    print(f'Tabla de multiplicar del {tabla} hasta {limite}:')
    for i in range(1, limite + 1):
        print(f'{tabla} x {i} = {tabla*i}')
    print('')

tabla = int(input('Ingrese la tabla: '))
limite = int(input('Ingrese el límite: '))
tabla_multiplicar(tabla, limite)
