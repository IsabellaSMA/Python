# Write a program that receives two int numbers and from these numbers, creates variables for each mathematical operation learned. The output of the program should calculate the average of all the operations performed.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2
media = (soma+sub+mult+div)/4
print(f'A média de todas as operações é: {média}')
