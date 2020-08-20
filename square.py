k = input()
l = "треугольник"
m = "прямоугольник"
o = "круг"
if k == m:
    a = float(input())
    b = float(input())
if k == l:
    a = float(input())
    b = float(input())
    c = float(input())
    p = float((a + b + c) / 2)
    s = float(p * (p - a) * (p - b) * (p - c))
if k == o:
     a = float(input())
     π = float(3.14)
if k == m:
    print(a * b)
if k == l:
    print(s ** 0.5)
if k == o:
    print(π * (a ** 2))
