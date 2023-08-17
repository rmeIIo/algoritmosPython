pessoas = []
total_pessoas = 0
soma_idades = 0
mulheres = []
idade_acima_media = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexp [M/F]: ').upper()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)
    total_pessoas += 1
    soma_idades += pessoa['idade']

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa)

    continuar = input('Deseja continuar [S/N]? ').upper()
    if continuar == 'N':
        break

media_idade = soma_idades / total_pessoas

for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        idade_acima_media.append(pessoa)

print('-='*30)
print(f'A) Total de pessoas cadastradas: {total_pessoas}')
print(f'B) Média de idade: {media_idade:.2f} anos')
print('C) Lista de mulheres:')
for mulher in mulheres:
    print(f'    - {mulher["nome"]}, {mulher["idade"]} anos')
print('D) Lista de pessoas com idade acima da média: ')
for pessoa in idade_acima_media:
    print(f'     - {pessoa["nome"]}, {pessoa["idade"]} anos.')
