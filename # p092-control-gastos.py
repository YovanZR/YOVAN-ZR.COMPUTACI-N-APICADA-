# p092-control-gastos.py
# Control de Gastos con menú, manejo de errores y PERSISTENCIA CSV
# - Carga automática desde gastos.csv si existe
# - Guarda automáticamente después de agregar, modificar o eliminar

import csv
import os

print('\033[H\033[J')
print('Control de Gastos Mensuales (con CSV)\n')

CSV_FILE = 'gastos.csv'
gastos = []  # lista de floats


def cargar_csv():
    if not os.path.exists(CSV_FILE):
        return
    try:
        with open(CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                try:
                    gastos.append(float(row[0]))
                except ValueError:
                    pass  # ignora filas inválidas
        print(f'✔ Datos cargados desde {CSV_FILE}.')
    except Exception as e:
        print(f'❌ No se pudo cargar {CSV_FILE}: {e}')


def guardar_csv():
    try:
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for g in gastos:
                writer.writerow([g])
        print(f'✔ Datos guardados en {CSV_FILE}.')
    except Exception as e:
        print(f'❌ No se pudo guardar en {CSV_FILE}: {e}')


def ver_gastos():
    if not gastos:
        print('No hay gastos registrados.')
        return
    print('Gastos actuales:')
    for i, g in enumerate(gastos):
        print(f'[{i}] ${g:.2f}')


def agregar_gasto():
    try:
        monto = float(input('Monto a agregar: $'))
        if monto < 0:
            print('El monto no puede ser negativo.')
            return
        gastos.append(monto)
        guardar_csv()
        print('✔ Gasto agregado.')
    except ValueError:
        print('❌ Error: ingresa un número válido.')


def modificar_gasto():
    try:
        idx = int(input('Índice a modificar: '))
        if idx < 0 or idx >= len(gastos):
            print('❌ Índice fuera de rango.')
            return
        nuevo = float(input('Nuevo monto: $'))
        if nuevo < 0:
            print('El monto no puede ser negativo.')
            return
        gastos[idx] = nuevo
        guardar_csv()
        print('✔ Gasto modificado.')
    except ValueError:
        print('❌ Error: entradas numéricas inválidas.')


def eliminar_gasto():
    if not gastos:
        print('No hay gastos para eliminar.')
        return
    modo = input('Eliminar por valor (v) o por índice (i)? ').strip().lower()
    if modo == 'v':
        try:
            valor = float(input('Valor a eliminar (primera coincidencia): $'))
            gastos.remove(valor)
            guardar_csv()
            print('✔ Gasto eliminado por valor.')
        except ValueError:
            print('❌ No se encontró el valor o entrada inválida.')
    elif modo == 'i':
        try:
            idx = int(input('Índice a eliminar: '))
            if idx < 0 or idx >= len(gastos):
                print('❌ Índice fuera de rango.')
                return
            eliminado = gastos.pop(idx)
            guardar_csv()
            print(f'✔ Eliminado índice {idx}: ${eliminado:.2f}')
        except ValueError:
            print('❌ Índice inválido.')
    else:
        print('❌ Opción no válida.')


def ver_total():
    total = sum(gastos)
    print(f'Total de gastos: ${total:.2f}')


# --- Flujo principal ---
cargar_csv()

while True:
    print('\n--- MENÚ ---')
    print('1) Ver gastos')
    print('2) Agregar gasto')
    print('3) Modificar gasto (por índice)')
    print('4) Eliminar gasto (por valor o índice)')
    print('5) Ver total')
    print('6) Guardar ahora (CSV)')
    print('7) Cargar desde CSV')
    print('8) Salir')
    op = input('Elige una opción: ').strip()

    if op == '1':
        ver_gastos()
    elif op == '2':
        agregar_gasto()
    elif op == '3':
        modificar_gasto()
    elif op == '4':
        eliminar_gasto()
    elif op == '5':
        ver_total()
    elif op == '6':
        guardar_csv()
    elif op == '7':
        gastos.clear()
        cargar_csv()
    elif op == '8':
        print('Saliendo... ¡Hasta luego!')
        break
    else:
        print('Opción no válida. Intenta de nuevo.')
