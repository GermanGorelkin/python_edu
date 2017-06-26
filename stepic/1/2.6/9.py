lst = [int(i) for i in input().split()]
x = int(input())
if lst.count(x) == 0:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if x == lst[i]:
            print(i, end=' ')
