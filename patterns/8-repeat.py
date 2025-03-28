from itertools import product

cnt = 0

for one in product('0123456789ABCDE', repeat=5):  # повторяющиеся символы, repeat = количество символов

    text = ''.join(one)

    amount = text.count('A') + text.count('B') + text.count('C') + text.count('D') + text.count('E')

    if (text[0] != '0') and (text.count('8') == 1) and (amount >= 2):
        cnt += 1

print(cnt)
