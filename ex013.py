salario = float(input('Qual é o salário do funcionário? R$'))
reajuste = float(salario + (salario * 0.15))
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${reajuste:.2f}.')
