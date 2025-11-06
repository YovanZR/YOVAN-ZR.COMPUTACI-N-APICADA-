# p109-conversion-divisas.py
# Conversor de divisas a pesos mexicanos (MXN) usando diccionarios

print('\033[H\033[J')
print('Conversor de monedas a pesos mexicanos (MXN)\n')

conversiones = {
    'USD': 20.50,
    'EUR': 22.30,
    'GBP': 25.80,
    'JPY': 0.19,
    'CAD': 16.20
}

print('Opciones de monedas:')
for moneda in conversiones:
    print(f'- {moneda}')

# Elegir moneda
while True:
    moneda = input('\nIngrese la moneda a convertir: ').upper().strip()
    if moneda in conversiones:
        break
    print('Moneda no válida. Intente de nuevo.')

# Cantidad
while True:
    try:
        cantidad = float(input(f'Ingrese la cantidad en {moneda}: '))
        if cantidad <= 0:
            print('La cantidad debe ser positiva.')
            continue
        break
    except ValueError:
        print('Entrada no válida. Ingrese un número (ej. 150.50).')

resultado = cantidad * conversiones[moneda]
print(f'{cantidad:,.2f} {moneda} son {resultado:,.2f} MXN')
