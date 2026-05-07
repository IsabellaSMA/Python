class Jokenpo:
    def __init__(self, insNome=False, insJogada=False):
        self.insNome = insNome
        self.insJogada = insJogada
        # Inicializamos as variáveis vazias para não dar erro
        self.jogador = ""
        self.jogada = ""

    def insereJogador(self):
        if self.insNome == False:
            self.jogador = str(input('Insira o nome do jogador: ')).strip()
            self.insNome = True
        else:
            print('O nome do jogador já foi inserido')

    def insereJogada(self):
        if self.insJogada == False:
            # Usamos upper() para garantir que "pedra" ou "PEDRA" funcionem
            self.jogada = str(input(f'{self.jogador}, escolha PEDRA, PAPEL ou TESOURA: ')).upper().strip()
            self.insJogada = True
        else:
            print(f'A jogada já foi inserida e foi {self.jogada}')

    def mainGame(self):
        import random
        # O computador escolhe entre as palavras da lista
        opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
        self.comp = random.choice(opcoes)
        

        print(f'{self.jogador} escolheu: {self.jogada}')
        print(f'Computador escolheu: {self.comp}')

        # Lógica de vitória/derrota/empate
        if self.jogada == self.comp:
            print("EMPATE!")
        
        elif (self.jogada == 'PEDRA' and self.comp == 'TESOURA') or \
             (self.jogada == 'PAPEL' and self.comp == 'PEDRA') or \
             (self.jogada == 'TESOURA' and self.comp == 'PAPEL'):
            print(f'O jogador {self.jogador} VENCEU!')
        
        else:
            print(f'O computador venceu! {self.jogador} PERDEU.')

jogo = Jokenpo()
jogo.insereJogador()
jogo.insereJogada()
jogo.mainGame()