x, y = map(int, input().split())  # пользователь вводит два числа через пробел
l = [x+y, x-y, x*y, x/y, x//y]
l = sorted(l)
print(l[-2])
