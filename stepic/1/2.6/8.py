n = int(input())
i = 1
while True:
    for j in range(i):
        print(str(i), end=' ')
        n -= 1
        if n <= 0:
            break
    if n <= 0:
        break
    i += 1
