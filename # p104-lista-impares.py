# Generar lista de n números impares y realizar cálculos
print('\033[H\033[J')

try:
    n = int(input("Introduzca la cantidad de números impares (n): "))
    lista = [2*i + 1 for i in range(n)]

    print("\n--- Generación de Lista ---")
    print(f"Lista de los primeros {n} números impares: {lista}")

    suma = sum(lista)
    promedio = suma / n if n > 0 else 0

    divisibles3 = [x for x in lista if x % 3 == 0]

    print("\n--- Cálculos ---")
    print(f"Suma de los números: {suma}")
    print(f"Promedio de los números: {promedio:.2f}")

    print("\n--- Divisibles entre 3 ---")
    print(f"Números divisibles entre 3: {divisibles3}")
    print(f"Suma de los números divisibles entre 3: {sum(divisibles3)}")

    buscar = int(input("\n--- Búsqueda ---\nIntroduzca elemento a buscar: "))
    if buscar in lista:
        print(f"Result: El elemento {buscar} está en la lista en la posición (índice) {lista.index(buscar)}.")
    else:
        print(f"Result: El elemento {buscar} no está en la lista.")
except ValueError:
    print("Entrada inválida, por favor ingrese un número entero.")
