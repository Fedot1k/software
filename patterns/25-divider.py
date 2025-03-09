def div(n): # функция получения делителей, <range(1, int(n**0.5 + 1))> для всех делителей
    return sorted(list({i for i in range(2, int(n**0.5 + 1)) if n%i==0} | {n//i for i in range(2, int(n**0.5 + 1)) if n%i==0}))


def prime(n): # функция определения простого числа
    return n > 1 and all([n%i!=0 for i in range(2, int(n**0.5) + 1)])


for n in range(112500000, 112550001):
    divs = div(n)
    if len(divs) >= 2 and (divs[-1] + divs[-2]) % 10000 == 1214:
        print(n)
