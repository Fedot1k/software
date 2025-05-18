from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 0:
        return f(n - 1) * n


for n in range(1, 2000):  # оптимизация через кэширование
    f(n)

print(f(15))
