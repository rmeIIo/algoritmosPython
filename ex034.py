sal = float(input('Qual é o salário do funcionário? R$'))
if sal > 1250:
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${sal+(sal*0.1):.2f} agora.')
else:
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${sal+(sal*0.15):.2f} agora.')
