# p070-conteo-descendente-for-v2.py
print("Iniciando cuenta regresiva...")
n = int(input("Desde donde ? "))
m = int(input("De cuanto en cuanto ? "))
for x in range(n, 0, -m):
    print(x, end=' ')
