# ******************** TASK 1 ********************

def indexes_of_extremums(lst):
    maxi, mini = [], []
    for i, j in enumerate(range(len(lst))):
        if lst[i] == max(lst): maxi.append(i)
        if lst[i] == min(lst): mini.append(i)

    return mini, maxi




# ******************** TASK 2 ********************

q = [x for y in range(1,11) for x in [y]*y]



# ******************** TASK 3 ********************

def numbers_from_range(s):
    q = []
    s = map(lambda x: x.split('-'), s.split(','))
    for i in s:
        q += [x for x in range(int(i[0]), int(i[1]) + 1)]

    return q

