s = input().split()
d = {}
for i in [i.lower() for i in s]:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for k, v in d.items():
    print(k, v)
