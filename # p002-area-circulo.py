# p002-area-circulo
# Calcula el área de un círculo (A = PI * r * r)

import math #Se importa el módulo "MATH" para constantes y funciones matemáticas

print("Calculando el área de un círculo: \n")

#ENTRADA
print("Dame el radio: ")
radio = float(input())

#PROCESO
area = math.pi * math.pow(radio,2)

#SALIDA
print(f'El círculo de radio: {radio:.2f} , tiene un área de: {area:.2f}')