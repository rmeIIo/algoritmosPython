# Valor da casa: R$80000
# Salário do comprador: R$1600
# Quantos anos de financiamento? 7
# Para pagar uma casa de R$80000 em 7 anos a prestação será de R$x
# Empréstimo NEGADO

# Valor da casa: R$80000
# Salário do comprador: R$10000
# Quantos anos de financiamento? 7
# Para pagar uma casa de R$80000 em 7 anos a prestação será de R$x
# Empréstimo pode ser CONCEDIDO

casa = float(input('\033[34mValor da casa:\033[m \033[32mR$'))
salario = float(input('\033[34mSalário do comprador:\033[m \033[32mR$'))
tempo = int(input('\033[34mQuantos anos de financiamento? '))
prestacao = casa/(tempo*12)

print(f'\033[mPara pagar uma casa de \033[32mR${casa:.2f} \033[mem {tempo} anos, a prestação será de \033[32mR${prestacao:.2f}')
if prestacao > salario*0.3:
    print('\033[mEmpréstimo \033[31mNEGADO\033[m!')
else:
    print('\033[mEmpréstimo pode ser \033[32mCONCEDIDO\033[m!')
