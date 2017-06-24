x = int(input())

first = (x // 100000) + (x // 10000 % 10) + (x // 1000 % 10)
last = (x % 10) + (x % 100 // 10) + (x % 1000 // 100)

if first == last:
    print('Счастливый')
else:
    print('Обычный')
