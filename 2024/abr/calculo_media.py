#Código que recebe o nome de um aluno, duas notas e efetuar o cálculo da média com 
#condições se a média for menor que 5, maior igual a 8 ou igual a 10

nome = str(input('Digite seu nome: ')).capitalize()
nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite uma nota: '))
media = (nota1+nota2)/2
print(f'Sua média é: {media}')

if media <= 10 and media >= 8:
    print(f'Parabéns {nome}, sua média está excelente e você está aprovado(a)')
elif media <= 8 and media >= 5:
    print(f'Parabéns {nome}, você está na média e aprovado(a)')
elif media < 5:
    print(
        f'Sinto muito {nome},você não atingiu a média. Logo está reprovado(a)')
