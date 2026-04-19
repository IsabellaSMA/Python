# desafio- fazer o jogo do Pedra, Papel, Tesoura
import random
jog = str(input('digite PEDRA, PAPEL ou TESOURA: ')).upper()
opc = ['PEDRA', 'PAPEL', 'TESOURA']
comp = random.choice(opc)
soma = jog+comp
print(f'O jogador escolheu :{jog} e o computador: {comp}')

if jog == 'PEDRA' and comp == 'TESOURA':
    print('O jogador vence!')
elif jog == 'PEDRA' and comp == 'PAPEL':
    print('O jogador perde')
elif jog == 'PAPEL' and comp == 'PEDRA':
    print('o jogador vence')
elif jog == 'PAPEL' and comp == 'TESOURA':
    print('O jogador perde')
elif jog == 'TESOURA' and comp == 'PAPEL':
    print('O jogador vence')
elif jog == 'TESOURA' and comp == 'PEDRA':
    print('O jogador perde')
else:
    print('O jogo deu empate')
