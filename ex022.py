nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem ao todo {len(nome.split()[0])}.')

