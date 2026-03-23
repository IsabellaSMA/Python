#Se media for entre 8 e 1o: media excelente e aprovado. Se for entre 5 e 8, está aprovado. Se for menor que 5, repriovado
def notas():
    media=(nota1+nota2)/2
    if media>=8.5 and media==10:
        print(f"Aluno {nome} foi aprovado com média excelente de {media}")
        
    elif media>=5 and media<=8.4:
        print(f"O(a) aluno(a): {nome} foi aprovado com média de {media}")
    else:
        print(f"O(a) aluno(a): {nome} foi reprovado com média {media}")
    return media

nome=str(input("Digite seu nome: ")).capitalize()
nota1=float(input("Digite sua primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))
notas()
