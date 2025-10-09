# p062-conversion-temperaturas.py
# Convertir un rango de temperaturas de Celsius a Fahrenheit

while True:
    print("\n--- Conversión de Temperaturas ---")
    ti = int(input("Introduce la temperatura inicial en °C: "))
    tf = int(input("Introduce la temperatura final en °C: "))

    print("-" * 20)
    c = ti
    while c <= tf:
        f = c * 9/5 + 32
        print(f"{c}°C = {f:.1f}°F")
        c += 1

    if input("¿Desea continuar (S/N)? ").upper() == "N":
        break
