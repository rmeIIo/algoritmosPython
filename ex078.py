lista_numeros = []

for i in range(5):
    numero = float(input('Digite um número: '))
    lista_numeros.append(numero)

maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)
posicao_maior = lista_numeros.index(maior_valor)
posicao_menor = lista_numeros.index(menor_valor)

print(f'Maior valor: {maior_valor}, na posição {posicao_maior}')
print(f'Menor valor: {menor_valor}, na posição {posicao_menor}')

