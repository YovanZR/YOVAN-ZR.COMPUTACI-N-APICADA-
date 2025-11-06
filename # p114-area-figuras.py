# p114-area-figuras.py
# Calculadora de áreas con diccionario de diccionarios (sin eval)

import math

figuras = {
    'Circulo':   {'param': ['radio']},
    'Triangulo': {'param': ['base', 'altura']},
    'Rectangulo':{'param': ['largo', 'ancho']}
}

print('\033[H\033[J')
print('Área de Figuras Geométricas\n')
print('Figuras disponibles:')
for nombre in figuras:
    print(f' - {nombre}')

# Elegir figura válida
while True:
    fig = input('\nElige una Figura: ').title().strip()
    if fig in figuras:
        break
    print('Error: Figura no válida. Intenta de nuevo.')

# Pedir parámetros
valores = {}
for p in figuras[fig]['param']:
    while True:
        try:
            valores[p] = float(input(f'{p.title()}: '))
            if valores[p] < 0:
                print('Debe ser no negativo.')
                continue
            break
        except ValueError:
            print('Ingresa un número válido.')

# Calcular área sin usar eval
area = 0.0
if fig == 'Circulo':
    r = valores['radio']
    area = math.pi * r ** 2
elif fig == 'Triangulo':
    b, a = valores['base'], valores['altura']
    area = 0.5 * b * a
elif fig == 'Rectangulo':
    l, a = valores['largo'], valores['ancho']
    area = l * a

print(f'\nEl Área del {fig} es: {area:.4f}')
