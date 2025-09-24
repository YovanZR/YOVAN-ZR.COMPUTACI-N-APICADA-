# Aceptar a un estudiante en base a la edad y calificaciones (versión invertida).

print('--- Admisiones de la Universidad Patito ---')
nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

# Verificación de edad (inversa)
if edad >= 18:
    print('Ingresa 2 calificaciones para continuar:')
    calificacion1 = float(input())
    calificacion2 = float(input())

    # Aprobación solo si ambas >= 8
    if calificacion1 >= 8 and calificacion2 >= 8:
        print(f' ¡Bienvenid@, {nombre}! Tu edad de {edad} y tus calificaciones te permiten ingresar.')
    else:
        print(' Lo sentimos, se requiere una calificación mínima de 8 en ambos exámenes.')
else:
    print(f' Lo sentimos, {nombre}. Solo aceptamos a mayores de 18 años.')
