# p041-aceptar-estudiante-v2.py
# Problema: Universidad Kitty Kat SA

nombre = input("Nombre: ")
sexo = input("Sexo (h/m): ").lower()
edad = int(input("Edad: "))

suma = 0
for i in range(1, 4):
    cal = float(input(f"Calificación {i}: "))
    suma += cal

promedio = suma / 3

if sexo != "m":
    print(f"Lo sentimos, {nombre}. La universidad solo acepta mujeres.")
elif edad <= 21:
    print(f"Lo sentimos, {nombre}. No cumples con la edad requerida (mayores de 21 años).")
elif promedio < 8:
    print(f"Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} no alcanza el mínimo requerido de 8.")
elif promedio > 9.5:
    print(f"Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} excede el máximo permitido de 9.5.")
else:
    print(f"¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {promedio:.2f} está dentro del rango permitido.")
