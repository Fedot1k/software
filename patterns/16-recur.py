from functools import lru_cache

@lru_cache(None)


def f(n, m):
    if m > n:
        return 0
    elif m <= n and n%m==0:
        return 1 + f(n, m+1)
    elif m <= n and n%m!=0:
        return f(n, m+1)


print(f(107864, 3))



