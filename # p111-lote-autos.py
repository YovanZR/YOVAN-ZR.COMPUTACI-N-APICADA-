# p111-lote-autos.py
# Crear una lista de diccionarios para representar un lote de autos

autos = [
    {'marca': 'Ford', 'modelo': 'Mustang', 'año': 1964},
    {'marca': 'VW', 'modelo': 'Jetta', 'año': 2015}
]

# Agregar otro auto
autos.append({'marca': 'Ford', 'modelo': 'Focus', 'año': 2000})

print('\033[H\033[J')
print('=' * 50)
print('Listado de Autos')
print('=' * 50)

# Vista general
print(f'\nTodos los autos: {autos}\nTotal: {len(autos)}')

# Mostrar cada auto
print('\nCada auto dentro de los autos:')
print('-' * 50)
for auto in autos:
    print(auto)

# Tabla
print('\nDatos en forma de Tabla:')
print('-' * 50)
# Encabezados (toman las llaves del primer diccionario)
headers = list(autos[0].keys())
print(''.join(f'{h:<12}' for h in headers))
for auto in autos:
    print(''.join(f'{str(auto[h]):<12}' for h in headers))

# Registros (llave : valor)
print('\nDatos en forma de Registro')
print('-' * 50)
for auto in autos:
    for k, v in auto.items():
        print(f'{k:<12} : {v}')
    print('')
