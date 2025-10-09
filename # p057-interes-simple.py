# p057-interes-simple.py
# Calcula años necesarios para alcanzar una meta con interés simple anual.

while True:
    print('\033[H\033[J', end='')
    print("Calculadora: Meta de Ahorro con Interés Simple")
    print("-" * 55)

    # Captura y validación
    while True:
        try:
            capital_inicial = float(input("Capital inicial: "))
            tasa_interes = float(input("Tasa de interés anual (%): "))
            meta_ahorro = float(input("Meta de ahorro: "))
            if capital_inicial > 0 and tasa_interes > 0 and meta_ahorro > capital_inicial:
                break
            print("Error: positivos, y meta > capital inicial.")
        except ValueError:
            print("Error: ingresa números válidos.")

    capital_actual = capital_inicial
    anios = 0
    interes_anual_fijo = capital_inicial * (tasa_interes / 100.0)  # interés simple

    while capital_actual < meta_ahorro - 1e-9:
        capital_actual += interes_anual_fijo
        anios += 1

    print("\nResultado:")
    print(f"Años necesarios: {anios}")
    print(f"Monto final: ${capital_actual:,.2f}")
    print("-" * 55)

    if input("¿Realizar otro cálculo (S/N)? ").strip().upper() == 'N':
        print("\nFin del programa. ¡Éxito con tus ahorros!")
        break
