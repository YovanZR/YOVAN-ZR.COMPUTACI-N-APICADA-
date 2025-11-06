# p125-segundo-sxamen-parcial.py
# ------------------------------------------------------------
# TecnoTienda - Sistema de Inventario
# Captura productos en una lista de diccionarios y al final:
#  1) Imprime los datos crudos (lista de diccionarios)
#  2) Muestra una tabla alineada con las columnas pedidas
#  3) Presenta un resumen (totales, conteos, sumas, promedios, min/máx)
#
# NOTAS DE IMPLEMENTACIÓN / DOCUMENTACIÓN:
# - Se usa un bucle while para capturar N productos hasta que el usuario
#   deje el nombre vacío o escriba '*'.
# - Cada producto es un diccionario con claves: nombre, precio, categoria, proveedor, stock.
# - Se validan entradas numéricas (precio >= 0, stock entero >= 0).
# - Para la salida tabular se calculan anchos de columna dinámicos
#   en función de los datos capturados.
# - Los precios se formatean con separadores de miles y 2 decimales.
# - El resumen incluye:
#   * total de productos
#   * conteos por categoría y por proveedor
#   * suma y promedio de stock
#   * suma y promedio de precios (un precio por producto)
#   * producto más caro y más barato
# ------------------------------------------------------------

from pprint import pprint

def pedir_texto(prompt: str, permitir_vacio: bool = False) -> str:
    """Pide un texto; si permitir_vacio=False reintenta hasta que no esté vacío."""
    while True:
        txt = input(prompt).strip()
        if txt or permitir_vacio:
            return txt
        print("  · Entrada vacía. Intenta de nuevo.")

def pedir_float_no_negativo(prompt: str) -> float:
    """Pide un número flotante >= 0. Reintenta en caso de error o valor negativo."""
    while True:
        s = input(prompt).strip()
        try:
            val = float(s)
            if val < 0:
                print("  · Debe ser un número >= 0.")
                continue
            return val
        except ValueError:
            print("  · Entrada inválida. Escribe un número (ej. 1500.50).")

def pedir_int_no_negativo(prompt: str) -> int:
    """Pide un entero >= 0. Reintenta en caso de error o valor negativo."""
    while True:
        s = input(prompt).strip()
        try:
            val = int(s)
            if val < 0:
                print("  · Debe ser un entero >= 0.")
                continue
            return val
        except ValueError:
            print("  · Entrada inválida. Escribe un entero (ej. 25).")

def dinero(x: float) -> str:
    """Formatea un número como dinero con separador de miles y 2 decimales."""
    return f"{x:,.2f}"

def construir_tabla(productos: list) -> None:
    """Imprime una tabla con columnas: Nombre, Precio, Categoría, Stock, Proveedor."""
    # Convertimos a cadenas ya formateadas para calcular anchos
    filas = []
    for p in productos:
        fila = {
            "Nombre": p["nombre"],
            "Precio": dinero(p["precio"]),
            "Categoría": p["categoria"],
            "Stock": str(p["stock"]),
            "Proveedor": p["proveedor"],
        }
        filas.append(fila)

    # Encabezados
    headers = ["Nombre", "Precio", "Categoría", "Stock", "Proveedor"]

    # Cálculo de anchos dinámicos por columna
    anchos = {}
    for h in headers:
        max_data = max((len(f[h]) for f in filas), default=0)
        anchos[h] = max(len(h), max_data)

    # Ensamblado de formatos (alinear: nombre/categoría/proveedor a la izq,
    # precio y stock a la derecha para mejor lectura numérica)
    fmt = (
        f"{{Nombre:<{anchos['Nombre']}}}  "
        f"{{Precio:>{anchos['Precio']}}}  "
        f"{{Categoría:<{anchos['Categoría']}}}  "
        f"{{Stock:>{anchos['Stock']}}}  "
        f"{{Proveedor:<{anchos['Proveedor']}}}"
    )

    # Línea de encabezado
    header_line = (
        f"{'Nombre':<{anchos['Nombre']}}  "
        f"{'Precio':>{anchos['Precio']}}  "
        f"{'Categoría':<{anchos['Categoría']}}  "
        f"{'Stock':>{anchos['Stock']}}  "
        f"{'Proveedor':<{anchos['Proveedor']}}"
    )
    print(header_line)
    print("-" * len(header_line))

    # Filas
    for f in filas:
        print(fmt.format(**f))

def conteos_por_clave(productos: list, clave: str) -> dict:
    """Regresa un dict con conteos por valor de la clave especificada (ej. 'categoria')."""
    conteos = {}
    for p in productos:
        k = p[clave]
        conteos[k] = conteos.get(k, 0) + 1
    return conteos

def imprimir_conteos_titulados(titulo: str, conteos: dict) -> None:
    """Imprime conteos con viñetas, ordenados alfabéticamente por clave."""
    print(titulo)
    for k in sorted(conteos.keys()):
        print(f"• {k}: {conteos[k]}")

def main():
    print("TecnoTienda - Sistema de Inventario")
    print("Captura de datos de los productos (deja el nombre vacío o escribe * para terminar):")

    productos = []

    while True:
        nombre = pedir_texto("Nombre del producto: ", permitir_vacio=True)
        if not nombre or nombre == "*":
            break  # fin de captura

        precio = pedir_float_no_negativo("Precio (ej. 1500.50): ")
        categoria = pedir_texto("Categoría (ej. Laptops, Celulares, Audio): ")
        proveedor = pedir_texto("Proveedor (ej. Sony, HP, Generico): ")
        stock = pedir_int_no_negativo("Stock (ej. 25): ")

        # Construimos el diccionario del producto y lo agregamos a la lista
        producto = {
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria,
            "proveedor": proveedor,
            "stock": stock
        }
        productos.append(producto)
        print("· Producto registrado.\n")

    print("\n3.1. DATOS (LISTA DE DICCIONARIOS):")
    if not productos:
        print("No se capturaron productos.")
        return

    # Datos crudos:
    pprint(productos, width=100)

    # Tabla
    print("\n3.2. TABLA DE DATOS:")
    construir_tabla(productos)

    # Resumen
    print("\n3. RESUMEN:")
    total = len(productos)
    print(f"Productos totales: {total}")

    # Conteos por categoría y por proveedor
    cat_counts = conteos_por_clave(productos, "categoria")
    prov_counts = conteos_por_clave(productos, "proveedor")
    imprimir_conteos_titulados("Categorías:", cat_counts)
    imprimir_conteos_titulados("Proveedores:", prov_counts)

    # Sumas y promedios
    suma_stock = sum(p["stock"] for p in productos)
    prom_stock = suma_stock / total if total > 0 else 0.0

    suma_precios = sum(p["precio"] for p in productos)
    prom_precios = suma_precios / total if total > 0 else 0.0

    print(f"Stock -> Suma: {suma_stock:,}, Promedio: {prom_stock:.1f}")
    print(f"Precio -> Suma: {dinero(suma_precios)}, Promedio: {dinero(prom_precios)}")

    # Producto más caro y más barato
    mas_caro = max(productos, key=lambda p: p["precio"])
    mas_barato = min(productos, key=lambda p: p["precio"])
    print(
        f"{mas_caro['nombre']} de {dinero(mas_caro['precio'])} es el más caro, "
        f"{mas_barato['nombre']} de {dinero(mas_barato['precio'])} es el más barato."
    )

if __name__ == "__main__":
    main()
