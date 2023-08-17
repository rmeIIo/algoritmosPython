#an = a1 + (n - 1) . r
print('Gerador de PA')
print('-='*10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
an = a1
cont = 1
while cont <= 10:
    print(f'{an} -> ', end='')
    an = an + r
    cont = cont + 1
print('FIM')

