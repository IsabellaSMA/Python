# Condicionals: if and else.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
soma = num1+num2
if soma % 2 == 0:
    print(
        f'A soma dos números {num1} e {num2} é igual á: {soma}.Resultando em PAR')
else:
    print(
        f'A soma dos números {num1} e {num2} é igual á: {soma}.Resultando em IMPAR')
