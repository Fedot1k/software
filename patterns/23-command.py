def f(s, x):
    if x == 1001:
        res.append(s)
        return 1

    return f(s + 2, x + 1) + f(s + 4, x + 1) + f(s + 5, x + 1) # возможные действия

print(f(31, 0))

print(res)

