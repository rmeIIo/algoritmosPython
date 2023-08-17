# Primeira nota: 7.5
# Segunda nota: 8
# Tirando 7.5 e 8.0, a média do aluno é 7.8
# O aluno está APROVADO!
# O aluno está em RECUPERAÇÂO!
# O aluno está REPROVADO!

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2

print(f'Tirando \033[34m{n1} \033[me \033[34m{n2}\033[m, a média do aluno é \033[34m{media:.1f}\033[m.')
if media >= 7.0:
    print('O aluno está \033[32mAPROVADO\033[m!')
elif media >= 5.0 <= 6.9:
    print('O aluno está em \033[33mRECUPERAÇÂO\033[m!')
elif media < 5.0:
    print('O aluno está \033[31mREPROVADO\033[m!')
