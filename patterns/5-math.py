for n in range(1, 1000):

    x = bin(n)[2:]

    if x.count('1') % 2 == 0:
        x = '10' + x[2:] + '0'
    else:
        x = '11' + x[2:] + '1'

    if int(x, 2) > 40:
        print(n)
        break
