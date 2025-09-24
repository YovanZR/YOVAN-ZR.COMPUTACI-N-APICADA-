# Simula una calculadora de descuentos basada en el monto de la compra

print("Calculadora de Descuentos \n")
compra = float(input("Ingresa el total de tu compra: $"))

# Definimos las variables para el descuento
descuento = 0
porcentaje = 0

if compra > 2000:
    porcentaje = 0.20  # 20% de descuento
    descuento = compra * porcentaje
else:
    if compra > 1000:
        porcentaje = 0.10  # 10% de descuento
        descuento = compra * porcentaje
    else:
        if compra > 500:
            porcentaje = 0.05  # 5% de descuento
            descuento = compra * porcentaje
        else:
            # Si no aplica ninguno de los descuentos anteriores
            descuento = 0

# Calculamos y mostramos el resultado
total = compra - descuento

print("\n--- Resumen de la Compra ---")
print(f"Total de la compra: ${compra:,.2f}")
print(f"Porcentaje de descuento: {int(porcentaje * 100)}%")
print(f"Ahorro por descuento: ${descuento:,.2f}")
print(f"Total a pagar: ${total:,.2f}")

print("\n¡Gracias por tu compra!")
