# Ano de nascimento:
# O atleta tem X anos.
# Classificação: JUNIOR.

import datetime
ano = int(input('Ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade < 14:
    print('Classificação: INFANTIL.')
elif idade < 19:
    print('Classificação: JUNIOR.')
elif idade < 26:
    print('Classificação: SÊNIOR.')
elif idade > 25:
    print('Classificação: MASTER.')