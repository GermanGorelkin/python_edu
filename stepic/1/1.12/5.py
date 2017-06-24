a = int(input())
b = int(input())
c = int(input())

temp = a

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(c)
print(a)
print(b)
