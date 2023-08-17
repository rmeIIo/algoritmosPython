aluno = {}
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input('Digite a média do aluno: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'

else:
    aluno['situacao'] = 'Reprovado'

print('Dados do aluno: ')
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'Situação: {aluno["situacao"]}')
