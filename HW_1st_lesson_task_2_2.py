lst = [5, 67, -6, 42, 235, -678, 0, 6, 8, 88]
lst_min = lst[0]
for i in lst:
    if i < lst_min:
        lst_min = i
print(lst_min)