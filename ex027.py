nom = input('Digite seu nome completo: ').strip()
nom = nom.title()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nom.split()[0]}')
print(f'Seu último nome é {nom.split()[-1]}')


