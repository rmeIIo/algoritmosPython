lista = []
for i in range(5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print(f'{num} adicionado ao final da lista.')
    else:
        for j in range(len(lista)):
            if num <= lista[j]:
                lista.insert(j, num)
                print(f'{num} adicionado na posição {j} da lista.')
                break
print('-='*30)
print(f'Os valores digitados, em ordem crescente, foram: {lista}.')
