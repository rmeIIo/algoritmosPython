expressao = input('Digite a expressão: ')
abertos = []

for caractere in expressao:
    if caractere == '(':
        abertos.append((caractere))
    elif caractere == ')':
        if len(abertos) > 0:
            abertos.pop()
        else:
            abertos.append(caractere)

if len(abertos) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
