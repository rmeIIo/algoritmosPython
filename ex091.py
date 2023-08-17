import random

jogadores = {}
for i in range(1, 5):
    jogador = input(f'Digite o nome do jogador {i}: ')
    jogada = random.randint(1, 6)
    jogadores[jogador] = jogada
print("Resultados: ")
for jogador, jogada in jogadores.items():
    print(f'{jogador}: {jogada}')

jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
print('Classificação final: ')
for i, (jogador, jogada) in enumerate(jogadores_ordenados):
    print(f'{i+1}º lugar: {jogador} com {jogada} pontos')
