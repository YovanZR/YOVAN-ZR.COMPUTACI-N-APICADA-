# p124-conjunto-numeros.py
# Autor: Yovan Zamarripa Rivera
# Descripción: Operaciones con conjuntos numéricos

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista1)
B = set(lista2)
C = set(lista3)

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)
print()

print("Unión (A | B):", A | B)
print("Unión (B | C):", B | C)
print("Diferencia (A - C):", A - C)
print("Diferencia Simétrica (B ^ C):", B ^ C)
print("Intersección (B & C):", B & C)
print()

print("¿A es subconjunto de B?:", A.issubset(B))
print("¿C es subconjunto de A?:", C.issubset(A))
print("¿El número 100 está en A?:", 100 in A)
print("¿El número 60 está en A, B y C?:", 60 in A and 60 in B and 60 in C)
print("¿El número 900 no está en C?:", 900 not in C)
