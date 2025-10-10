# p077-triangulo-caracter.py
# Imprime un triángulo rectángulo de caracteres

print('\033[H\033[J')

n = int(input("¿Cuántos renglones tendrá el triángulo? "))
car = input("¿Qué carácter quieres usar para dibujar? ")

print("\n--- Triángulo Generado ---")
for i in range(1, n + 1):     # Filas
    for j in range(i):        # Columnas (igual al número de fila)
        print(car, end="")
    print()
