class automovel:
    def __init__(self, tipo, marca, ano, cor, rodas, andar=False, quebrar=False):
        self.tipo = tipo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.rodas = rodas
        self.andar = andar
        self.quebrar = quebrar
        
    def definicao(self):
        print(f'Automóvel: {self.tipo}\nMarca: {self.marca}\nAno: {self.ano}\nCor: {self.cor}\nQtd. Rodas: {self.rodas}\n')
            
    def status(self):
        # Primeiro checamos se está quebrado
        if self.quebrar:
            print(f'O automóvel {self.marca} está quebrado e não pode andar!')
        # Se não estiver quebrado, verificamos se está em movimento ou parado
        elif self.andar:
            print(f'O automóvel {self.marca} está andando.')
        else:
            print(f'O automóvel {self.marca} está parado (está bom, mas não em movimento).')
                
    def iniciar_movimento(self):
        if self.quebrar:
            print(f'Erro: Não é possível dar partida, o {self.marca} está quebrado!')
        else:
            self.andar = True # Usamos "=" para atribuir o valor
            print(f'O automóvel {self.marca} começou a andar.')

    def parar_movimento(self):
        self.andar = False # Usamos "=" para atribuir o valor
        print(f'O automóvel {self.marca} parou de andar.')
            
    def quebrar_veiculo(self):
        self.quebrar = True # Usamos "=" para atribuir o valor
        self.andar = False  # Se quebrou, ele para de andar automaticamente
        print(f'O automóvel {self.marca} quebrou!')

    def consertar(self):
        self.quebrar = False
        print(f'O automóvel {self.marca} foi consertado!')

# Testando a lógica
a1 = automovel('Carro', 'Renault Sandero', 1996, 'Prata', 4)
a1.definicao()

a2= automovel('Ônibus','Mercedes',2010,'Azul',6)
a2.definicao()

a1.iniciar_movimento() # Começa a andar
a1.status()
a1.quebrar_veiculo()   # Quebra (ele para de andar)
a1.status()
a1.iniciar_movimento() # Tenta andar quebrado (não vai conseguir)

