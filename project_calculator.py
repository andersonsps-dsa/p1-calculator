print('\n⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂ PYTHON CALCULATOR VERSION 1 ⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂\n')

x = float(input('Enter the FIRST number: '))
y = float(input('Enter the SECOND number: '))

operation = input('Choose the following options: \n\n[a] - Addition \n[b] - Subtraction \n[c] - Multiplication \n[d] - Division \n\n▶️  Your choice was: ')

for oper in operation:
    if  oper == 'a':
        print('👌 Addition %r + %r =' %(x,y), x+y)
    elif oper == 'b':
        print('👌 Subtraction %r - %r =' %(x,y), x-y)
    elif oper == 'c':
        print('👌 Multiplication %r * %r =' %(x,y), x*y)
    elif oper == 'd':
        if y != 0:
            print('👌 Division %r / %r =' %(x,y), x/y)
        else:
            print('⛔ Error! Cannot perform division by zero.')
    else:
        print('⛔ Erro! \nChoose the following options: \n\n[a] - Addition \n[b] - Subtraction \n[c] - Multiplication \n[d]  - Division ')