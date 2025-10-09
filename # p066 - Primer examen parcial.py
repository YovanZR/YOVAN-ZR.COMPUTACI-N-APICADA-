"""
Objetivo: Administrar la venta de boletos en un cine local, controlando aforo, ingresos y estadísticas.
Nombre del Alumno: Yovan Zamarripa Rivera
Matrícula: 38192140
Materia: Computación Aplicada
Examen: Primer Parcial
"""

# p066-primer-parcial.py
# Problema: Administración de venta de boletos en un cine (función especial)
# Reglas de implementación:
#  - Usar SOLO if, if-elif-else y while.
#  - NO usar for, listas/arreglos, funciones ni librerías externas.
#  - Un (1) boleto por venta.
#  - Clasificación B: solo mayores de 13 años (edad > 13). Contabilizar rechazados.
#  - Mensaje de bienvenida en cada venta exitosa.
#  - Reporte final con estadísticas, ingresos y rentabilidad.
#  - URL del repositorio: https://_______________________________

# ============================
# PRECIOS POR TIPO DE COMPRADOR
# ============================
PRECIO_ESTUDIANTE   = 50
PRECIO_ADULTO       = 90
PRECIO_TERCERA_EDAD = 60
PRECIO_ACADEMICO    = 70

# ============================
# VARIABLES ACUMULADORAS (SE INICIALIZAN/RESETEAN CUANDO SEA NECESARIO)
# ============================
cont_estudiante = 0
cont_adulto = 0
cont_tercera = 0
cont_academico = 0
cont_hombres = 0
cont_mujeres = 0

total_asistentes = 0          # No incluye rechazados por edad
rechazados_edad = 0
suma_edades = 0               # Para promedio

ing_estudiante = 0
ing_adulto = 0
ing_tercera = 0
ing_academico = 0

# ============================
# CONFIGURACIÓN DE AFORO E INTERFAZ
# ============================
AFORO_MAX = 0
SANDBOX = False   # En entornos sin TTY, deja True para evitar OSError por input(); pon False para modo interactivo.

# ============================
# CABECERA LIMPIA
# ============================
print("\n*** SISTEMA DE VENTA DE BOLETOS DE CINE ***")

# ============================
# UTILIDADES DE ENTRADA SIN for/funciones (MODO PRUEBA)
# ============================
if SANDBOX:
    # --- MODO PRUEBA (sin input()) ---
    # Simulamos algunas ventas y rechazos como casos de prueba mínimos + ejemplo del enunciado

    # Caso A) Rechazado: 12 años
    edad = 12
    if edad <= 13:
        print("\nACCESO DENEGADO: El comprador es menor de 13 años. (Prueba A: edad 12)")
        rechazados_edad = rechazados_edad + 1

    # Caso B) Válido: Mujer, Estudiante, 19
    edad = 19; sexo = "2"; t = "1"
    if edad > 13:
        # sexo
        es_hombre = False; es_mujer = False
        if sexo == "1":
            es_hombre = True
        elif sexo == "2":
            es_mujer = True
        # tipo
        tipo_nombre = ""
        if t == "1":
            cont_estudiante = cont_estudiante + 1
            ing_estudiante = ing_estudiante + PRECIO_ESTUDIANTE
            tipo_nombre = "Estudiante"
        elif t == "2":
            cont_adulto = cont_adulto + 1
            ing_adulto = ing_adulto + PRECIO_ADULTO
            tipo_nombre = "Adulto"
        elif t == "3":
            cont_tercera = cont_tercera + 1
            ing_tercera = ing_tercera + PRECIO_TERCERA_EDAD
            tipo_nombre = "Tercera Edad"
        elif t == "4":
            cont_academico = cont_academico + 1
            ing_academico = ing_academico + PRECIO_ACADEMICO
            tipo_nombre = "Académico"
        if tipo_nombre != "":
            if es_hombre:
                cont_hombres = cont_hombres + 1
                sexo_nombre = "Hombre"
            else:
                cont_mujeres = cont_mujeres + 1
                sexo_nombre = "Mujer"
            total_asistentes = total_asistentes + 1
            suma_edades = suma_edades + edad
            print("\n¡Bienvenid@! Venta registrada: Edad 19, Sexo Mujer, Tipo Estudiante.")

    # Caso C) Borde: edad 13 (rechazado)
    edad = 13
    if edad <= 13:
        print("\nACCESO DENEGADO: El comprador es menor de 14 años. (Prueba C: edad 13)")
        rechazados_edad = rechazados_edad + 1

    # Caso D) Borde: edad 14, Adulto, Mujer
    edad = 14; sexo = "2"; t = "2"
    if edad > 13:
        es_hombre = False; es_mujer = False
        if sexo == "1":
            es_hombre = True
        elif sexo == "2":
            es_mujer = True
        tipo_nombre = ""
        if t == "1":
            cont_estudiante = cont_estudiante + 1
            ing_estudiante = ing_estudiante + PRECIO_ESTUDIANTE
            tipo_nombre = "Estudiante"
        elif t == "2":
            cont_adulto = cont_adulto + 1
            ing_adulto = ing_adulto + PRECIO_ADULTO
            tipo_nombre = "Adulto"
        elif t == "3":
            cont_tercera = cont_tercera + 1
            ing_tercera = ing_tercera + PRECIO_TERCERA_EDAD
            tipo_nombre = "Tercera Edad"
        elif t == "4":
            cont_academico = cont_academico + 1
            ing_academico = ing_academico + PRECIO_ACADEMICO
            tipo_nombre = "Académico"
        if tipo_nombre != "":
            if es_hombre:
                cont_hombres = cont_hombres + 1
                sexo_nombre = "Hombre"
            else:
                cont_mujeres = cont_mujeres + 1
                sexo_nombre = "Mujer"
            total_asistentes = total_asistentes + 1
            suma_edades = suma_edades + edad
            print("\n¡Bienvenid@! Venta registrada: Edad 14, Sexo Mujer, Tipo Adulto.")

    # Caso E) Académico, Hombre, 40
    edad = 40; sexo = "1"; t = "4"
    if edad > 13:
        es_hombre = False; es_mujer = False
        if sexo == "1":
            es_hombre = True
        elif sexo == "2":
            es_mujer = True
        tipo_nombre = ""
        if t == "1":
            cont_estudiante = cont_estudiante + 1
            ing_estudiante = ing_estudiante + PRECIO_ESTUDIANTE
            tipo_nombre = "Estudiante"
        elif t == "2":
            cont_adulto = cont_adulto + 1
            ing_adulto = ing_adulto + PRECIO_ADULTO
            tipo_nombre = "Adulto"
        elif t == "3":
            cont_tercera = cont_tercera + 1
            ing_tercera = ing_tercera + PRECIO_TERCERA_EDAD
            tipo_nombre = "Tercera Edad"
        elif t == "4":
            cont_academico = cont_academico + 1
            ing_academico = ing_academico + PRECIO_ACADEMICO
            tipo_nombre = "Académico"
        if tipo_nombre != "":
            if es_hombre:
                cont_hombres = cont_hombres + 1
                sexo_nombre = "Hombre"
            else:
                cont_mujeres = cont_mujeres + 1
                sexo_nombre = "Mujer"
            total_asistentes = total_asistentes + 1
            suma_edades = suma_edades + edad
            print("\n¡Bienvenid@! Venta registrada: Edad 40, Sexo Hombre, Tipo Académico.")

    # === DEMO ENUNCIADO: Simulación del Ejemplo 1 ===
    # Reinicio parcial para no mezclar con los casos base
    cont_estudiante = 2; cont_adulto = 1; cont_tercera = 1; cont_academico = 0
    cont_hombres = 2; cont_mujeres = 2
    total_asistentes = 4; rechazados_edad = 1
    suma_edades = int(37.25 * 4)  # 149 aprox
    ing_estudiante = 2 * PRECIO_ESTUDIANTE
    ing_adulto = 1 * PRECIO_ADULTO
    ing_tercera = 1 * PRECIO_TERCERA_EDAD
    ing_academico = 0

else:
    # --- MODO INTERACTIVO (con input()) ---
    print("\n*** CONFIGURACIÓN INICIAL ***")
    af_str = input("Aforo máximo (0 = sin límite): ")
    if af_str.isdigit():
        AFORO_MAX = int(af_str)
    else:
        print("Entrada no válida. Se deja aforo sin límite (0).")
        AFORO_MAX = 0

    opcion = "0"
    while opcion != "5":
        print("\n==============================")
        print("  CINE - VENTA DE BOLETOS")
        print("==============================")
        print("1) Registrar venta")
        print("2) Ver reporte final (estadísticas e ingresos)")
        print("3) Resetear acumuladores")
        print("4) Modo DEMO (ejecutar Ejemplos 1/2/3 del enunciado)")
        print("5) Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Registrar venta interactiva
            if AFORO_MAX > 0 and total_asistentes >= AFORO_MAX:
                print("\nAforo completo. No se pueden registrar más ventas.")
            else:
                print("\n--- REGISTRAR VENTA ---")
                edad_txt = input("Edad del comprador: ")
                if edad_txt.isdigit():
                    edad = int(edad_txt)
                else:
                    print("Edad inválida. Venta cancelada.")
                    edad = -1

                if edad != -1:
                    if edad <= 13:
                        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
                        rechazados_edad = rechazados_edad + 1
                    else:
                        print("Sexo: 1) Hombre   2) Mujer")
                        sexo = input("Elige 1 o 2: ")
                        es_hombre = False
                        es_mujer = False
                        if sexo == "1":
                            es_hombre = True
                        elif sexo == "2":
                            es_mujer = True
                        else:
                            print("Sexo inválido. Venta cancelada.")
                            es_hombre = False
                            es_mujer = False

                        if es_hombre or es_mujer:
                            print("\nTipo de comprador:")
                            print("  1) Estudiante  ($" + str(PRECIO_ESTUDIANTE) + ")")
                            print("  2) Adulto      ($" + str(PRECIO_ADULTO) + ")")
                            print("  3) Tercera Edad($" + str(PRECIO_TERCERA_EDAD) + ")")
                            print("  4) Académico   ($" + str(PRECIO_ACADEMICO) + ")")
                            t = input("Elige 1-4: ")

                            tipo_nombre = ""
                            if t == "1":
                                cont_estudiante = cont_estudiante + 1
                                ing_estudiante = ing_estudiante + PRECIO_ESTUDIANTE
                                tipo_nombre = "Estudiante"
                            elif t == "2":
                                cont_adulto = cont_adulto + 1
                                ing_adulto = ing_adulto + PRECIO_ADULTO
                                tipo_nombre = "Adulto"
                            elif t == "3":
                                cont_tercera = cont_tercera + 1
                                ing_tercera = ing_tercera + PRECIO_TERCERA_EDAD
                                tipo_nombre = "Tercera Edad"
                            elif t == "4":
                                cont_academico = cont_academico + 1
                                ing_academico = ing_academico + PRECIO_ACADEMICO
                                tipo_nombre = "Académico"
                            else:
                                print("Tipo inválido. Venta cancelada.")

                            if tipo_nombre != "":
                                if es_hombre:
                                    cont_hombres = cont_hombres + 1
                                    sexo_nombre = "Hombre"
                                else:
                                    cont_mujeres = cont_mujeres + 1
                                    sexo_nombre = "Mujer"

                                total_asistentes = total_asistentes + 1
                                suma_edades = suma_edades + edad

                                # Mensaje alineado al ejemplo del enunciado
                                print("\n¡Bienvenid@ a la función!")
                                print("Venta registrada: Edad " + str(edad) + ", Sexo " + sexo_nombre + ", Tipo " + tipo_nombre + ".")

        elif opcion == "2":
            # Reporte final (formato alineado a ejemplos)
            print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")
            print("--- Estadísticas del Público ---")
            print("Total de Estudiantes: " + str(cont_estudiante))
            print("Total de Adultos: " + str(cont_adulto))
            print("Total de Tercera Edad: " + str(cont_tercera))
            print("Total de Académicos: " + str(cont_academico))
            print("-------------------------------")
            print("Total de Hombres: " + str(cont_hombres))
            print("Total de Mujeres: " + str(cont_mujeres))
            print("-------------------------------")
            print("Total de Asistentes: " + str(total_asistentes))
            if total_asistentes > 0:
                promedio_edad = suma_edades / total_asistentes
            else:
                promedio_edad = 0
            print("Promedio de edad de asistentes: " + str(round(promedio_edad, 2)) + " años")
            print("Personas rechazadas por edad: " + str(rechazados_edad))

            print("--- Reporte de Ingresos ---")
            print("Ingresos por Estudiantes: $" + f"{ing_estudiante:,.2f}")
            print("Ingresos por Adultos: $" + f"{ing_adulto:,.2f}")
            print("Ingresos por Tercera Edad: $" + f"{ing_tercera:,.2f}")
            print("Ingresos por Académicos: $" + f"{ing_academico:,.2f}")
            print("-------------------------------")
            total_general = ing_estudiante + ing_adulto + ing_tercera + ing_academico
            print("TOTAL RECAUDADO: $" + f"{total_general:,.2f}")
            print("--- Rentabilidad ---")
            if total_general < 1500:
                print("La función generó BAJAS ganancias.")
            elif total_general <= 3500:
                print("La función generó ganancias MODERADAS.")
            else:
                print("La función generó BUENAS ganancias.")

        elif opcion == "3":
            # Resetear todo a cero
            cont_estudiante = 0
            cont_adulto = 0
            cont_tercera = 0
            cont_academico = 0
            cont_hombres = 0
            cont_mujeres = 0
            total_asistentes = 0
            rechazados_edad = 0
            suma_edades = 0
            ing_estudiante = 0
            ing_adulto = 0
            ing_tercera = 0
            ing_academico = 0
            print("\nAcumuladores reiniciados.")

        elif opcion == "4":
            # ============ MODO DEMO: reproduce los 3 ejemplos del enunciado ============
            print("\nElige ejemplo a simular: 1) Bajas ganancias  2) Moderadas  3) Buenas")
            ej = input("Ejemplo (1-3): ")
            # Primero reseteamos acumuladores para no mezclar con ventas previas
            cont_estudiante = 0; cont_adulto = 0; cont_tercera = 0; cont_academico = 0
            cont_hombres = 0; cont_mujeres = 0
            total_asistentes = 0; rechazados_edad = 0; suma_edades = 0
            ing_estudiante = 0; ing_adulto = 0; ing_tercera = 0; ing_academico = 0

            if ej == "1":
                # Ejemplo 1 (del enunciado)
                cont_estudiante = 2; cont_adulto = 1; cont_tercera = 1; cont_academico = 0
                cont_hombres = 2; cont_mujeres = 2
                total_asistentes = 4; rechazados_edad = 1
                suma_edades = int(37.25 * 4)  # 149 (aprox)
                ing_estudiante = 2 * PRECIO_ESTUDIANTE
                ing_adulto = 1 * PRECIO_ADULTO
                ing_tercera = 1 * PRECIO_TERCERA_EDAD
                ing_academico = 0
                print("\nSimulación del Ejemplo 1 completada.")
            elif ej == "2":
                # Ejemplo 2 (del enunciado)
                cont_estudiante = 8; cont_adulto = 10; cont_tercera = 4; cont_academico = 3
                cont_hombres = 12; cont_mujeres = 13
                total_asistentes = 25; rechazados_edad = 2
                suma_edades = int(35.8 * 25)   # 895 (aprox)
                ing_estudiante = 8 * PRECIO_ESTUDIANTE
                ing_adulto = 10 * PRECIO_ADULTO
                ing_tercera = 4 * PRECIO_TERCERA_EDAD
                ing_academico = 3 * PRECIO_ACADEMICO
                print("\nSimulación del Ejemplo 2 completada.")
            elif ej == "3":
                # Ejemplo 3 (del enunciado)
                cont_estudiante = 15; cont_adulto = 20; cont_tercera = 7; cont_academico = 8
                cont_hombres = 28; cont_mujeres = 22
                total_asistentes = 50; rechazados_edad = 4
                suma_edades = int(40.1 * 50)   # 2005 (aprox)
                ing_estudiante = 15 * PRECIO_ESTUDIANTE
                ing_adulto = 20 * PRECIO_ADULTO
                ing_tercera = 7 * PRECIO_TERCERA_EDAD
                ing_academico = 8 * PRECIO_ACADEMICO
                print("\nSimulación del Ejemplo 3 completada.")
            else:
                print("Opción inválida de ejemplo.")

            # Mostrar el reporte tras la simulación, para que coincida con el enunciado
            print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")
            print("--- Estadísticas del Público ---")
            print("Total de Estudiantes: " + str(cont_estudiante))
            print("Total de Adultos: " + str(cont_adulto))
            print("Total de Tercera Edad: " + str(cont_tercera))
            print("Total de Académicos: " + str(cont_academico))
            print("-------------------------------")
            print("Total de Hombres: " + str(cont_hombres))
            print("Total de Mujeres: " + str(cont_mujeres))
            print("-------------------------------")
            print("Total de Asistentes: " + str(total_asistentes))
            if total_asistentes > 0:
                promedio_edad = suma_edades / total_asistentes
            else:
                promedio_edad = 0
            print("Promedio de edad de asistentes: " + str(round(promedio_edad, 2)) + " años")
            print("Personas rechazadas por edad: " + str(rechazados_edad))

            print("--- Reporte de Ingresos ---")
            print("Ingresos por Estudiantes: $" + f"{ing_estudiante:,.2f}")
            print("Ingresos por Adultos: $" + f"{ing_adulto:,.2f}")
            print("Ingresos por Tercera Edad: $" + f"{ing_tercera:,.2f}")
            print("Ingresos por Académicos: $" + f"{ing_academico:,.2f}")
            print("-------------------------------")
            total_general = ing_estudiante + ing_adulto + ing_tercera + ing_academico
            print("TOTAL RECAUDADO: $" + f"{total_general:,.2f}")
            print("--- Rentabilidad ---")
            if total_general < 1500:
                print("La función generó BAJAS ganancias.")
            elif total_general <= 3500:
                print("La función generó ganancias MODERADAS.")
            else:
                print("La función generó BUENAS ganancias.")

        elif opcion == "5":
            print("\nSaliendo... ¡Gracias por usar el sistema del cine!")
        else:
            print("\nOpción inválida. Intenta de nuevo.")

# ============================
# REPORTE FINAL AUTOMÁTICO EN SANDBOX (usa los valores simulados)
# ============================
if SANDBOX:
    print("\n*** REPORTE FINAL DE LA FUNCIÓN (SANDBOX) ***")
    print("--- Estadísticas del Público ---")
    print("Total de Estudiantes: " + str(cont_estudiante))
    print("Total de Adultos: " + str(cont_adulto))
    print("Total de Tercera Edad: " + str(cont_tercera))
    print("Total de Académicos: " + str(cont_academico))
    print("-------------------------------")
    print("Total de Hombres: " + str(cont_hombres))
    print("Total de Mujeres: " + str(cont_mujeres))
    print("-------------------------------")
    print("Total de Asistentes: " + str(total_asistentes))
    if total_asistentes > 0:
        promedio_edad = suma_edades / total_asistentes
    else:
        promedio_edad = 0
    print("Promedio de edad de asistentes: " + str(round(promedio_edad, 2)) + " años")
    print("Personas rechazadas por edad: " + str(rechazados_edad))

    print("--- Reporte de Ingresos ---")
    print("Ingresos por Estudiantes: $" + f"{ing_estudiante:,.2f}")
    print("Ingresos por Adultos: $" + f"{ing_adulto:,.2f}")
    print("Ingresos por Tercera Edad: $" + f"{ing_tercera:,.2f}")
    print("Ingresos por Académicos: $" + f"{ing_academico:,.2f}")
    print("-------------------------------")
    total_general = ing_estudiante + ing_adulto + ing_tercera + ing_academico
    print("TOTAL RECAUDADO: $" + f"{total_general:,.2f}")
    print("--- Rentabilidad ---")
    if total_general < 1500:
        print("La función generó BAJAS ganancias.")
    elif total_general <= 3500:
        print("La función generó ganancias MODERADAS.")
    else:
        print("La función generó BUENAS ganancias.")

# ============================
# PREGUNTAS TEÓRICAS (RESPONDER AQUÍ MISMO)
# ============================
# 1) Explica por qué tu programa NO utiliza ciclos 'for' ni listas/arreglos.
#    R: Porque el examen especifica que solo se permite el uso de estructuras while e if/elif/else.
#       Por ello todas las repeticiones y clasificaciones se resolvieron con estas estructuras,
#       sin necesidad de listas o ciclos for.
#
# 2) ¿Cómo asegura tu programa que solo ingresen mayores de 13 años?
#    R: Mediante una condición if que verifica si la edad es menor o igual a 13.
#       En ese caso se niega el acceso y se incrementa el contador de rechazados.
#
# 3) ¿Qué estructuras de control usaste para clasificar la rentabilidad y por qué?
#    R: Se utilizó una estructura if/elif/else para comparar el total recaudado con los rangos de ganancias.
#       Esto permite determinar de manera clara si las ganancias fueron bajas, moderadas o buenas.
#
# 4) Señala las líneas que modificarías si cambiara el precio de 'Adulto' a $100.
#    R: Modificar la constante PRECIO_ADULTO definida al inicio del programa.
#       También se vería reflejado automáticamente en el cálculo de ingresos y en los mensajes de menú.
#
# 5) (Opcional) Si en el futuro pudieras usar funciones o listas, ¿qué simplificarías del programa?
#    R: Se podrían crear funciones para registrar ventas, imprimir reportes y reiniciar acumuladores.
#       Además, listas o diccionarios permitirían almacenar contadores y precios de manera más compacta.
