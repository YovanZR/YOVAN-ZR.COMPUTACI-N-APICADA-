# p112-registro-estudiantes.py
# Crear una lista de diccionarios para representar un registro de estudiantes

grupo = [
    {'nombre': 'Carlos', 'edad': 45, 'carrera': 'sistemas', 'promedio': 9.0},
    {'nombre': 'Rocio',  'edad': 35, 'carrera': 'sistemas', 'promedio': 10.0}
]

print('\033[H\033[J')
print('Registro de Estudiantes\n')

print('Grupo de estudiantes inicial:')
print('-' * 60)
print(grupo, '-', len(grupo))

# Captura de nuevos estudiantes
print('\nCaptura de nuevos estudiantes')
print('-' * 60)
while True:
    nombre = input('Nombre (vacío para terminar): ').strip()
    if nombre == '':
        break
    try:
        edad = int(input('Edad: '))
        carrera = input('Carrera: ').strip()
        promedio = float(input('Promedio: '))
    except ValueError:
        print('Dato inválido. Intenta de nuevo.')
        continue
    datos = {'nombre': nombre, 'edad': edad, 'carrera': carrera, 'promedio': promedio}
    grupo.append(datos)

# Grupo completo
print('\nGrupo de estudiantes completo:')
print('-' * 60)
print(grupo, '-', len(grupo))

# Tabla formateada
print('\nDatos en forma de Tabla:')
print('-' * 60)
headers = list(grupo[0].keys())
print(''.join(f'{h:<13}' for h in headers))
for alumno in grupo:
    print(''.join(f'{str(alumno[h]):<13}' for h in headers))

# Registro y cálculo de promedios
print('\nDatos en forma de Registro y Cálculo de Promedios:')
print('-' * 60)
suma = 0
for est in grupo:
    suma += float(est.get('promedio', 0))
    for k, v in est.items():
        print(f'{k:<10} : {v}')
    print('')

print('\nCálculo de Promedios:')
print('-' * 60)
prom = suma / len(grupo) if grupo else 0
print(f'La suma es {suma:.2f}')
print(f'El promedio es {prom:.2f}')
