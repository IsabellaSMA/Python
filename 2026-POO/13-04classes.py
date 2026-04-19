class pessoa:
    def __init__(self,nome,cpf,idade,peso,cor_olhos, falar = False, comer = False, andar =False):
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

p1=pessoa('Maurício', 15972730832,80,78,'castanhos')
p1.definicao()

p2=pessoa('Débora', 19057865202,21,40,'castanhos')
p2.definicao()

p3=pessoa('Joana', 39581268737,15,67,'preto')
p3.definicao()

p4=pessoa('Samantha', 79685245316,32,60,'verdes')
p4.definicao()

