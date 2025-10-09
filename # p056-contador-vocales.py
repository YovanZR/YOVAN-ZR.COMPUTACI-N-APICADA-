# p056-contador-vocales.py
# Cuenta vocales, consonantes y otros caracteres en una frase (usa while).

while True:
    print('\033[H\033[J', end='')
    print("Contador de Vocales y Consonantes")
    print("-" * 35)

    frase = input("Introduce una frase: ").lower()

    vocales = 0
    consonantes = 0
    otros = 0
    i = 0

    while i < len(frase):
        ch = frase[i]
        if 'a' <= ch <= 'z':
            if ch in "aeiou":
                vocales += 1
            else:
                consonantes += 1
        else:
            otros += 1
        i += 1

    print("\nResultados:")
    print(f"Vocales: {vocales}")
    print(f"Consonantes: {consonantes}")
    print(f"No alfabéticos: {otros}")

    if input("\n¿Analizar otra frase (S/N)? ").strip().upper() == 'N':
        print("\nFin del programa. ¡Gracias!")
        break
