pessoas = []

while True:
    nome = input('Digite o nome da pessoa (ou "sair" para encerrar): ')
    if nome.lower() == 'sair':
        break
    peso = float(input('Digite o peso da pessoa: '))
    pessoas.append((nome, peso))

print(f'Foram cadastradas {len(pessoas)} pessoas.')

pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])
print('Pessoas mais leves: ')
for pessoa in pessoas_ordenadas[:3]:
    print(f'{pessoa[0]} ({pessoa[1]}kg)')

pessoas_ordenadas.reverse()

print('Pessoas mais pesadas:')
for pessoa in pessoas_ordenadas[:3]:
    print(f'{pessoa[0]} ({pessoa[1]}kg)')
