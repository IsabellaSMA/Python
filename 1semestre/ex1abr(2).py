# Programa em que recebe o nome de uma pessoa e sua idade.
#A saída deve dizer se ela tem a obrigatoriedade de votar ou não

nome = str(input('Digite seu nome: ')).capitalize()
idade = int(input('Digite sua idade: '))
if idade <= 15:
    print(f'{nome}, você não tem a obrigatoriedade de votar')
elif idade == 16 or idade == 17:
    print(f'{nome}, seu voto é opcional')
elif idade >= 18:
    print(f'{nome}, seu voto é obrigatório')
