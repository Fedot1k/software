def f(s, k):
    if s == k: return 1
    if s > k: return 0
    return f(s + 1, k) + f(s * 2, k) # возможные действия

print(f(1, 24)) # s - начало, k - конец