# p008-entrada-con-espacio
# Leer 3 números enteros separados por un espacio

print("Entrada de varios valores separados por un espacio")

print("Dame 3 números, separalos con un espacio:")

n1, n2, n3 = input().split() #LEO UNA LINEA Y LA SEPARO EN BASE AL ESPACIO (SPLIT)

n1, n2, n3 = int(n1), int(n2), int(n3)

print("Los valores introducidos son:")
print(n1,n2,n3)