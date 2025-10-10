# p084-cuadro-hueco-caracter.py
# Dibuja un cuadrado hueco con un carácter dado

n = int(input("¿De qué tamaño será el lado del cuadrado? "))
car = input("¿Qué carácter quieres usar? ")

fila = 1
while fila <= n:
    col = 1
    linea = ""
    while col <= n:
        if fila == 1 or fila == n or col == 1 or col == n:
            linea = linea + car + " "
        else:
            linea = linea + "  "
        col = col + 1
    print(linea.strip())
    fila = fila + 1
