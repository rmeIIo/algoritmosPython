# an = a1 + (n - 1) . r
print('Gerador de PA')
print('-='*10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
an = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{an} -> ', end='')
        an = an + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
