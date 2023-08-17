import random
numeros = tuple(random.sample(range(1, 101), 5))
print(f'Os números gerados foram: {numeros}')
menor = min(numeros)
maior = max(numeros)
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
