# p078-piramide-caracter.py
# Imprime una pirámide de caracteres

print('\033[H\033[J')
print('Imprime una pirámide de caracteres')

altura = int(input("Introduce la altura de la pirámide: "))
car = input("Introduce el carácter para la pirámide: ")

print("\n--- Pirámide Generada ---")
for i in range(1, altura + 1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for j in range(espacios):      # Espacios en blanco
        print(" ", end="")
    for k in range(caracteres):    # Caracteres de la pirámide
        print(car, end="")
    print()