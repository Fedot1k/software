def div(n):
    return sorted(set([x for i in range(2, int(n**0.5) + 1) if n % i == 0 for x in (i, n // i)]))

def prime(n):
    return n > 1 and all([n%i!=0 for i in range(2, int(n**0.5) + 1)])

print(prime(12), div(12))
