# p064-verificar-palindromo.py
# Verificar si un número entero es palíndromo

while True:
    print("\n--- Verificar Palíndromo ---")
    num = input("Introduce un número para verificar si es palíndromo: ")

    if num == num[::-1]:
        print(f"El número {num} es un palíndromo.")
    else:
        print(f"El número {num} no es un palíndromo.")

    if input("¿Desea continuar (S/N)? ").upper() == "N":
        break
