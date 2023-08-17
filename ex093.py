jogador = {}
jogador['nome'] = input('Nome do jagador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
total_gols = 0

for i in range(partidas):
    gols_partida = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append((gols_partida))
    total_gols += gols_partida

jogador['gols'] = gols
jogador['total_gols'] = total_gols

print('-='*30)
print(jogador)
