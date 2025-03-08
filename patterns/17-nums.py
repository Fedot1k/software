with open('18-7.txt', 'r') as f:
    num = [int(i) for i in f.readlines()]

res = 0

for x in range(len(num)):
    for y in range(1, 7):
        try:
            g = num[x] + num[x+y]
            if g%2==0:
                res += 1
        except:
            continue

print(res)