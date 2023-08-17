import math

#variaveis
ang = int(input('Digite um ângulo que você deseja: '))

print(f'O ângulo de {ang} tem o SENO de {math.sin(math.radians(ang)):.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {math.cos(math.radians(ang)):.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {math.tan(math.radians(ang)):.2f}')
