a = int(input())
b = int(input())
i = 2
if a > b:
    a, b = b, a
d = a

while True:
    if d % b == 0:
        break
    d = a * i
    i += 1
print(d)
