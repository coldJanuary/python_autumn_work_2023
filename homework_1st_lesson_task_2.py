x, y = map(int, input().split())  # пользователь вводит два числа через пробел
print(max(x+y, x-y, x*y, x/y, x//y))
