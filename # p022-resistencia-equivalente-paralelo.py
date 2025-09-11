# p022-resistencia-equivalente-paralelo.py
# Calcular la resistencia equivalente de resistencias en paralelo:
# 1/Req = 1/R1 + 1/R2 + 1/R3

print("=" * 50)
print(" RESISTENCIA EQUIVALENTE EN PARALELO ")
print("=" * 50)

R1 = float(input("Resistencia R1 (Ω): "))
R2 = float(input("Resistencia R2 (Ω): "))
R3 = float(input("Resistencia R3 (Ω): "))

Req = 1 / ((1/R1) + (1/R2) + (1/R3))

print("-" * 50)
print(f"Resistencias: R1 = {R1} Ω, R2 = {R2} Ω, R3 = {R3} Ω")
print(f"Resistencia equivalente (paralelo) = {Req:.4f} Ω")
print("=" * 50)
