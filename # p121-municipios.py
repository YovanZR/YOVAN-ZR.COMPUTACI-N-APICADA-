# p121-municipios.py
# Gestión de un padrón municipal usando conjuntos

municipios = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}
print('\033[H\033[J')
print('--- Gestión de Municipios (con Conjuntos) ---\n')
print(f'La colección es del tipo : {type(municipios)}')
print(f'Longitud del padrón : {len(municipios)}')
print(f'Padrón original : \n{municipios}\n')
print("Lista de municipios registrados:")
for mun in municipios:
    print(mun, end=' | ')
print(f'\n\n¿Está Zacatecas en el padrón?: {"Zacatecas" in municipios}')
print('\n--- Altas en el Padrón ---')
municipios.add("Teul")
print(f'Alta con Add() (Teul): \n{municipios}\n')
otros_municipios = {"Luis Moya", "Ojocaliente", "Tepetongo"}
municipios.update(otros_municipios)
print(f'Alta con Update() (varios): \n{municipios}\n')
print("\n--- Bajas del Padrón ---")
municipios.remove('Zacatecas')
print(f'Baja con Remove() (Zacatecas): \n{municipios}\n')
municipios.discard("Ojocaliente")
print(f'Baja con Discard() (Ojocaliente): \n{municipios}\n')
mun_eliminado = municipios.pop()
print(f'Baja con Pop() (elemento arbitrario): \n{municipios} \nEliminado: {mun_eliminado}\n')
municipios.clear()
print(f'Padrón vaciado con Clear(): \n{municipios}\n')
