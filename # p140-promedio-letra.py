def calificacion_a_letra(prom: float)->tuple[str,str]:
    if 90<=prom<=100: return 'A','Excelente'
    elif 80<=prom<90: return 'B','Bien'
    elif 70<=prom<80: return 'C','Suficiente'
    elif 60<=prom<70: return 'D','Deficiente'
    elif 0<=prom<60: return 'F','Reprobado'
    else: return 'Calificación inválida',''

p=float(input('Promedio: '))
l,m=calificacion_a_letra(p)
print(l,m)
