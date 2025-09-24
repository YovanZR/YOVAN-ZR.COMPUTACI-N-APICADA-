# Calcular fuerza, masa o aceleración según la elección del usuario.

print('--- Calculadora de la 2da Ley de Newton ---')
print('[1] Calcular la Fuerza (fuerza = masa * aceleración)')
print('[2] Calcular la Masa (masa = fuerza / aceleración)')
print('[3] Calcular la Aceleración (aceleración = fuerza / masa)')

opcion = int(input('Elige una opción (1, 2 o 3): '))

if opcion == 1:
    print('\n Calculando la Fuerza...')
    masa = float(input('Dame la masa: '))
    aceleracion = float(input('Dame la aceleración: '))
    fuerza = masa * aceleracion
    print(f' La fuerza es: {fuerza}')
elif opcion == 2:
    print('\n Calculando la Masa...')
    fuerza = float(input('Dame la fuerza: '))
    aceleracion = float(input('Dame la aceleración: '))
    if aceleracion == 0:
        print(' Error: la aceleración no puede ser 0.')
    else:
        masa = fuerza / aceleracion
        print(f' La masa es: {masa}')
elif opcion == 3:
    print('\n Calculando la Aceleración...')
    fuerza = float(input('Dame la fuerza: '))
    masa = float(input('Dame la masa: '))
    if masa == 0:
        print(' Error: la masa no puede ser 0.')
    else:
        aceleracion = fuerza / masa
        print(f' La aceleración es: {aceleracion}')
else:
    print('\n Opción inválida. Por favor, elige 1, 2 o 3.')
