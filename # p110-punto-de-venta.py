# p110-punto-de-venta.py
# Simulación de un punto de venta usando diccionarios

print('\033[H\033[J')
print('Simulación de un punto de venta usando diccionarios\n')

menu = {
    'taco': 18.50,
    'burrito': 45.00,
    'quesadilla': 35.00,
    'refresco': 20.00,
    'agua': 15.00
}

print("""--- Bienvenido a 'El Taco Feroz' ---
Este es nuestro menú:""")
for item, precio in menu.items():
    print(f' - {item:<12} : ${precio:,.2f}')

carrito = {}
while True:
    prod = input("\n¿Qué desea ordenar? (escriba 'fin' para terminar): ").lower().strip()
    if prod == 'fin':
        break
    if prod not in menu:
        print('Error: Ese producto no está en el menú. Intente de nuevo.')
        continue
    try:
        cant = int(input(f'¿Cuántos "{prod}" desea?: '))
        if cant <= 0:
            print('Error: La cantidad debe ser un número positivo.')
            continue
    except ValueError:
        print('Error: Debe ingresar un número entero (ej. 2).')
        continue
    carrito[prod] = carrito.get(prod, 0) + cant
    print(f'Se agregaron {cant} {prod}(s) al carrito.')

print('\n--- SU RECIBO ---')
if not carrito:
    print('No se ordenó ningún producto.')
else:
    total_general = 0
    for prod, cant in carrito.items():
        subtotal = menu[prod] * cant
        total_general += subtotal
        print(f' {cant} x {prod:<12} : ${subtotal:,.2f}')
    print('-' * 35)
    print(f'TOTAL A PAGAR: ${total_general:,.2f}')
    print('¡Gracias por su compra!')
