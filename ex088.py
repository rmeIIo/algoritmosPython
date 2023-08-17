import random
num_jogos = int(input('Quantos jogos você quer gerar? '))
jogos = []

for i in range(num_jogos):
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)

for jogo in jogos:
    print(jogo)
