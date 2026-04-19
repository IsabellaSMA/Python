# Challenge odd-even game lang=pt-br

import random
jog = str(input('Digite Par ou Impar: '))
num = int(input('Digite um número de 0 a 10: '))
comp = random.Randint(0, 10)
soma = num+comp

if jog == 'Par' and soma % 2 == 0:
    print(f'O jogador escolheu {jog} e o computador {comp}. O jogador vence ')
elif jog == 'Par' and soma % 2 == 1:
    print(f'O jogador escolheu {jog} e o computador {comp}. O jogador perde')
elif jog == 'Impar' and soma % 2 == 1:
    print(f'O jogador escolheu {jog} e o computador {comp}. O jogador vence')
else:
    print(f'O jogador escolheu {jog} e o computador {comp}. O jogador perde')
