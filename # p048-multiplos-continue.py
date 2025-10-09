# p048-multiplos-continue.py
# Imprime solo los múltiplos de 10 entre 1 y 200 usando 'continue'.

print("Buscando múltiplos de 10 entre 1 y 200...")
c = 0
while c < 200:
    c += 1
    if c % 10 != 0:
        # Ignora el resto y salta a la siguiente iteración
        continue
    # Solo se ejecuta si c es múltiplo de 10
    print(f"{c}", end=" ")

print("\nBúsqueda finalizada.")
