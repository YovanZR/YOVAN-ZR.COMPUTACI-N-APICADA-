# Mostrar el tipo de ángulo según su medida en grados.

print('--- Clasificador de Ángulos ---')
angulo = int(input('Dame un ángulo en grados: '))

# Validación de rango básico
if angulo < 0 or angulo > 360:
    print(' El ángulo está fuera del rango de 0 a 360 grados.')
elif angulo < 90:
    print(f' El ángulo de {angulo} grados es un ángulo AGUDO.')
elif angulo == 90:
    print(f' El ángulo de {angulo} grados es un ángulo RECTO.')
elif angulo < 180:
    print(f' El ángulo de {angulo} grados es un ángulo OBTUSO.')
elif angulo == 180:
    print(f' El ángulo de {angulo} grados es un ángulo LLANO.')
elif angulo < 360:
    print(f' El ángulo de {angulo} grados es un ángulo CÓNcAVO.')
else:  # 360
    print(f' El ángulo de {angulo} grados es un ángulo COMPLETO.')
