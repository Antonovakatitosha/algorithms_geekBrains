a = [i for i in range(2, 100)]
b = [0 for i in range(10)]

for i in range(2, 10):
    j = 0
    while j < len(a):
        if a[j] % i == 0:
            b[i] += 1
            j += i
        else:
            j += 1

print(b[2:])


