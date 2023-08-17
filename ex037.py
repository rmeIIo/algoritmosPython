# Digite um número inteiro: 234
# Escolha uma das bases para conversão:
# [ 1 ] converter para BINÁRIO
# [ 2 ] converter para OCTAL
# [ 3 ] converter para HEXADECIMAL
# Sua opção:
# x convertido para BINÁRIO/OCTAL/HEXADECIMAL é igual a y

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('\033[34m[ 1 ] converter para BINÁRIO')
print('\033[32m[ 2 ] converter para OCTAL')
print('\033[33m[ 3 ] converter para HEXADECIMAL')
conv = int(input('\033[mSua opção: '))

if conv == 1:
    print(f'{num} convertido para \033[34mBINÁRIO \033[mé igual a {bin(num)[2:]}')
elif conv == 2:
    print(f'{num} convertido para \033[32mOCTAL \033[mé igual a {oct(num)[2:]}')
elif conv == 3:
    print(f'{num} convertido para \033[33mHEXADECIMAL \033[mé igual {hex(num)[2:]}')
else:
    print('\033[31mOpção inválida! \033[mTente novamente!')
