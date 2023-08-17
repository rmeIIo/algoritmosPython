def titulo(texto):
    """
    Função que imprime um título em destaque.
    :param texto: texto do título
    """
    print('\033[1;34m=\033[m' * 40)
    print(f'{texto.upper():^40}')
    print('\033[1;34m=\033[m' * 40)

titulo('Interactive Help')
while True:
    comando = input('\033[1;33mFunção ou Biblioteca: \033[44m').strip().lower()
    if comando == 'fim':
        break
    titulo(f'Acessando o manual do comando "{comando}"')
    print('\033[1;36m')
    help(comando)
    print('\033[m')
titulo('Até Logo!')
