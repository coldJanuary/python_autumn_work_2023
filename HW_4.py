# ****** TASK 1 ******

q = input().split()
q[0], q[2] = int(q[0]), int(q[2])

d = {'+': q[0]+q[2],
     '-': q[0]-q[2],
     '*': q[0]*q[2],
     '/': q[0]/q[2]}

print(d[q[1]])



# ****** TASK 2 ******

n = int(input())

max_len = len(str(n * n))  # для красивого вывода вконце

mas = [[0] * n for i in range(n)]
x = -1  # текущие координаты
y = 0
d_hor = 1  # горизонтальное движение. Также 0 и -1
d_ver = 0  # вертикальное движение. Также 0 и -1

i = 1
while i <= n * n:
    if 0 <= x + d_hor < n and 0 <= y + d_ver < n and mas[y + d_ver][x + d_hor] == 0:
        mas[y + d_ver][
            x + d_hor] = i  # когда мы упремся в край или на ненулевое значение, надо менять направление движения:
        x += d_hor
        y += d_ver
        i += 1
    else:
        if d_hor == 1:
            d_hor = 0
            d_ver = 1
        elif d_ver == 1:
            d_ver = 0
            d_hor = -1
        elif d_hor == -1:
            d_hor = 0
            d_ver = -1
        elif d_ver == -1:
            d_ver = 0
            d_hor = 1

for i in mas:
    for j in i:
        print(str(j).rjust(max_len), end=' ')
    print()



# ****** TASK 3 ******

import string

sen1 = input()
sen2 = input()
d1 = {}
d2 = {}

for i in sen1:
    if i not in string.punctuation and i != ' ':
        d1[i] = d1.get(i, 0) + 1
for i in sen2:
    if i not in string.punctuation and i != ' ':
        d2[i] = d2.get(i, 0) + 1

print(d1 == d2)

