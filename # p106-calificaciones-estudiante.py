# p106-calificaciones-estudiante.py
# Gestión de calificaciones de un estudiante usando diccionarios

print('\033[H\033[J')
print('Gestión de calificaciones de un estudiante usando diccionarios')

materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
califs = [10, 9, 8, 7.5, 6]

print(f'Lista de materias: {materias}')
print(f'Lista de calificaciones: {califs}\n')

# Crear diccionario desde las listas
notas = dict(zip(materias, califs))
print(f'Diccionario nuevo juntando las listas: ({len(notas)}) -> {notas}')

# Agregar elementos
notas.update({'Ingles': 10})
notas.update({'Programacion': 7})
print(f'\nSe agregaron elementos: ({len(notas)}) -> {notas}')

# Remover elementos
notas.pop('Fisica', None)   # evitar KeyError si no existe
notas.popitem()             # elimina el último insertado
print(f'\nSe removieron elementos: ({len(notas)}) -> {notas}')

# Modificar elementos
notas.update({'Quimica': 10})
notas.update({'Matematicas': 10})
print(f'\nSe modificaron elementos: {notas}\n')

# Recorrido y cálculos
print('Materias y calificaciones finales')
suma = 0
for materia, cal in notas.items():
    print(f'{materia:<12} - {cal:>5}')
    suma += cal

prom = suma / len(notas) if notas else 0
print(f'\nLa suma: {suma} y el promedio: {prom:.2f}')

# Limpiar todo
notas.clear()
print(f'\nSe borró todo: {notas}')
