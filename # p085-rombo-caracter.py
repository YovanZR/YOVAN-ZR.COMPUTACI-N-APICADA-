# p085-rombo-caracter.py
# Dibuja un rombo con un número impar

n = int(input("Dame un número impar para la altura: "))
while n <= 0 or n % 2 == 0:
    print("El número debe ser IMPAR y mayor que 0.")
    n = int(input("Dame un número impar para la altura: "))

car = input("¿Qué carácter quieres usar? ")

mid = (n // 2) + 1

i = 1
while i <= mid:
    esp = mid - i
    num_car = 2 * i - 1
    j = 1
    linea = ""
    while j <= esp:
        linea = linea + " "
        j = j + 1
    k = 1
    while k <= num_car:
        linea = linea + car
        k = k + 1
    print(linea)
    i = i + 1

i = mid - 1
while i >= 1:
    esp = mid - i
    num_car = 2 * i - 1
    j = 1
    linea = ""
    while j <= esp:
        linea = linea + " "
        j = j + 1
    k = 1
    while k <= num_car:
        linea = linea + car
        k = k + 1
    print(linea)
    i = i - 1
