n = int(input())
result = {}


def f(num):
    return num ** num


for i in range(n):
    x = int(input())
    if x not in result:
        result[x] = f(x)
    print(result[x])
