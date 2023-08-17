times = ('Palmeiras', 'Atlética-MG', 'Fortaleza', 'Bragantino', 'Athletico-PR', 'Flamengo', 'Ceará', 'Santos', 'Atlético-GO', 'Corinthians', 'Internacional', 'Juventude', 'São Paulo', 'Fluminense', 'Sport', 'América-MG', 'Cuiabá', 'Grêmio', 'Bahia', 'Chapecoense')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
posicao = times.index('Chapecoense') + 1
print(f'Chapecoense está na posição {posicao}')
