# Mostrar nombre del mes y días según número ingresado
print('\033[H\033[J')

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    num = int(input("Introduzca un número de mes (1-12): "))
    if 1 <= num <= 12:
        print("\n--- Resultados ---")
        print(f"Mes: {meses[num-1]}")
        print(f"Días: {dias[num-1]}")
    else:
        print("Número de mes inválido. Debe estar entre 1 y 12.")
except ValueError:
    print("Entrada inválida, debe ser un número entero.")
