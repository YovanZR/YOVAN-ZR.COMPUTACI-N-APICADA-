# Verificar si un numero es positivo, negativo o cero (versión if else )

print('Verificar si un numero es positivo, negativo o cero')
numero = int(input('Dame un numero entero: '))

if numero > 0:
    print('El numero es POSITIVO ')
else:
    if numero < 0:
        print('El numero es NEGATIVO ')
    else:
        print('El numero es CERO ')

print('\nAqui ya terminamos de tomar decisiones')
