# используем метод строки count:
n = input()

for i in range(10):
    print(f'{i} - {n.count(str(i))}')



# словарем:
# alphabet = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
# n = int(input())
#
# while n != 0:
#     alphabet[n % 10] += 1
#     n = n // 10
#
# for i in alphabet:
#     print(f'{i} - {alphabet[i]}')
