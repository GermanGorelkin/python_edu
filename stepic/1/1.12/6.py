n = int(input())
x = n % 100

if 11 <= x <= 19:
    print(x, 'программистов')
else:
    x = n % 10
    if x == 1:
        print(x, 'программист')
    elif 2 <= x <= 4:
        print(x, 'программиста')
    else:
        print(x, 'программистов')

