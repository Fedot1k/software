def ss(n, b):
    res = []
    while n:
        res.append(n%b)
        n //= b
    return ''.join(str(x) for x in res[::-1])


for p in range(9, 20):
    for x in ('0123456789ABCDEFGHIJ'):
        for y in ('0123456789ABCDEFGHIJ'):
            f1 = y + '2' + y
            f2 = y + '87'
            f3 = '1' + x + x
            try: 
                if (int(f1, p) + int(f2, p)) == int(f3, p):
                    print(x, y, p)
            except:
                pass

