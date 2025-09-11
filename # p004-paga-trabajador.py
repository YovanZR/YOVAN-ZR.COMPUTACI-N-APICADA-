# p004-paga-trabajador
# Calcular la paga total de un trabajador

print("Calculando la paga de un trabajador\n")

#ENTRADA
Nombre = input("Nombre:")
Horas = int(input("Horas:"))    
Paga = float(input("Paga x Hora:")) 

#PROCESO
tasa = 0.03 #IMPUESTO DE HACIENDA
pagabruta = Horas * Paga
impuesto = tasa * pagabruta
paganeta = pagabruta - impuesto

#SALIDA
print("\nResumen de Pagos")
print(f"El trabajador {Nombre}, trabajó {Horas} horas, con una paga de {Paga:.2f} pesos, con una tasa de {tasa:.2%}")
print(f"Paga Bruta: {pagabruta:.2f}")
print(f"Impuesto: {impuesto:.2f}")
print(f"Paga Neta: {paganeta:.2f}")
