import sys

sys.setrecursionlimit(1000000000)

def f(n):
    if n <= 1:
        return 3
    else:
        return f(n-1) + 2 * f(n-2) - 5

print(f(100))