# Ano de nascimento: 2001
# Quem nasceu em 2001 tem 16 anos em 2017.
# Ainda faltam 2 anos para o alistamento.
# Seu alistamento será em 2019.

import datetime
nasc = int(input('Ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - nasc
alistamento = 18
print(f'Quem nasceu em {nasc} tem {idade} anos em {datetime.date.today().year}.')
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para seu alistamento.')
    print(f'Seu alistamento será {atual + saldo}')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi {atual - saldo}.')
