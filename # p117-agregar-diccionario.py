# p117-agregar-diccionario.py
# Agregar elementos nuevos a un diccionario

ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}

print("Ventas iniciales:")
print(ventas)

ventas['Rocio'] = 2500
ventas['Mateo'] = 1567
ventas.update({'Andrea': 9567})
ventas.update({'Miguel': 1234})

print("\nVentas actualizadas:")
print(ventas)
