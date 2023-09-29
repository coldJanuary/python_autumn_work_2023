# ****** TASK 1 ******

from math import factorial as f

N = int(input())

for n in range(N + 1):
    for k in range(N + 1):
        if n - k >= 0:
            if k == 0:      #для красивого вывода
                print(' ' * (N - n), end=' ')
            print(int(f(n) / (f(k) * (f(n - k)))), end=' ')
    print()




# ****** TASK 2 ******

def is_prime(a):  #функция проверяет на простоту
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k += 1
    if k == 0:
        return True
    else:
        return False


n = int(input())
N = n  # для красивого вывода
d = {} # словарь заполняем так:
# ключ - основание степени простого делителя, значение - показатель его степени

for i in range(2, n // 2 + 1):
    if is_prime(i):
        while n % i == 0:
            d[i] = d.get(i, 0) + 1
            n = int(n / i)

#print(d)

print(N, end=' = ')
s = ''
for i in d:
    s = s + f'{i}^{d[i]} * '
print(s[:-2])




# ****** TASK 3 ******

n = int(input())
lst = [1, 1]
for i in range(n - 2):
    lst.append(lst[-2] + lst[-1])

# print(lst)

for i in range(len(lst)):
    lst[i] = str(lst[i]) + ','
lst[-1] = lst[-1][:-1]
print(*lst)
