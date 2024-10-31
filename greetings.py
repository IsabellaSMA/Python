name = str(input('What´s your name? ')).capitalize()
print(f'Hello, {name}, this is my greeting code ')
opc = str(input(
    'I´m IsabellaSMA and hope you like my repository :). Wanna know more about? [Y/N] ')).upper()


def more():
    print('At first, I´m starting to code in my natural language, creating code that all beginners do')
    print('While I´m improving, my code will be in English, but until that happens, the titles and descriptions of my code will be in English')


if opc == 'Y':
    more()
else:
    print('Okay, thanks for visiting!')
