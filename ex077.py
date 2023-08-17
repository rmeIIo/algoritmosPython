palavras = ('python', 'programacao', 'dados', 'computacao')
vogais = 'aeiou'

for palavra in palavras:
    print(f'Vogais da palavra {palavra}:', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end='')
    print()