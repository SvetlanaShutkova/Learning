lowercase = input().lower().split()
d = {x: lowercase.count(x) for x in lowercase}
for key, value in d.items():
    print(key, value)
