# Crie um programa que receba dois numeros inteiros e realize quatro operações(soma,potenciação ,multiplicação, divisão ) e após os resultados, elevar o numero e verificar se é par ou ímpar

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
soma = num1+num2
mult = num1*num2
div = num1/num2
pot = num1**num2
res = (soma+mult+div+pot)**2

if res % 2 == 0:
    print(f'O resultado das somas das operações é {res}. Logo é PAR')
else:
    print(f'O resultado das somas das operações é {res}. Logo é IMPAR')
    print(f'O resultado das somas das operações é {res}. Logo é IMPAR')
        print (f'O resultado das somas das operações é {res}. Logo é IMPAR')
