for n in range(1, 1000):
    
    st = bin(n)[2:]
    
    if st.count('1') % 2 == 0:
        x = '10' + st[2:] + '0'
    else:
        x = '11' + st[2:] + '1'

    if int(x, 2) > 40:
        print(n)
        break