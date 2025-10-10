# p065-sistema-papeleria.py
# -------------------------------------------------------------
# Objetivo:
#   Sistema para gestionar ventas de fotocopias en una papelería.
#   Registra múltiples ventas, aplica descuento por volumen por transacción,
#   calcula subtotales por tipo y total general, y clasifica el desempeño del día.
#
# Desarrollador: Yovan Zamarripa Rivera
# -------------------------------------------------------------

# ----------------------------
# ENTRADAS / CONFIGURACIÓN
# ----------------------------
PRECIOS = {
    'C': 3.00,   # Carta
    'O': 4.00,   # Oficio
    'D': 6.00,   # Doble Oficio
    'P': 12.00   # Plano
}

NOMBRES = {
    'C': 'Carta',
    'O': 'Oficio',
    'D': 'Doble Of.',
    'P': 'Plano'
}

# Estructuras para acumulados por tipo
acum_cant = {k: 0 for k in PRECIOS.keys()}            # cantidad total por tipo
acum_subtotal = {k: 0.0 for k in PRECIOS.keys()}      # subtotal (ya con descuentos) por tipo
acum_original_con_desc = {k: 0.0 for k in PRECIOS.keys()}  # solo para mostrar "Precio original" donde hubo descuento

ventas_realizadas = 0  # número de transacciones
otra = 'S'

print("---------------------------------")
print("Papelería la Malena, SA. de CV.")
print("Sistema de ventas de copias")
print("---------------------------------")

# ----------------------------
# PROCESO: CAPTURA DE VENTAS
# ----------------------------
while otra.upper() == 'S':
    ventas_realizadas += 1
    print(f"Venta: {ventas_realizadas}")

    # Elegir tipo
    while True:
        tipo = input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 ? ").strip().upper()
        if tipo in PRECIOS:
            break
        print("Opción inválida. Responde con C, O, D o P.")

    # Cantidad
    while True:
        try:
            cant = int(input("Cantidad ? ").strip())
            if cant > 0:
                break
            print("La cantidad debe ser un entero positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

    precio_unit = PRECIOS[tipo]
    importe_original = cant * precio_unit

    # Descuento por transacción si cant > 50
    if cant > 50:
        importe_desc = round(importe_original * 0.90, 2)  # 10% de descuento
        print("*** Descuento del 10% aplicado por volumen! ***")
        # Acumular para mostrar "Precio original" en el resumen de ese tipo
        acum_original_con_desc[tipo] += importe_original
        importe_final = importe_desc
    else:
        importe_final = importe_original

    # Acumular por tipo
    acum_cant[tipo] += cant
    acum_subtotal[tipo] = round(acum_subtotal[tipo] + importe_final, 2)

    # ¿Otra venta?
    while True:
        otra = input("Otra venta (S/N) ? ").strip().upper()
        if otra in ('S', 'N'):
            break
        print("Responde S o N, por favor.")

# ----------------------------
# SALIDAS: RESUMEN DIARIO
# ----------------------------
print("---------------------------------------")
print("Resumen diario de ventas")
print("---------------------------------------")
print(f"Ventas realizadas: {ventas_realizadas}")
print("-------------------------")

# Imprimir por tipo en el orden especificado C, O, D, P
orden = ['C', 'O', 'D', 'P']
for k in orden:
    nombre = NOMBRES[k]
    cant = acum_cant[k]
    subtotal = acum_subtotal[k]
    # Línea base
    print(f"{nombre:<8}: {cant} - $ {subtotal:0.2f}")
    # Si hubo alguna transacción con descuento en ese tipo, mostrar precio original acumulado
    if acum_original_con_desc[k] > 0:
        print(f"(Precio original: $ {acum_original_con_desc[k]:0.2f})")

print("-------------------------")

# Totales globales
total_cant = sum(acum_cant.values())
total_monto = round(sum(acum_subtotal.values()), 2)
print(f"Tot. Ventas : {total_cant} - $ {total_monto:0.2f}")

# Clasificación del desempeño
def clasificar_desempeno(total: float) -> str:
    if total < 50.00:
        return "Venta moderada"
    elif 50.00 <= total <= 150.00:
        return "Venta frecuente"
    else:
        return "Venta superada"

print(f"Esta venta es una : {clasificar_desempeno(total_monto)}")
