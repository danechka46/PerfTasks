import sys
list = []
file = sys.argv[1]
'''Заполняем список и сортируем по возрастанию'''
with open(f'{file}','r') as file:
    for i in file:
        list.append(int(i))
sort_array = sorted(list)
'''Находим значение в центре к которому будем приводить значения'''
x = sort_array[len(list)//2]
'''Заводим счетчик кол-ва шагов'''
count = 0
for i in sort_array:
    '''Считаем шаги по модулю, чтобы не было отрицательного числа в сумме'''
    count+= abs(i - x)
print(count)
