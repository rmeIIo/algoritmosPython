jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador (ou "sair" para encerrar): ')
    if jogador['nome'] == 'sair':
        break
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    total_gols = 0
    for i in range(partidas):
        gols_partida = int(input(f'Quantos gols na partida {i+1}? '))
        gols.append(gols_partida)
        total_gols += gols_partida
    jogador['gols'] = gols
    jogador['total_gols'] = total_gols
    jogadores.append(jogador)

print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for i, jogador in enumerate(jogadores):
    print(f'{i:>3}', end='')
    for dado in jogador.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-'*60)

while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para sair): '))
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print(f'Erro! Não existe jogador com código {escolha}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["nome"]}:')
        for i, gols in enumerate(jogadores[escolha]['gols']):
            print(f'   No jogo {i+1} fez {gols} gols.')
print('<< ENCERRADO >>')
