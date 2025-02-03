from functools import lru_cache

@lru_cache(None)

def f(n):
    if n == 1:
        return 1
    if n > 0:
        return f(n-1) * n

print(f(15))



