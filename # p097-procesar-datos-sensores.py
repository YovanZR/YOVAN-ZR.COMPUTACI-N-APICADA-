# p097-procesar-datos-sensores.py
# Simulación de recolección y procesamiento de datos de sensores

import random

print('\033[H\033[J')
print("Simulando la recolección de datos de dos sensores...")

# --- 1. Generación de Datos Simulados ---
sensor_a_datos = []
sensor_b_datos = []
for _ in range(10):
    sensor_a_datos.append(random.randint(1, 100))  # Lista del sensor A
    sensor_b_datos.append(random.randint(1, 100))  # Lista del sensor B

print("\n--- Datos Originales de los Sensores ---")
print(f"Sensor A: {sensor_a_datos}")
print(f"Sensor B: {sensor_b_datos}")

# --- 2. Transformación (elevar al cuadrado) y 3. Combinación (suma elemento a elemento) ---
datos_combinados = []
for i in range(10):
    sensor_a_datos[i] = sensor_a_datos[i] ** 2
    sensor_b_datos[i] = sensor_b_datos[i] ** 2
    suma_transformada = sensor_a_datos[i] + sensor_b_datos[i]
    datos_combinados.append(suma_transformada)

# --- 4. Muestra de Resultados ---
print("\n--- Datos Procesados ---")
print(f"Sensor A (Transformados): {sensor_a_datos}")
print(f"Sensor B (Transformados): {sensor_b_datos}")
print(f"Datos Combinados: {datos_combinados}")
