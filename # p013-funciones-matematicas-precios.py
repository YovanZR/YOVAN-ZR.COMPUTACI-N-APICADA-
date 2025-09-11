# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas para redondeo y manejo de precios

import math

print("=" * 50)
print(" REDONDEO DE PRECIOS ")
print("=" * 50)

# Precio con decimales
precio = 15.65

# Diferentes métodos de redondeo
arriba   = math.ceil(precio)
abajo    = math.floor(precio)
truncado = math.trunc(precio)
redondeo = round(precio)      # redondeo estándar al entero más cercano
un_dec   = round(precio, 1)   # a 1 decimal
dos_dec  = round(precio, 2)   # a 2 decimales

# Mostrar resultados con formato
print(f"Precio original         : ${precio:.2f}")
print(f"Redondeo arriba (ceil)  : ${arriba}")
print(f"Redondeo abajo (floor)  : ${abajo}")
print(f"Truncado (trunc)        : ${truncado}")
print(f"Redondeo normal         : ${redondeo}")
print(f"Redondeo 1 decimal      : ${un_dec:.1f}")
print(f"Redondeo 2 decimales    : ${dos_dec:.2f}")
print("=" * 50)
