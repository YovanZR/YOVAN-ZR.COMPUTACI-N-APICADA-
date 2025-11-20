def estacion_ano(mes: int) -> str:
    if mes in [12,1,2]: return "Invierno"
    elif mes in [3,4,5]: return "Primavera"
    elif mes in [6,7,8]: return "Verano"
    elif mes in [9,10,11]: return "Otoño"
    else: return "Mes inválido"

mes=int(input('Mes: '))
print(estacion_ano(mes))
