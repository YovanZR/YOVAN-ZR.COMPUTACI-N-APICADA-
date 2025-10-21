# Procesar notas entre 0 y 100 hasta ingresar 0
print('\033[H\033[J')
print("Procesador de Notas\n")

notas = []
suma = 0.0

while True:
    try:
        n = int(input("Introduzca nota (0 para detener): "))
        if n == 0:
            break
        if 0 <= n <= 100:
            notas.append(n)
            suma += n
        else:
            print("Entrada inválida, debe ser 0-100")
    except ValueError:
        print("Entrada no válida, por favor ingrese un número entero.")

if not notas:
    print("\nNo se introdujeron notas.")
else:
    promedio = suma / len(notas)
    menores_prom = [x for x in notas if x < promedio]

    print("\n--- Resultados ---")
    print(f"Total de notas introducidas: {len(notas)}")
    print(f"Lista de notas: {notas}")
    print(f"Suma de notas: {suma}")
    print(f"Promedio de notas: {promedio:.2f}")
    print(f"Nota máxima: {max(notas)}")
    print(f"Nota mínima: {min(notas)}")
    print(f"Notas menores al promedio ({promedio:.2f}): {len(menores_prom)}")
    print(f"Lista de notas menores al promedio: {menores_prom}")
