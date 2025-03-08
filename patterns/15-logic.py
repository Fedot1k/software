for A in range(3000):
    valid = True
    
    for x in range(10000):
        for y in range(10000):
            f = (x*y < A) or (x < y) or (9 < x)
            if f == 0:
                valid = False
                break
            
        if not valid:
            break

    if valid:
        print(A)