from collections import namedtuple
n = int(input("Задайте количество предприятий: "))
enterprise_type = namedtuple('enterprise', ['title',  'average'])
enterprises = set()
global_average = 0

for i in range(n):
    title = input("Введите название: ")
    average = round(sum(map(int, input("Введите прибыль через пробел: ").split()))/4, 2)
    global_average += average
    enterprises.add(enterprise_type(title=title, average=average))

global_average = round(global_average/n, 2)
print(f'\nПредприятия, чья прибыль больше {global_average}')
for enterprise in list(enterprises):
    if enterprise.average > global_average:
        print(enterprise.title, end=' ')
        enterprises.remove(enterprise)

print(f'\nПредприятия, чья прибыль меньше {global_average}')
for enterprise in enterprises: print(enterprise.title, end=' ')
