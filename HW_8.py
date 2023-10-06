# ************** TASK 1 **************

s = input()
s = s.replace('АГ', 'ГА')
s = s.replace('ЦТ', 'ЦАГТ')

print(s)



# ************** TASK 2 **************

def sor(a):
    return len(a)

lst = eval((input()))

for i in range(len(lst)):
    lst[i] = sorted(lst[i], reverse=True)

print(sorted(lst, key = sor))



# ************** TASK 3 **************

q = eval(input())

def ss(s):
    return (-len(set(s)), s)

print(sorted(q, key=ss))
