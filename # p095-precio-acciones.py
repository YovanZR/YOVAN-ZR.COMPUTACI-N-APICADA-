# p095-precio-acciones.py
# Análisis básico de precios de una acción durante la semana

print('\033[H\033[J')
print('Análisis de precios semanales\n')

# Precios de cierre de una acción (Lunes a Viernes)
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
precios = [150.25, 152.50, 149.75, 155.00, 153.20]

# Encontrar el precio máximo y mínimo
precio_max = max(precios)
precio_min = min(precios)

# Encontrar la posición (el día) de esos precios
pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)

print(f"Precios de la semana: {precios}")
print(f"El precio más alto fue ${precio_max} el día {dias[pos_max]}.")
print(f"El precio más bajo fue ${precio_min} el día {dias[pos_min]}.")
