def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            return valor

n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')

