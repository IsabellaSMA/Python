# Jogo do pedra, papel tesoura com placar
import random
vitorias = 0
derrotas = 0
count = 0  # contagem das chances do jogador
while count < 3:
    count += 1
    jog = str(input('Digite pedra,papel ou tesoura: ')).upper()
    num = int(input('Digite um numero de 0 a 10: '))
    comp = random.randint(0, 10)
    soma = num+comp
    print(
    f'O jogador escolheu {jog} e o número {num}. O computador escolheu o número {comp}')

   if (jog == 'PAR' and soma % 2 == 0) or (jog == 'IMPAR' and soma % 2 != 0):
        print(O jogador vence)
        vitorias += 1
    else:
        print('O jogador perde')
        derrotas += 1

def placar():
    print('Placar: ')
    print(f'Vitórias do jogador: {vitorias}')
    print(f'Derrotas do jogador: {derrotas}')
placar()