km = float(input('Qual é a distância da sua viagem? '))
p = km * 0.5
p1 = km * 0.45
if km <= 200:
    print(f'Você está prestes a começar uma viagem de {km:.2f}Km.')
    print(f'E o preço da sua passagem será de R${p:.2f}.')
else:
    print(f'Você está prestes a começar uma viagem de {km:.2f}Km')
    print(f'E o preço da sua passagem será de R${p1:.2f}.')
