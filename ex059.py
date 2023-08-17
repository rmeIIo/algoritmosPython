import time
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}.')
        print('=-'*15)
        time.sleep(2)
    if opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}.')
        print('=-' * 15)
        time.sleep(2)
    if opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2} o maior valor é {n1}.')
            print('=-' * 15)
            time.sleep(2)
        elif n2 > n1:
            maior = n2
            print(f'Entre {n1} e {n2} o maior valor é {n2}.')
            print('=-' * 15)
            time.sleep(2)
    if opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-' * 15)
        time.sleep(2)
    if opcao > 5:
        print('Opção inválida. Tente novamente...')
        print('=-' * 15)
        time.sleep(1)
    if opcao == 5:
        print('Finalizando...')
        print('=-' * 15)
        time.sleep(1)
