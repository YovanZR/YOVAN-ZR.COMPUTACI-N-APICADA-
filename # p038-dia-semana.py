# p038-dia-semana.py
# Problema: Mostrar el día de la semana según número ingresado

dia = int(input("Ingresa un número del 1 al 7: "))

dias_semana = {
    1: "Domingo",
    2: "Lunes",
    3: "Martes",
    4: "Miércoles",
    5: "Jueves",
    6: "Viernes",
    7: "Sábado"
}

if dia in dias_semana:
    print(dias_semana[dia])
else:
    print("Error: Día inválido.")
