def calc_imc():
    nome=str(input("Digite seu nome: ")).capitalize()
    idade=int(input("Digite a idade: "))
    peso=float(input("Digite seu peso (ex 51.9): "))
    altura=float(input("Digite sua altura (ex 1.81): "))
    
    imc=peso/(altura**2)
    print(f"Seu Indice de massa corporal é: {imc:.1f} ")
    
    if imc<18.5:
        print(f" {nome}. De acordo com a tabela de IMC, seu nível é: Magreza")
    elif imc >=25.5 and imc <=29.9:
        print(f" {nome}. De acordo com a tabela de IMC, seu nível é: Sobrepeso")
    elif imc >=30.0 and imc <=34.9:
        print(f" {nome}.De acordo com a tabela de IMC, seu nível é: Obesidade I")
    elif imc >=35.0 and imc<=39.9:
        print(f" {nome}.De acordo com a tabela de IMC, seu nível é: Obesidade II")
    elif imc >=40:
        print(f" {nome}.De acordo com a tabela de IMC, seu nível é: Obesidade III")
    else:
        print(f" {nome}.De acordo com a tabela de IMC, seu nível é: Normal")
calc_imc()
