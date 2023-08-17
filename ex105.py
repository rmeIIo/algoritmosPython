def notas(*notas, situacao=False):
    dic_notas = {}
    dic_notas['Quantidade de notas'] = len(notas)
    dic_notas['Maior nota'] = max(notas)
    dic_notas['Menor nota'] = min(notas)
    dic_notas['Média da turma'] = sum(notas) / len(notas)
    if situacao:
        if dic_notas['Média da turma'] >= 7:
            dic_notas['Situação'] = 'APROVADO'
        elif dic_notas['Média da turma'] >= 5:
            dic_notas['Situação'] = 'RECUPERAÇÃO'
        else:
            dic_notas['Situação'] = 'REPROVADO'
    return dic_notas

notas_alunos = notas(8, 9, 7, 6, 5, 10, situacao=True)
print(notas_alunos)
