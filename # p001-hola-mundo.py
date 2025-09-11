# p001-hola-mundo
# Lee datos y envia un saludo

print("Leyendo datos y enviando un saludo: \n")

nombre = input("Dame tu nombre:")
edad = int(input("Dame tu edad:"))
peso = float(input("Dame tu peso:"))

print(f"Bienvenido {nombre}, tu edad es {edad}, tu peso es {peso} \n")

print(type(nombre)) 
print(type(edad))
print(type(peso))