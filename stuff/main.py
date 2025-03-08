twos = [2**n for n in range(0, 20)]
res = []

for j in range(65, 100):
    for n in range(1, j):

        s = '0' + '1' * n + '2' * (j-1-n)

        g = sum(int(i) for i in s)

        while ('01' in s) or ('02' in s):
            s = s.replace('02', '110', 1)
            s = s.replace('01', '2120', 1)

        if sum(int(i) for i in s) in twos:
            print(j, n)
            res.append(g)

print(min(res))