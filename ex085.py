numeros = [[], []]

for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        numeros[0].append((num))
    else:
        numeros[1].append((num))

numeros[0].sort()
numeros[1].sort()

print('Números pares: ', end='')
for num in numeros[0]:
    print(num, end=' ')
print()

print('Números ímpares: ', end='')
for num in numeros[1]:
    print(num, end=' ')
print()