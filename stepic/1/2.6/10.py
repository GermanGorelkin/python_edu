l1 = []
while True:
    s = input()
    if s == 'end':
        break
    l1.append([int(i) for i in s.split()])

width, height = len(l1), len(l1[0])
l2 = [[0 for i in range(height)] for i in range(width)]

for i in range(width):
    for j in range(height):
        if i == 0:
            l2[i][j] += l1[width - 1][j]
        else:
            l2[i][j] += l1[i - 1][j]
        if i == width - 1:
            l2[i][j] += l1[0][j]
        else:
            l2[i][j] += l1[i + 1][j]
        if j == 0:
            l2[i][j] += l1[i][height - 1]
        else:
            l2[i][j] += l1[i][j - 1]
        if j == height - 1:
            l2[i][j] += l1[i][0]
        else:
            l2[i][j] += l1[i][j + 1]
for i in l2:
    print(' '.join(map(str, i)))
