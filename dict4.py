def f(x):
    return x ** 3


n = int(input())
d = {}
for _ in range(n):
    i = int(input())
    if i not in d:
        d[i] = f(i)
    print(d[i])
