# p075-cifrado-cesar.py
while True:
    mensaje_original = input("Ingresa el mensaje a encriptar: ")
    desplazamiento = int(input("Ingresa la clave de desplazamiento: "))
    mensaje_cifrado = ""
    for caracter in mensaje_original:
        if caracter.isalpha():
            codigo_ascii = ord(caracter)
            base = ord('a') if caracter.islower() else ord('A')
            codigo_nuevo = base + (codigo_ascii - base + desplazamiento) % 26
            mensaje_cifrado += chr(codigo_nuevo)
        else:
            mensaje_cifrado += caracter
    print(f"Mensaje Original: {mensaje_original}")
    print(f"Mensaje Cifrado: {mensaje_cifrado}")
    if input('¿Deseas encriptar otro mensaje (S/N)? ').upper() == 'N':
        break
