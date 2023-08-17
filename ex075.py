valores = ()
for i in range(4):
    valor = int(input('Digite um valor: '))
    valores = valores + (valor,)

qtd_9 = 0
for valor in valores:
    if valor == 9:
        qtd_9 += 1
print(f'O valor 9 apareceu {qtd_9} vezes na tupla.')

pos_3 = None
for i in range(4):
    if valores[i] == 3:
        pos_3 = i
        break
if pos_3 is not None:
    print(f'O primeiro valor 3 foi encontrado na posição {pos_3} da tupla.')
else:
    print('Não foi digitado nenhum valor 3 na tupla.')

valores_pares = ()
for valor in valores:
    if valor % 2 == 0:
        valores_pares = valores_pares + (valor,)
if len(valores_pares) > 0:
        print(f'Os valores pares da tupla são: {valores_pares}')
else:
        print('Não há valores pares na tupla')