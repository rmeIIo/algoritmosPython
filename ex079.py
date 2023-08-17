valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado.')
    opcao = str(input('Deseja continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
print('-='*30)
print(f'Os valores únicos digitados foram: {sorted(valores)}')
