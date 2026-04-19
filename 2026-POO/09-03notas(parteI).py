def notas():
    nome=str(input("Digite seu nome: "))
    nota1=int(input("Digite sua primeira nota: "))
    nota2=int(input("Digite sua segunda nota: "))
    media=(nota1+nota2)/2
    if media>=5:
        print(f"Aluno {nome} foi aprovado com média {media}")
    else:
        print(f"Aluno {nome} foi reprovado com média {media}")
    return media
notas()