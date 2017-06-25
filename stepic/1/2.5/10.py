l = [int(i) for i in input().split()]

if len(l) == 1:
    print(l[0])
else:
    for i in range(len(l)):
        v1 = l[i-1]
        if i == len(l)-1:
            v2 = l[0]
        else:
            v2 = l[i+1]
        print(v1+v2, end=' ')
