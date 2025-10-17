# p090-eliminar-lista.py
# Eliminar elementos de una lista

print('\033[H\033[J')
print('Eliminar elementos de una lista:\n')

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f'Datos originales con anomalías: {nums}\n')

print('Eliminar la primera ocurrencia del valor 99:')
nums.remove(99)  # Si no existiera, lanzaría ValueError
print(f'Resultado : {nums}\n')

print('Eliminar el elemento en la posición 8:')
num_removido = nums.pop(8)  # guarda el eliminado
print(f'Resultado : Removido ({num_removido}), {nums}\n')

print('Eliminar el último elemento:')
ultimo_num = nums.pop()
print(f'Resultado: Removido ({ultimo_num}): {nums}\n')

print('Eliminar todos los elementos de la lista:')
nums.clear()
print(f'Resultado: {nums}\n')
