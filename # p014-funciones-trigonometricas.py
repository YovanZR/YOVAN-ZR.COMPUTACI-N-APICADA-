# p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonométricas básicas

import math

print("=" * 50)
print(" FUNCIONES TRIGONOMÉTRICAS ")
print("=" * 50)

# Definir un ángulo en grados y convertirlo a radianes
angulo = 45
radianes = math.radians(angulo)

# Calcular funciones trigonométricas básicas
seno     = math.sin(radianes)
coseno   = math.cos(radianes)
tangente = math.tan(radianes)

# Convertir de vuelta a grados para demostración
grados = math.degrees(radianes)

# Formatear la salida con f-strings para mejor presentación
salida = (
    "Resumen de funciones\n"
    f"El seno es           {seno:.4f}\n"
    f"El coseno es         {coseno:.4f}\n"
    f"La tangente es       {tangente:.4f}\n"
    f"El ángulo {angulo}° en radianes es {radianes:.4f}\n"
    f"Los {radianes:.4f} radianes equivalen a {grados:.1f}°\n"
)

# Mostrar la salida formateada
print(salida)
print("=" * 50)
