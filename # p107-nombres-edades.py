# p107-nombres-edades.py
# Gestión de nombres y edades usando diccionarios

print('\033[H\033[J')
print('Gestión de nombres y edades usando diccionarios\n')

datos = {}
print('Introduce nombres y edades (nombre vacío para terminar)')
while True:
    nombre = input('Nombre: ').strip()
    if nombre == '':
        break
    try:
        edad = int(input('Edad: '))
        if edad < 0:
            print('La edad debe ser positiva. Intenta de nuevo.')
            continue
    except ValueError:
        print('Error: Debe ingresar un número entero para la edad.')
        continue
    datos[nombre] = edad

print(f'\nEl diccionario de datos creado: ({len(datos)}) -> {datos}\n')

print('Listado y promedio de edades:')
suma = 0
for n, e in datos.items():
    print(f'{n:<20} - {e:2}')
    suma += e

prom = (suma / len(datos)) if datos else 0
print(f'\nSuma: {suma}  |  Promedio: {prom:.2f}')
