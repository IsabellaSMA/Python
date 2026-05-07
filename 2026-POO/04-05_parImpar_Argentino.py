class parImpar:
    def __init__(self, insNome=False, insJogada=False, insNumero=False):
        self.insNome = insNome
        self.insJogada = insJogada
        self.insNumero = insNumero

    def insereJogador(self):
        if self.insNome == False:
            self.jogador = str(input('Insira o nome do jogador: '))
            self.insNome = True
        else:
            print('O nome do jogador já foi inserido')

    def insereJogada(self):
        if self.insJogada == False:
           self.jogada = str(input(f'{self.jogador}: Digite Par ou Ímpar: ')).lower().strip()
           self.insJogada = True
        else:
            print(f'A jogada já foi inserida e foi {self.jogada}')

    def insereNumero(self):
        if self.insNumero == False:
            self.numero = int(input(f'{self.jogador} você pediu {self.jogada}, agora digite um numero de 0 a 10: '))
            self.insNumero = True
        else:
            print(f'O número já foi inserido')

    def mainGame(self):
        import random
        self.comp = random.randint(0,10)
        self.esccomp = ""
        soma = self.numero + self.comp
        if self.jogada == "par":
            self.esccomp = "impar"
        else:
            self.esccomp = "par"
        if self.jogada == 'par' and soma % 2 == 0 or self.jogada == 'impar' and soma % 2 != 0:
            print(f'O jogador {self.jogador} escolheu {self.jogada} e o número {self.numero} o computador escolheu'
                  f' {self.esccomp} e o número {self.comp}. Jogador Venceu!')
        else:
            print(f'O jogador {self.jogador} escolheu {self.jogada} e o número {self.numero} o computador escolheu {self.esccomp} e o número {self.comp}. Jogador Perdeu')


p = parImpar()

p.insereJogador()

p.insereJogada()
p.insereNumero()

p.mainGame()