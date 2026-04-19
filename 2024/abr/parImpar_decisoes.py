# 'Criar o jogo do par ou impar em que o usuario decide se quer jogar denovo'
import random
while True:
    jog = input('PAR ou IMPAR: ').upper()
    num = int(input('Digite um número de 0 a 10: '))
    comp = random.randint(0, 10)
    soma = num + comp
    print(f'O jogador escolheu {jog} e o número {num}.')
    print(f'O computador escolheu o número: {comp}')

    if (jog == 'PAR' and soma % 2 == 0) or (jog == 'IMPAR' and soma % 2 == 1):
        print('O jogador vence')
    else:
        print('O jogador perde')

    opc = input('Gostaria de jogar de novo? [S/N]').upper()
    if opc != 'S':
        print('Obrigada por jogar!')
        break
