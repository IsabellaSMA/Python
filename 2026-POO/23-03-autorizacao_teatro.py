from datetime import date

def calc_idade(ano_nasc):
    hoje=date.today().year
    return hoje-ano_nasc
   
print("Boas vindas ao sistema do Theatro Mallabaris!")


nome=str(input("Digite seu nome: ")).capitalize()
ano_nasc=int(input("Digite seu ano de nascimento: "))
idade= calc_idade(ano_nasc)

if idade >=16 and idade <18:
    print("Para menores de 18, deve-se apresentar um documento de identidade antes de assistir aos espetáculos")

elif idade<=12:
    print("Para pessoas de 12 anos ou menos, um responsável legal deve acompanhar a criança. ")

else
    print(f"A passagem é liberada para pessoas com mais de 20 anos")
