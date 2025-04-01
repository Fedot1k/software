print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = z <= (x == (w <= y))  # выражение из задания
                if f == 0:
                    print(x, y, z, w, '=', int(f))
