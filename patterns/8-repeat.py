from itertools import product

cnt = 0

for x in product('0123456789ABCDE', repeat=5):  # повторяющиеся символы, repeat = количество символов

    s = ''.join(x)

    amount = s.count('A') + s.count('B') + s.count('C') + s.count('D') + s.count('E')

    if (s[0] != '0') and (s.count('8') == 1) and (amount >= 2):
        cnt += 1

print(cnt)
