s = input()
cnt = 1
prev = ''

for i in s:
    if i == prev:
        cnt += 1
    elif prev != '':
        print(cnt, end='')
        cnt = 1
        print(i, end='')
    else:
        print(i, end='')
    prev = i
print(cnt, end='')
