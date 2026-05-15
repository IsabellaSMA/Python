#pra testar codigo: online-python.com

class Animal:
	def fazerSom(self):
		print("Animal fez som")

class Cachorro(Animal):
	def abanarRabo(self):
		print("O cachorro está abanando o rabo")

class Humano(Animal):
	def falar(self):
		print("O som que o humano faz é falar")


cachorro1= Cachorro() # Só de criar o objeto e chamar a classe 
cachorro1.fazerSom()  # aparecerá a mensagem O animal fez som


humano1=Humano()
humano1.falar()

