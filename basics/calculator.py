num1 = int(input())
num2 = int(input())
action = (input('Выберите операцию из следующих +-*/%**// : '))
if action == '+':
    print('Ответ:', num1 + num2)
elif action == '-':
    print('Ответ:', num1 - num2)
elif action == '*':
    print('Ответ:', num1 * num2)
elif action == '/':
    print('Ответ:', num1/num2)
elif action == '%':
    print('Ответ:', num1 % num2)
elif action == '**':
    print('Ответ:', num1 ** num2)
elif action == '//':
    print('Ответ:', num1 // num2)
else:
    print('Ответ:Данной операции нет в системе')