# *********** TASK 1 ***********

def nok(list_of_numbers):
    # принимает список чисел, возвращает их НОК

    def number_spliter(n):
        # раскладывает число на простые множители
        d = {}
        while n != 1:
            for i in range(2, n + 1):
                if n % i == 0:
                    d[i] = d.get(i, 0) + 1
                    n = int(n / i)
                    break
        return d

    q = {}
    for i in list_of_numbers:
        d = number_spliter(i)
        for i in d:
            q[i] = max(d[i], q.get(i, 0))
    m = 1
    for i in q:
        m = m * (i ** q[i])
    return m




# *********** TASK 2 ***********

def code(string, n):
    new_string = ''
    for i in string:
        if i.isalpha():
            if ord(i.lower()) + n % 26 > ord('z'):
                q = 1
            else:
                q = 0
            new_string += chr(ord(i) + n % 26 - 26 * q)
        else:
            new_string += i

    return new_string




# *********** TASK 3 ***********

def three_biggest_from_array(arr):
    lst = []
    for i in arr:
        for j in i:
            lst.append(j)

    return sorted(lst)[-3:]
