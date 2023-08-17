a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

# Menor
menor = a
if a<b and a<c:
    menor = a
if b<c and b<c:
    menor = b
if c<a and c<b:
    menor = c

# Maior
maior = a
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')
