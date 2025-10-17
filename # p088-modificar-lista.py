# p088-modificar-lista.py
# Modificar los elementos de una lista

print('\033[H\033[J')
print('Modificar los elementos de una lista')

califs = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]
print(f'\nTodas las calificaciones: {califs}')

print('\nModificar calificaciones en posiciones [0] y [1] con 7 y 7:')
califs[0] = 7
califs[1] = 7
print(f'Resultado: {califs}')

print('\nModificar calificaciones en el rango [2:5] (5 no incluida) con 9, 9, 9:')
califs[2:5] = [9, 9, 9]
print(f'Resultado: {califs}')

# Demostración de mutabilidad adicional
print('\nReemplazar las últimas dos por [8, 8.5]:')
califs[-2:] = [8, 8.5]
print(f'Resultado: {califs}')
