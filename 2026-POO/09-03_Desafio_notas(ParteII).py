#Se media for entre 8 e 1o: media excelente e aprovado. Se for entre 5 e 8, está aprovado. Se for menor que 5, repriovado
def notas():
    nome=str(input("Digite seu nome: "))
    nota1=int(input("Digite sua primeira nota: "))
    nota2=int(input("Digite sua segunda nota: "))
    media=(nota1+nota2)/2
    if media>=8 and media==10:
        print(f"Aluno {nome} foi aprovado com média excelente de {media}")
        
    elif media>=5 and media<=8:
        print(f"Aluno {nome} foi aprovado com média de {media}")
    else:
        print(f"Aluno {nome} foi reprovado com média {media}")
    return media
notas()
