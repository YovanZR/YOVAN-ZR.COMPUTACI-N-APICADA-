# p080-combina-colores.py
# Genera combinaciones de dos colores a partir de una lista

print("--- Generador de Combinaciones de Colores ---\n")

colores = input("Ingresa los colores separados por comas: ").strip().split(',')

print(f"\nColores base: {colores}")
print("--- Combinaciones Posibles ---")

for color1 in colores:
    for color2 in colores:
        if color1 != color2:
            print(f"- {color1.strip()} y {color2.strip()}")
