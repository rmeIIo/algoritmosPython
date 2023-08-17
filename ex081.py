numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-='*30)
print(f'Foram digitados {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'Lista de valores, ordenada de forma decrescente: {numeros}.')
if 5 in numeros:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado ou não está na lista.')
