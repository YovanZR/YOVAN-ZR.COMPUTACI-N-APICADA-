# Clasificar un triángulo según la longitud de sus tres lados.

print('--- CLASIFICADOR DE TRIÁNGULOS ---')
print('Ingresa la longitud de los tres lados de un triángulo.')

lado_a = float(input('Ingresa la longitud del primer lado: '))
lado_b = float(input('Ingresa la longitud del segundo lado: '))
lado_c = float(input('Ingresa la longitud del tercer lado: '))

# (Opcional) Validación simple de existencia del triángulo usando desigualdad triangular
# Si quisieras ser más estricto, descomenta:
# if not (lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a):
#     print(' Las longitudes no forman un triángulo válido.')
#     raise SystemExit

if lado_a == lado_b and lado_b == lado_c:
    print(' Es un triángulo EQUILÁTERO (todos los lados son iguales).')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print(' Es un triángulo ISÓSCELES (al menos dos lados son iguales).')
else:
    print(' Es un triángulo ESCALENO (ningún lado es igual).')
