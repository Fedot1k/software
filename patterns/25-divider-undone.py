def div(n): # функция получения делителей, <range(1, int(n**0.5 + 1))> для всех делителей
    return sorted(list({i for i in range(2, int(n**0.5 + 1)) if n%i==0} | {n//i for i in range(2, int(n**0.5 + 1)) if n%i==0}))

def prime(n): # функция определения простого числа
    return n > 1 and all([n%i!=0 for i in range(2, int(n**0.5) + 1)])

print(prime(43), div(54))
