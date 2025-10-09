# p036-numeros-consecutivos.py
# Problema: Verificar si tres números son consecutivos

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

# Ordenamos los números para evaluar consecutividad
numeros = [a, b, c]
numeros.sort()

if numeros[1] == numeros[0] + 1 and numeros[2] == numeros[1] + 1:
    print("Los números son consecutivos.")
else:
    print("Los números no son consecutivos.")
