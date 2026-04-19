# Jogo em que o jogador 3 tres vidas e deve responder "Atirar" e o computador irá escolher seu destino: se o jogador vai matar, morrer ou errar o tiro
# Improved by myself

import random


def fase():
    rod = str(input('Um inimigo apareceu..ATIRE: '))
    comp = random.choice(['Errou', 'Matou', 'Morreu'])

    if rod == 'ATIRAR' and comp != 'Matou':
        print('O inimigo sobrevive, retornando para o início da fase..')
        return False
    elif comp == 'Matou':
        print('Você derrotou o inimigo, para a próxima fase..')
    else:
        print('Você foi derrotado pelo inimigo. Recomeçando o nível...')
        return True


def inicio():  # tutorial for this game
    print('Bem vindo(a) ao jogo de Matou, Morreu, Errou.')
    print('Seu objetivo é digitar a palavra´Atirar´ e o computador decidirá se você passará de fase')
    start = str(input('Vamos começar?[S/N] ')).upper()
    return start == 'S'


def jogo():
    if not inicio():
        return
    count = 0
    while count < 3:
        count += 1
    if fase():
        break
        print(f'Tentativa {count} de 3')
    else:
        print('Tentativas esgotadas. Fim de jogo')


jogo()
