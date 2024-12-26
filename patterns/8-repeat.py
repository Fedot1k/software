from itertools import *

cnt = 0

for x in product('ГЕНОСТХЮ', repeat = 4): # повторяющиеся символы
    cnt += 1
    s = ''.join(x)
    if (s[0] != 'Н') and (s.count('О') >= 2) and ('С' not in s) and (cnt % 2!= 0):
        print(cnt)

