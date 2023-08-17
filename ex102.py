def fatorial(num, show=False):
    """
    Função que calcula o fatorail de um número e mostra (opcionalmente) o processo de cálculo.
    :param num: número inteiro a ser calculado o fatorial.
    :param show: valor booleano indicando se o processo de cálculo deve ser mostrado na tela
    :return: resultado do fatorial
    """
    fat = 1
    for i in range(num, 0, -1):
        fat *= 1
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return fat

print(fatorial(5, True))
print(fatorial(5))
