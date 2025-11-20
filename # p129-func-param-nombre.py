def saluda(apaterno: str, amaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}')

saluda('Lopez', 'Martinez', 'Ana')
saluda(nombre='Ana', amaterno='Martinez', apaterno='Lopez')
