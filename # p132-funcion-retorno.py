def suma(n1: float, n2: float) -> float:
    return n1 + n2

print('Suma de dos numeros constantes: ')
suma_resultado = suma(10,20)
print(f"La suma es {suma_resultado}")

print('Dame dos numeros separados por enter: ')
a,b = int(input()), int(input())
print(f"La suma de los numeros es {suma(a,b)}")
