with open('stuff/17-1.txt') as file:
    big = list(map(int, file))

res = []

maxElem = max([x for x in big if x % 111 == 0])


for n in range(len(big) - 1):
    if (big[n] > maxElem or big[n + 1] > maxElem) and (big[n] % 10 == 7 or big[n + 1] % 10 == 7):
        res.append(big[n] + big[n + 1])

print(len(res), min(res))
