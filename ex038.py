# Primeiro número: 4
# Segundo número: 1
# O PRIMEIRO valor é maior.
# O SEGUNDO valor é maior.
# Os dois valores são IGUAIS.

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1>n2:
    print('O PRIMEIRO valor é maior.')
elif n2>n1:
    print('O SEGUNDO valor é maior.')
elif n1==n2 or n2==n1:
    print('Os dois valores são IGUAIS.')
