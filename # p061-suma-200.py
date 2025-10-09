# p061-suma-200.py
# Leer números y sumarlos hasta que el total >= 200

while True:
    print("\n--- Suma hasta 200 ---")
    suma = 0
    cuenta = 0
    while suma < 200:
        num = int(input(f"Suma actual: {suma}. Introduce un número: "))
        suma += num
        cuenta += 1

    print("-" * 20)
    print("Meta de 200 alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de números introducidos: {cuenta}")

    if input("¿Desea continuar (S/N)? ").upper() == "N":
        break
