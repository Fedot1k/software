from fnmatch import *

for i in range(1756, 10**8, 1756):
    if fnmatch(str(i), '12*45*3'):  # проверка чисел через цикл
        print(i, i // 1756)
