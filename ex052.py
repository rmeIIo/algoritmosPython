n = int(input('Digite um número: '))
tot = 0
for num in range(1, n+1):
    if n % num == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print(f'{num} ', end='')
print(f'\n\033[mO número {n} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
