# Версия python 3.8, разрядность системы 64x
#
#
# start – 24 bit
# end – 24 bit
# i – 24 bit
# j – 24 bit
#
# суммарно 56 bit, если под цикл не выделяется память, range итератор, как я поняла

start = 32
end = 127

for i in range(start, end + 1, 10):
    for j in range(0, 10):
        if i + j > end: break
        print(f'{i + j}: "{chr(i + j)}"', end=', ')

    print()
