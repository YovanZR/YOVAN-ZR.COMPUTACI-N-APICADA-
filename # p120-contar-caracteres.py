# p120-contar-caracteres.py
# Contar frecuencia de caracteres en una cadena

cadena = input("Ingrese una cadena: ")
frecuencia = {}

for caracter in cadena:
    if caracter in frecuencia:
        frecuencia[caracter] += 1
    else:
        frecuencia[caracter] = 1

print("\nResultado:")
print(frecuencia)
