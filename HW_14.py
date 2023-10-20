# **************** TASK 1 ****************

def len_of_number(n):
    if n//10 == 0:
        return 1
    else:
        return 1 + len_of_number(n//10)

# **************** TASK 2 ****************

def sum_of_digits(n):
    if n//10 == 0:
        return n
    else:
        return n%10 + sum_of_digits(n//10)

# **************** TASK 3 ****************

def tri_2(n):
    if n == 1:
        print('*')
    else:
        print(n*'*')
        tri_2(n-1)
    if n != 1:
        print(n*'*')