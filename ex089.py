alunos = []

while True:
    nome = input('Digite o nome do aluno: ')
    if nome.lower() == 'sair':
        break
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    alunos.append([nome, nota1, nota2])

print('Boletim dos alunos: ')
for i, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{i+1}. {aluno[0]} - Média: {media:.2f}')

while True:
    opcao = input('Mostrar notas de qual aluno? (digite "sair" para encerrar): ')
    if opcao.lower() == 'sair':
        break
    try:
        indice = int(opcao) - 1
        aluno = alunos[indice]
        print(f'Notas de {aluno[0]}: {aluno[1]} e {aluno[2]}')
    except(ValueError, IndexError):
        print('Aluno não encontrado. Tente novamente.')
