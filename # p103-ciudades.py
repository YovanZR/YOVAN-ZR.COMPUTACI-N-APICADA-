# Leer nombres de ciudades y analizar lista
print('\033[H\033[J')

ciudades = []

while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ")
    if ciudad == "$":
        break
    ciudades.append(ciudad)

if not ciudades:
    print("\nNo se introdujeron ciudades.")
else:
    descendente = sorted(ciudades, reverse=True)
    consonantes = [c for c in ciudades if c[0].lower() not in "aeiou"]

    print("\n--- Resultados ---")
    print(f"Total de ciudades introducidas: {len(ciudades)}")
    print(f"Lista original: {ciudades}")
    print(f"Lista ordenada descendente: {descendente}")
    print(f"Ciudades que inician con consonante: {len(consonantes)}")
    print(f"Lista de ciudades con consonante inicial: {consonantes}")
