matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

print('Matriz: ')
for linha in matriz:
    for valor in linha:
        print(f'{valor:^5}', end='')
    print()