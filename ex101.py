def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade >= 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

ano_nascimento = int(input('Digite o ano de nascimento: '))
print(f'Para uma pessoa nascida em {ano_nascimento}, o voto é {voto(ano_nascimento)}')
