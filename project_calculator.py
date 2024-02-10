print('\n⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂ PYTHON CALCULATOR VERSION 1 ⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂\n')

def add(firtNum,secondNum):
    return firtNum+secondNum

def sub(firtNum,secondNum):
    return firtNum-secondNum

def mul(firtNum,secondNum):
    return firtNum*secondNum

def div(firtNum,secondNum):
    return firtNum/secondNum

choice_firtNum = float(input('Enter the FIRST number: '))
choice_secondNum = float(input('Enter the SECOND number: '))

operation = input('Choose the following options: \n\n[a] - Addition \n[b] - Subtraction \n[c] - Multiplication \n[d] - Division \n\n▶️  Your choice was: ')

for oper in operation:
    if  oper == 'a':
        print('\n🧮 Addition %r + %r =' %(choice_firtNum,choice_secondNum), add(choice_firtNum,choice_secondNum))
    elif oper == 'b':
        print('\n🧮 Subtraction %r - %r =' %(choice_firtNum,choice_secondNum), sub(choice_firtNum,choice_secondNum))
    elif oper == 'c':
        print('\n🧮 Multiplication %r * %r =' %(choice_firtNum,choice_secondNum), mul(choice_firtNum,choice_secondNum))
    elif oper == 'd':
        if choice_secondNum != 0:
            print('\n🧮 Division %r / %r =' %(choice_firtNum,choice_secondNum), div(choice_firtNum,choice_secondNum))
        else:
            print('\n⛔ Error! Cannot perform division by zero.')
    else:
        print('\n⛔ Erro! \nChoose the following options: \n\n[a] - Addition \n[b] - Subtraction \n[c] - Multiplication \n[d]  - Division ')