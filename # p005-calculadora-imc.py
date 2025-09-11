# p005-calculadora-imc
# Calcular el IMC de una persona

print("Calculando el Índice de Masa Corporal (IMC):\n")

#ENTRADA
peso_kg = float(input("Ingresa tu peso en kilogramos:"))
altura_m = float(input("Ingresa tu altura en metros: "))

#PROCESO
imc = peso_kg / (altura_m ** 2) # DIVIDE EL PESO ENTRE LA ALTURA AL CUADRADO (** ELEVA A UNA POTENCIA)

#SALIDA
print("\nEl peso es {0:.2f}kg y la altura es {1:.2f}m".format(peso_kg,altura_m))
print(f"\nTu peso es: {peso_kg:.2f}kg y la altura es: {altura_m:.2f}m y resulta en un IMC de: {imc:.2f}")

