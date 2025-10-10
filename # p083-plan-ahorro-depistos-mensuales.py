# p083-plan-ahorro-depistos-mensuales.py
# Simular plan de ahorro mensual

saldo = float(input("Monto inicial de ahorro: "))
deposito = float(input("Depósito mensual: "))
tasa_mensual = float(input("Tasa de interés mensual (%): "))
meses = int(input("Número de meses a simular: "))

print("--- Plan de Ahorro Detallado ---")

mes = 1
while mes <= meses:
    saldo_inicial_mes = saldo
    interes_mes = saldo_inicial_mes * (tasa_mensual / 100.0)
    saldo_final_mes = saldo_inicial_mes + interes_mes + deposito
    print(f"Mes {mes}: Saldo Inicial: ${saldo_inicial_mes:0.2f} | Interés: ${interes_mes:0.2f} | Saldo Final: ${saldo_final_mes:0.2f}")
    saldo = saldo_final_mes
    mes = mes + 1

print(f"Al final de {meses} meses, tendrás ${saldo:0.2f}")
