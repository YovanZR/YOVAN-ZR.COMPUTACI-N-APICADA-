# p079-factorial-numeros.py
# Calcula el factorial de n números

print("--- Cálculo Sucesivo de Factoriales ---\n")

try:
    n = int(input("¿Hasta qué número deseas calcular el factorial? "))

    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        print(f"El factorial de {i}! es = {factorial}")

except ValueError:
    print("Error: Por favor, introduce un número entero válido.")
