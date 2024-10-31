# Condicionals 18 march
# Create a program that receives 3 grades from a student and calculates the average.
# To pass, the final grade must be greater than or equal to 7.0. The output of the program should say the score and whether the student passed.

nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite uma nota: '))
nota3 = float(input('Digite uma nota: '))
media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f'A média do aluno é: {média}. Logo está Aprovado')
else:

    print(f'A média do aluno é: {média}. Logo está Reprovado')
