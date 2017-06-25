l = []

while True:
    l.append(int(input()))
    if sum(l) == 0:
        print(sum([i * i for i in l]))
        break
