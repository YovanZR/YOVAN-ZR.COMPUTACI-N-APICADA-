# p049-sumar-consecutivos.py
# Suma números consecutivos (1 + 2 + 3 + ...) hasta que la suma sea >= 100, usando 'break'.

c = 0
suma = 0
print("Meta: 100. Empezando a sumar números...")

# Límite de seguridad alto; 'break' detendrá el ciclo antes.
while c < 1000:
    c += 1
    suma += c
    print(f"(+{c})", end=" ")
    if suma >= 100:
        print("\n\n¡Meta alcanzada!")
        break

print(f"Se necesitaron los primeros {c} números para llegar a una suma de {suma}.")
