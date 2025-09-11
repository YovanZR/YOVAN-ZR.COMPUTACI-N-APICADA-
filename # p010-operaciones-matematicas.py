# p010-operaciones-matematicas.py
# Demostrar el uso de los diferentes operadores aritméticos con números

print("=" * 50)
print(" CALCULADORA DE OPERACIONES MATEMÁTICAS ")
print("=" * 50)

# Solicitar números al usuario
x = float(input("Ingresa el primer número (x): "))
y = float(input("Ingresa el segundo número (y): "))

print(f"\nRESULTADOS CON x = {x} y y = {y}")
print("-" * 50)

# Suma / Resta / Multiplicación
print(f"Suma:            {x:>8} + {y:<8} = {x + y:>12.2f}")
print(f"Resta:           {x:>8} - {y:<8} = {x - y:>12.2f}")
print(f"Multiplicación:  {x:>8} × {y:<8} = {x * y:>12.2f}")

# División (evitar división entre cero)
if y != 0:
    print(f"División:        {x:>8} ÷ {y:<8} = {x / y:>12.2f}")
    print(f"Módulo:          {x:>8} % {y:<8} = {x % y:>12.2f}")
    print(f"División entera: {x:>8} // {y:<8} = {x // y:>12.2f}")
else:
    print("División:        No definida (y = 0)")
    print("Módulo:          No definido (y = 0)")
    print("División entera: No definida (y = 0)")

# Exponenciación
print(f"Exponenciación:  {x:>8} ^ {y:<8} = {x ** y:>12.2f}")

print("=" * 50)
