# p068-conteo-ascendente-for-v2.py
print("Iniciando secuencia de conteo ascendente...")
n = int(input("Hasta donde ? "))
m = int(input("De cuanto en cuanto ? "))
for i in range(1, n+1, m):
    print(i, end=' ')
