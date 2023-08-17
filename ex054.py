import datetime
maior = 0
menor = 0
for pessoa in range(1, 8):
    ano = int(input((f'Em que ano a {pessoa}ª pessoa nasceu? ')))
    idade = datetime.date.today().year - ano
    if idade >= 18:
        maior = maior + 1
    elif idade < 18:
        menor = menor + 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade!')
print(f'E também tivemos {menor} pessoas menores de idade!')
