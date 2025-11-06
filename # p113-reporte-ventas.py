# p113-reporte-ventas.py
# Crear una lista de diccionarios para representar un reporte de ventas

print('\033[H\033[J')
print('Reporte de Ventas\n')
print('-' * 60)
print('--- Registro de Transacciones ---')

# Captura de compras
while True:
    try:
        n = int(input('Número de compras a registrar: '))
        if n < 0:
            print('Debe ser un entero no negativo.')
            continue
        break
    except ValueError:
        print('Entrada inválida, intenta de nuevo.')

compras = []
for i in range(1, n + 1):
    print(f'\n------ Compra {i} ------')
    cliente = input('Nombre Cliente: ').strip()
    producto = input('Nombre Producto: ').strip()
    while True:
        try:
            cantidad = int(input('Cantidad: '))
            if cantidad <= 0:
                print('Debe ser positiva.')
                continue
            break
        except ValueError:
            print('Ingrese un entero.')
    while True:
        try:
            precio = float(input('Precio: '))
            if precio < 0:
                print('No puede ser negativo.')
                continue
            break
        except ValueError:
            print('Ingrese un número.')
    compras.append({'cliente': cliente, 'producto': producto, 'cantidad': cantidad, 'precio': precio})

print('\n--- Lista de Compras Registradas ---')
print(compras)

# Agregación por cliente (diccionario de diccionarios)
clientes = {}
for compra in compras:
    cli = compra['cliente']
    if cli not in clientes:
        clientes[cli] = {'cantidad': 0, 'subtotal': 0.0}
    clientes[cli]['cantidad'] += compra['cantidad']
    clientes[cli]['subtotal'] += compra['cantidad'] * compra['precio']

print('\n--- Reporte de Totales por Cliente ---\n')
for cli, datos in clientes.items():
    print(f'Cliente: {cli}')
    print(f'Cantidad Total de Productos: {datos["cantidad"]}')
    print(f'Subtotal a Pagar: ${datos["subtotal"]:,.2f}\n')

print('\n--- Diccionario de Clientes (Estructura Interna) ---')
print(clientes)
