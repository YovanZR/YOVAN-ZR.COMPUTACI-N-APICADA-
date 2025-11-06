# p123-conjunto-personas.py
# Autor: Yovan Zamarripa Rivera
# Descripción: Operaciones con conjuntos de personas

lista1 = ['Juan', 'Maria', 'Pedro', 'Jose', 'Rocio']
lista2 = ['Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther']

A = set(lista1)
B = set(lista2)

print("Conjunto A:", A)
print("Conjunto B:", B)
print()

print("Unión (A | B):", A | B)
print("Intersección (A & B):", A & B)
print("Diferencia (A - B):", A - B)
print("Diferencia Simétrica (A ^ B):", A ^ B)
print()

print("¿{Pablo, Mateo} es subconjunto de B?:", {'Pablo', 'Mateo'}.issubset(B))
print("¿A es superconjunto de {Reynaldo, Angelica}?:", A.issuperset({'Reynaldo', 'Angelica'}))
print("¿'Pedro' está en el conjunto A?:", 'Pedro' in A)
print("¿'Lilia' no está en el conjunto B?:", 'Lilia' not in B)
