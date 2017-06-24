shape_type = input()

if shape_type == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())

    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    s = s ** 0.5

    print(s)
elif shape_type == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif shape_type == 'круг':
    r = float(input())
    s = 3.14 * r ** 2
    print(s)
