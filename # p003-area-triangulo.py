# p003-area-triangulo
# Calcula el área de un triángulo

print("Calculando el área de un triángulo: \n")

#ENTRADA
print("Dame la base y la altura separados por ENTER")
base, altura = int(input()), int(input()) #Lee dos valores

#PROCESO
area = (base * altura) / 2

#SALIDA
print("El triangulo de base    :", base)
print("El triangulo de altura  :", altura)
print("Tiene un área de        :", area)

print(f'\nEl triangulo de base {base} y altura {altura} tiene un area de: {area:.2f}')
print("El triangulo de base " + str(base) + " y altura " + str(altura) + " tiene un area de " + str(area))