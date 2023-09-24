# более сложный вариант: прог. выводит все слова
# наибольшей длины, если их несколько
s = input().split()

# сортировка пузырьком:
for i in range(len(s) - 1):
    for j in range(len(s) - i - 1):
        if len(s[j]) > len(s[j + 1]):
            s[j], s[j + 1] = s[j + 1], s[j]

max_len = len(s[-1])
while len(s[-1]) == max_len:
    print(s.pop(-1))
