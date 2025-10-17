# p091-iterar-lista.py
# Iterar por los elementos de una lista

print('\033[H\033[J')
print('Iterar por los elementos de una lista:\n')

nums = [2, 4, 6, 8, 10, 12, 14, 16]
print(f'Números a procesar: {nums}\n')

print('1. Iteración por elemento:')
for n in nums:
    print(n, end=' ')
print()

print('\n2. Iteración por índice:')
for i in range(len(nums)):
    print(nums[i], end=' ')
print()

print('\n3. Iteración por elemento para sumar 2 (sin modificar la lista):')
for n in nums:
    print(n + 2, end=' ')
print()

print('\n4. Iteración por índice para sumar 10 (modificando la lista):')
for i in range(len(nums)):
    nums[i] += 10
    print(nums[i], end=' ')
print()

print('\n\n5. Iteración con enumerate:')
print('Pos\tValor')
for i, n in enumerate(nums):
    print(f'{i}\t{n}')
