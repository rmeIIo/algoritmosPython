#an = a1 + (n - 1) . r
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for n in range(1, 11):
    an = a1 + (n -1) * r
    print(f'{an} -> ', end='')
print('ACABOU')
