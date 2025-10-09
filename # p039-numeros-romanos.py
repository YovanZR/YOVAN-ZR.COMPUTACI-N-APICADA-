# p039-numeros-romanos.py
# Problema: Convertir número a romano (1-10)

num = int(input("Ingresa un número entre 1 y 10: "))

romanos = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"
}

if num in romanos:
    print(romanos[num])
else:
    print("Error: Número inválido.")
