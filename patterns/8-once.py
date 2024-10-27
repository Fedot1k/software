from itertools import *

cnt = 0

for x in permutations('01234567', 6):
    s = ''.join(x)
    b = s.replace('1', '*').replace('3', '*').replace('5', '*').replace('7', '*').replace('0', '#').replace('2', '#').replace('4', '#').replace('6', '#')
    if s[0] != '0' and len(set(s)) == len(s) and '**' not in b and '##' not in b:
        cnt += 1

print(cnt)