a = int(input())
b = int(input())

cnt = 0
s = 0

if a % 3 != 0:
    for i in range(a+1, a+3):
        if i % 3 == 0:
            a = i
            break

for i in range(a, b + 1, 3):
    cnt += 1
    s += i
print(s/cnt)
