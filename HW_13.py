# ********************** TASK 1 **********************

def plus_minus():
    n = 1
    while True:
        yield ((-1) ** (n + 1)) * n
        n += 1


pm = plus_minus()

lst = []
for i in range(20):  # range(длина ряда)
    lst.append(str(next(pm)))
print(', '.join(lst))



# ********************** TASK 2 **********************

def array_of_palindroms():
    n = 1
    while True:
        N = str(n)
        if len(N) == 1:
            yield n
        if len(N)%2 == 0:
            if N[:int(len(N)/2)] == N[:int(len(N)/2)-1:-1]:
                yield n
        else:
            if N[:len(N)//2+1] == N[:len(N)//2-1:-1]:
                yield n
        n += 1

ap = array_of_palindroms()

for i in range(100):        #range(кол-во чисел)
    print(next(ap), end=' ')

# ********************** TASK 3 **********************

def odds_from_numbers(lst):
    for i in range(len(lst)):
        if i%2:
            yield i

ofn = odds_from_numbers(list(range(20))) #например

for i in ofn:
    print(i, end=' ')