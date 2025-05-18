def ss(n, b):  # функция перевода в системы счисления
    res = []
    while n:
        res.append(n % b)
        n //= b
    return res[::-1]


for x in range(100):
    f1 = 37**3 + 2 * 37**2 + 3 * 37 + x  # перевод в десятичную из любой
    f2 = 4 * 37**3 + x * 37**2 + 5 * 37 + 9

    res = f1 + f2

    if res % 36 == 0:
        print(x, res // 36)
