# p050-conteo-numeros.py
# Lee números hasta ingresar 999 y muestra estadísticas.

cuenta = 0
suma = 0
cuenta_positivos = 0
cuenta_negativos = 0
cuenta_ceros = 0

print("Analizador de Números (escribe 999 para finalizar)")

while True:
    num = int(input("Introduce un número entero: "))
    if num == 999:
        print("Detectado código de salida (999).")
        break

    cuenta += 1
    suma += num

    if num > 0:
        cuenta_positivos += 1
    elif num < 0:
        cuenta_negativos += 1
    else:
        cuenta_ceros += 1

print("\n========== REPORTE FINAL ==========")
print(f"Números introducidos: {cuenta}")
print(f"Suma total: {suma}")
print(f"Positivos: {cuenta_positivos}")
print(f"Negativos: {cuenta_negativos}")
print(f"Ceros: {cuenta_ceros}")
print("===================================")
