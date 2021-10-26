import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
x = 1
list = []
m = m-1 # т.к делаем на 1 шаг меньше
for i in range(n):
    list.append(i+1)
for _ in iter(int, 1):
    pass
    print(x, end='')
    x = 1 + (m + x - 1) % n
    if x == 1:
        break