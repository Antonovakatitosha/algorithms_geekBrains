start = 32
end = 127

for i in range(start, end + 1, 10):
    for j in range(0, 10):
        if i + j > end: break
        print(f'{i + j}: "{chr(i + j)}"', end=', ')

    print()
