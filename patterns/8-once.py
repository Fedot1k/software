from itertools import permutations

cnt = 0

for x in set(permutations('01234567', 6)): # неповторяющиеся символы

    text = ''.join(x)

    new = text.replace('1', '*').replace('3', '*').replace('5', '*').replace('7', '*').replace('0', '#').replace('2', '#').replace('4', '#').replace('6', '#')

    if (text[0] != '0') and (len(set(text)) == len(text)) and ('**' not in new) and ('##' not in new):
        cnt += 1

print(cnt)