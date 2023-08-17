v = float(input('Qual é a velocidade atual do carro?'))
if v <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${7*(v-80):.2f}.')
    print('Tenha um bom dia! Dirija com segurança!')
