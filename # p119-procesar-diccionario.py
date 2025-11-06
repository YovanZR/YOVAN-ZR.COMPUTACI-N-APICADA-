# p119-procesar-diccionario.py
# Procesar un diccionario con nombres y sueldos

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))

print("Diccionario de nómina:")
print(nomina)

print("\n--- Iterando Llaves (keys) ---")
for nombre in nomina.keys():
    print(nombre)

print("\n--- Iterando Valores (values) ---")
for sueldo in nomina.values():
    print(sueldo)

print("\n--- Iterando Llave y Valor (accediendo por llave) ---")
for nombre in nomina:
    print(f"{nombre} -> {nomina[nombre]}")

print("\n--- Iterando Llave y Valor (items) ---")
for item in nomina.items():
    print(item)

total = sum(nomina.values())
promedio = total / len(nomina)

print("\n--- Cálculos ---")
print(f"Suma total de sueldos: {total:.2f}")
print(f"Promedio de sueldos: {promedio:.2f}")
