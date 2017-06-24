import math

x = float(input())
y = float(input())
op = input()

if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '/':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x / y)
elif op == '*':
    print(x * y)
elif op == 'mod':
    if y == 0:
        print('Деление на 0!')
    else :
        print(x % y)
elif op == 'pow':
    print(math.pow(x, y))
elif op == 'div':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x // y)
