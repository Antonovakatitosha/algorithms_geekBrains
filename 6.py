from random import randint
a = [randint(0, 20) for _ in range(12)]
print(a)

min_pos, max_pos = 0, 0
for i, elem in enumerate(a):
    if elem > a[max_pos]: max_pos = i
    if elem < a[min_pos]: min_pos = i

result_sum = 0
for i in range(min(min_pos, max_pos) + 1, max(max_pos, min_pos)):
    result_sum += a[i]
print(f'result_sum = {result_sum}')


