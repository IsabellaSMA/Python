class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def apresentar(self):
        print(f"Nome: {self.nome} ")
        print(f"Idade: {self.idade}")

# classe filha que herda da mãe
class Aluno(Pessoa):
    def __init__ (self,nome,idade,curso):
        # Herda os atributos da classe mãe com esse código abaixo:
        super().__init__(nome,idade)

        # Atributo próprio da classe filha:
        self.curso=curso

    def mostrarCurso(self):
        print(f"Curso: {self.curso}")

# Criando objeto
aluno1 = Aluno("Massao",23,"ADS")

# Métodos herdados
aluno1.apresentar()

#método da classe filha
aluno1.mostrarCurso()
