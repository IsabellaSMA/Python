import random
class jogo: #superclasse JOGO
    def __init_(self,jog, num, comp,soma):
        self.jog=jog
        self.num=num
        self.comp=comp
        self.soma=soma
    
    def par_impar(self): 
        jog=str(input("Digite [PAR] ou [IMPAR]:")).upper()
        num=int(input("Digite um numero de 0 a 10: "))
        comp=random.randint(0,10)
        soma= num+comp
        if (jog == 'PAR' and soma % 2 == 0) or (jog == 'IMPAR' and soma % 2 == 1):
            print('O jogador vence')
        else:
            print('O jogador perde')

p1=jogo() # P = partida 1 e chama a superclasse
p1.par_impar() # a partida 1 chama o par e impar