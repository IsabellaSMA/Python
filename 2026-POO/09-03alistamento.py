#Se o candidatop tem 18 anos ou mais deve se alistarn se não, não tem maioridade
def alistamento():
    nome=str(input("Digite seu nome: "))
    idade=int(input("Digite sua idade: "))
    if idade >=18:
        print (f"O candidato {nome} está apto para se alistar no exército")
    else:
        print (f" O candidato {nome} não possui maioridade para se alistar no exército")
alistamento()        