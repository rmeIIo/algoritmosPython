numeros = []
pares = []
impares = []

while True:
    numeros.append((int(input('Digite um número: '))))
    if numeros[-1] % 2 == 0:
        pares.append(numeros[-1])
    else:
        impares.append(numeros[-1])
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-='*30)
print(f'Lista completa: {numeros}')
print(f'Lista de valores pares: {pares}')
print(f'Lista de valores ímpares: {impares}')
