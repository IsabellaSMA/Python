# jogo do par ou ímpar que oferece 3 chances ao jogador:
count = 0
while count < 3:
    count += 1
    import random
    jog = str(input('PAR ou IMPAR: ').upper())
    num = int(input('Digite um número de 0 a 10: '))
    comp = random.randint(0, 10)
    soma = num+comp
    print(f'O jogador escolheu {jog} e o numero {num}.')
    print(f'O computador escolheu o número: {comp}')

    if jog == 'PAR' and soma % 2 == 0:
        print('O jogador vence')
    elif jog == 'IMPAR' and soma % 2 == 0:
        print('O jogador perde')
    elif jog == 'IMPAR' and soma % 2 == 1:
        print('O jogador ganha')
    else:
        print('O jogador perde')
