# **************** TASK 1 ****************

def dnk_to_rnk(s):
    d = {'G': 'C',
         'C': 'G',
         'T': 'A',
         'A': 'T'}
    return ''.join(map(lambda x: d[x], s))




# **************** TASK 2 ****************

vowels = 'ауоыиэяюеё'
d = []

main_word = list(map(lambda x: 1 if x in vowels else 0, input()))
for i in range(int(input())):
    maybe_similar = input()
    maybe = list(map(lambda x: 1 if x in vowels else 0, maybe_similar))
    if (0, 1) not in list(zip(main_word, maybe)) and (1, 0) not in list(zip(main_word, maybe)):
        d.append(maybe_similar)

print(*d)




# **************** TASK 3 ****************

s = input().lower()
d = {}

for i in s:
    d[i] = d.get(i, 0) + 1

for i in sorted(list(d.items())[0:10], key=lambda x: -x[1]):
    print(f'{i[0]} - {i[1]}')
