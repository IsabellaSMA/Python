class pessoa:
    def __init__(self,nome,cpf,idade,peso,cor_olhos, falar = False, comer = False, andar =False): #superclasse
        self.nome=nome
        self.cpf=cpf
        self.idade=idade
        self.peso=peso
        self.cor_olhos=cor_olhos
        self.falar=falar
        self.comer=comer
        self.andar=andar

    def definicao(self): # função que vai mostrar as caracteŕisticas da pessoa
        print(f'Pessoa \nNome: {self.nome} \nCPF: {self.cpf} \nIdade: {self.idade} \nPeso: {self.peso}kg \nCor dos Olhos: {self.cor_olhos}')

#Com a definição da pessoa, cria-se métodos referentes ás ações de comer e falar com regras: se a pessoa fala, ela não come e vice-versa

    def falando(self): 
        if self.comer==True: 
            print(f'A pessoa {self.nome} não pode falar pois esta comendo!')
        else:
            self.falar=True
            print(f'A pessoa {self.nome} está falando!')

    def comendo(self):
        if self.falar==True: #
            print(f'A pessoa {self.nome} não pode comer pois está falando!')
        else:
            self.comer=True
            print(f'A pessoa {self.nome} está comendo!')

# mas e se a mesma pessoa ou outras realizarão tarefas diferentes simultaneas? tem que ser chamado método por método todas as vezes? Não. Basta criar funções para parar as ações

    def pararFalar(self):
        self.falar==False
        print(f'A pessoa {self.nome} parou de falar')

    def pararComer(self):
        self.comer==False
        print(f'A pessoa {self.nome} parou de comer')

#Mantendo a mesma lõgica, cria-se uma função para mais um método: andar. porém a pessoa pode tanto comer e falar quanto falar e andar assim como apenas andar
    def andando(self):
        if self.falar==True:
            print(f'A pessoa {self.nome} está falando e andando!')
            self.andar=True
        elif self.comer==True:
            print(f'A pessoa {self.nome} está comendo e andando!')
            self.andar=True
        else:
            print(f'A pessoa {self.nome} está apenas andando!')


p1=pessoa('Maurício', 15972730832,80,78,'castanhos') #não necessita referenciar as variáveis. 
p1.definicao() #chama o método alocando e mostrando os valores. Se colocar print(p1), o pycharm mostrará onde está localizado o objeto em código hexadecimal(lingua de máquina)
p1.comendo()

p2=pessoa('Débora', 19057865202,21,40,'castanhos')
p2.andando()
#p2.definicao()
#p3=pessoa('Joana', 39581268737,15,67,'preto')
#p3.definicao()
#p4=pessoa('Samantha', 79685245316,32,60,'verdes')
#p4.definicao()

