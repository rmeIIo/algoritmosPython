# Preço das compras: R$ [1500]
# FORMAS DE PAGAMENTO:
# [ 1 ] à vista dinheiro/cheque
# [ 2 ] à vista cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão
# Qual é a opção?
# Sua compra de R$ x vai custar X no final. {opção 1} {10% de desconto}
# Sua compra de R$ x vai custar X no final. {opção 2} {5% de desconto}
# Sua compra de R$ x vai custar X no final. {opção 3} {sem desconto}
# Quantas parcelas? {opção 4}
# Sua compra será parcelada em Xx de R$x COM JUROS {20% de juros}
# Sua compra de R$ x vai custar X no final.

print('\033[31m='*10, 'LOJAS AMERICANAS', '='*10)
preco = float(input('\033[mPreço das compras: R$'.strip()))
print('FORMA DE PAGAMENTO:')
print('\033[31m[ 1 ] \033[mà vista dinheiro/cheque')
print('\033[31m[ 2 ] \033[mà vista cartão')
print('\033[31m[ 3 ] \033[m2x no cartão')
print('\033[31m[ 4 ] \033[m3x ou mais no cartão')
opt = int(input('Qual é a opção? '))
if opt == 1:
    dsc = preco - (preco*0.1)
    print(f'Sua compra de R${preco:.2f} vai custar \033[32mR${dsc:.2f} \033[mno final. ')
elif opt == 2:
    dsc = preco - (preco*0.05)
    print(f'Sua compra de R${preco:.2f} vai custar \033[32mR${dsc:.2f} \033[mno final.')
elif opt == 3:
    print(f'Sua compra vai custar \033[32mR${preco:.2f}\033[m, sem descontos!')
elif opt == 4:
    p = int(input('Quantas parcelas? '))
    juros = preco + (preco * 0.2)
    p1 = juros / p
    print(f'Sua compra será parcelada em {p}x de \033[32mR${p1:.2f} \033[mCOM JUROS.')
else:
    print('\033[31mOpção não encontrada! \033[mTente novamente!')
