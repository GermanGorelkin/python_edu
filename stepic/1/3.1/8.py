def f(x):
    if x <= -2:
        return -x * x - 4 * x - 3
    elif -2 < x <= 2:
        return -x/2
    elif 2 < x:
        return x * x - 4 * x + 5

n = float(input())

print(f(n))
