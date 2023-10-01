#   ********** TASK 1 **********

def from_roman_to_arabic(rom):
    rom = rom.replace('IV', '4 ')
    rom = rom.replace('IX', '9 ')
    rom = rom.replace('XL', '40 ')
    rom = rom.replace('XC', '90 ')
    rom = rom.replace('CD', '400 ')
    rom = rom.replace('CM', '900 ')
    rom = rom.replace('I', '1 ')
    rom = rom.replace('V', '5 ')
    rom = rom.replace('X', '10 ')
    rom = rom.replace('L', '50 ')
    rom = rom.replace('C', '100 ')
    rom = rom.replace('D', '500 ')
    rom = rom.replace('M', '1000 ')

    rom = list(map(int, rom.split()))

    return sum(rom)




#   ********** TASK 2 **********

s1 = set(input().split(', '))
s2 = set(input().split(', '))

print(len(s1 & s2))




#   ********** TASK 3 **********

import string

s = list(set(input()))

for i in s:
    if i in string.ascii_lowercase:
        print(i, end = ' ')
print()
for i in s:
    if i in string.digits:
        print(i, end = ' ')
print()
for i in s:
    if i in string.punctuation:
        print(i, end = ' ')