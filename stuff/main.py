def f(s, k, last):
    if s == k:
        return 1
    if s > k+1 or s % 10 == 0:
        return 0
    return (0 if last else f(s-1, k, True)) + f(s+2, k, False) + f(s*3, k, False)

print(f(5, 32, False) * f(32, 62, False))