l = [int(i) for i in input().split()]
l.sort()

r = []

if len(l) > 1:
    for i in range(len(l)):
        if l[i-1] == l[i]:
            if l[i] not in r:
                r.append(l[i])
for i in r:
    print(i, end=' ')
