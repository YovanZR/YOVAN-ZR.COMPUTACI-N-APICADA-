# p086-triangulo-invertido-numeros.py
# Triángulo numérico invertido

n = int(input("Dame un número: "))

i = n
while i >= 1:
    j = 1
    linea = ""
    while j <= i:
        linea = linea + str(j) + " "
        j = j + 1
    print(linea.strip())
    i = i - 1
