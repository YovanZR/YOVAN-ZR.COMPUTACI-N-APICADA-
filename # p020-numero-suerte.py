# p020-numero-suerte.py
# Calcular número de la suerte a partir del año de nacimiento

print("=" * 50)
print(" NÚMERO DE LA SUERTE ")
print("=" * 50)

anio = input("Año de nacimiento (4 dígitos): ")
digitos = [int(d) for d in anio]
suma = sum(digitos)

print("-" * 50)
print(f"Año ingresado: {anio}")
print(f"Dígitos: {' - '.join(anio)}")
print(f"Suma de los dígitos: {suma}")
print("=" * 50)
