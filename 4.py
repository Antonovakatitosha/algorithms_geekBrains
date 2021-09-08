from random import randint
a = [randint(1, 7) for _ in range(20)]
print(a)

b = {}
for elem in a:
    if elem in b: b[elem] += 1
    else: b[elem] = 1

max_key, max_value = 0, 0
for key, value in b.items():
    if value > max_value:
        max_key = key
        max_value = value

print(b)
print(max_key)
