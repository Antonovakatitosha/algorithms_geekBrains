from random import randint

a = [randint(1, 101) for _ in range(15)]
print(a)
max_pos, min_pos = 0, 0

for i, elem in enumerate(a):
    if elem > a[max_pos]: max_pos = i
    if elem < a[min_pos]: min_pos = i

a[max_pos], a[min_pos] = a[min_pos], a[max_pos]
print(a[max_pos], a[min_pos])
print(a)
