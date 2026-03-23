#Calculo de idade usando função, biblioteca datetime e apenas o ano de nascimento.

from datetime import date

def calc_idade(ano_nasc):
    hoje=date.today().year
    return hoje-ano_nasc
    
nome=str(input("Digite seu nome: ")).capitalize()
ano_nasc=int(input("Digite seu ano de nascimento: "))
idade= calc_idade(ano_nasc)
print(f"{nome}, sua idade é {idade}")
