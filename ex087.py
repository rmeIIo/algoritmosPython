matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
maior_segunda_linha = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor para [{i}], [{j}]: '))
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
    if matriz[1][j] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][j]

    for i in range(3):
        for j in range(3):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()

print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')
