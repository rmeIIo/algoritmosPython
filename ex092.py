from datetime import date

pessoa = {}
pessoa['nome'] = input('Digite o nome: ')
ano_nascimento = int(input('Digite o ano de nascimento: '))
pessoa['idade'] = date.today().year - ano_nascimento
pessoa['ctps'] = int(input('Digite o número da CTPS (0 se não tiver): '))

if pessoa['ctps']!= 0:
    pessoa['ano contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite o salário: '))
    anos_contribuicao = date.today().year - pessoa['ano contratação']
    idade_aposentadoria = 35 + anos_contribuicao
    pessoa['aposentadoria'] = pessoa['idade'] + idade_aposentadoria

print('-='*30)
for chave, valor in pessoa.items():
    print(f'{chave.capitalize()}: {valor}')
