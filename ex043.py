# Qual é seu peso? (Kg) [87] [120] [150] [45]
# Qual é sua altura? (m) [1.97] [1.75] [1.60] [1.80]
# O IMC dessa pessoa é de x
# PARABÉNS, você está na faixa de PESO NORMAL!
# Você está em OBESIDADE!
# Você está em OBESIDADE MÓRBIDA, cuidado!
# Você está ABAIXO DO PESO normal!

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
IMC = peso/(altura**2)
print(f'O IMC dessa pessoa é de {IMC:.1f}')
if IMC < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif IMC > 18.5 and IMC <= 25:
    print('PARABÉNS! Você está na faixa de peso normal.')
elif IMC > 25 and IMC <= 30:
    print('Você está em SOBREPESO!')
elif IMC > 30 and IMC <= 40:
    print('Você está em OBESIDADE!')
elif IMC > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

