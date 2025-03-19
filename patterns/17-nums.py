with open('stuff/17-range.txt') as file:
    big = list(map(int, file))

res = []

maxElem = max([x for x in big if x%10==7])


for n in range(len(big) - 2):
    three = [big[n], big[n+1], big[n+2]]

    first = [int(str(abs(x))[0]) for x in three]
    second = [x for x in three if len(str(abs(x))) == 3 and str(abs(x))[-1] == '7']

    if len(set(first)) == 1 and len(second) >= 1 and abs(sum(three)) < maxElem:
        res.append(abs(sum(three)))

print(len(res), max(res))