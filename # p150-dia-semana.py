# p150-dia-semana.py
# Recibe un número entre 1 y 7 y regresa el día de la semana correspondiente.

from typing import Optional

def dia_semana(numero: int) -> Optional[str]:
    """Regresa el nombre del día de la semana para un número entre 1 y 7.
    Si el número no está en el rango, regresa None.
    """
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo",
    }
    return dias.get(numero)

def main() -> None:
    numero = int(input("Introduce un número del 1 al 7: "))
    dia = dia_semana(numero)
    if dia is None:
        print("Error: El número debe estar entre 1 y 7.")
    else:
        print(f"El día es: {dia}")

if __name__ == "__main__":
    main()
