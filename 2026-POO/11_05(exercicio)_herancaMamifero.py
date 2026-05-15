class Mamifero: #classe mae que vai ter as outras classes como Cachorro, Humano
    def __init__(self, nome,raca, cor_olhos, cor_pelo,comer=False,beber=False,
    sentar=False,andar = False,correr =False,pular =False):
        self.nome = nome
        self.raca=raca
        self.cor_olhos=cor_olhos
        self.cor_pelo=cor_pelo
        self.comer = comer
        self.beber = beber
        self.sentar = sentar
        self.andar = andar
        self.correr = correr
        self.pular = pular
        
        def apresentar(self):
            print(f"Nome: {self.nome}\nRaça: {self.raca}\nCor dos olhos: {self.cor_olhos}")
            print(f"\nCor dos pelos: {self.cor_pelo}")
            
        def comendo(self):
            print(f" O mamífero {self.nome} da raça {self.raca} está comendo")
            self.comer = True
                
        def bebendo(self):
            print(f" O mamífero {self.nome} da raça {self.raca} está bebendo algo")
            self.beber = True
                    
        def andando(self):
            print(f" O mamífero {self.nome} da raça {self.raca} está andando")
            self.andar=True
                        
        def correndo(self):
            print(f" O mamífero {self.nome} da raça {self.raca} está correndo")
            self.correr=True
                            
        def pulando(self):
            print(f" O mamífero {self.nome} da raça {self.raca} está pulando")
            self.pular=True

class Humano(Mamifero):
    def __init__(self, nome,raca, cor_olhos, cor_pelo,comer=False,beber=False,
    sentar=False,andar = False,correr =False,pular =False , falar=False):
        super().__init__(nome,raca, cor_olhos, cor_pelo,comer,beber,sentar, andar, correr, pular,)
        self.falar = falar
    
    def falando(self):
        print (f"O humano {self.nome} está falando Oi")
        self.falar=True


class Cachorro(Mamifero):
    def __init__(self, nome,raca, cor_olhos, cor_pelo,comer=False,
    beber=False,sentar=False,andar = False,correr =False,pular =False,latir=False):
        super().__init__(nome,raca, cor_olhos, cor_pelo,comer,beber,sentar, andar, correr, pular)
        self.latir = latir
        
    def latindo(self):
        print (f"O cachorro {self.nome} está latindo")
        self.latir=True


humano1=Humano("Isabella","humana","Castanho","Castanho")
humano1.falando()
#problemas ao chamar métodos da classe Mãe -> Mamifero

cachorro1=Cachorro("Freddy","Cachorro","Castanho","Preto e Branco")
cachorro1.latindo()
