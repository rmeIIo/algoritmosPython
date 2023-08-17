# Primeiro segmento:
# Segundo segmento:
# Terceiro segmento:
# Os segmentos acima PODEM FORMAR um triângulo ESCALENO/ISÓCELES/EQUILATERO!
# Os segmentos acima NÃO PODEM FORMAR triângulo!

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 == s2 == s3:
    print(f'Os segmentos acima \033[32mPODEM FORMAR \033[mum triângulo \033[34mEQUILÁTERO\033[m!')
elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 == s2 or s2 == s3 or s1 == s3:
    print(f'Os segmentos acima \033[32mPODEM FORMAR \033[mum triângulo \033[32mISÓSCELES\033[m!')
elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'Os segmentos acima \033[32mPODEM FORMAR \033[mum triângulo \033[33mESCALENO\033[m!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR \033[mtriângulo!')
