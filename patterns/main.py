s = '0' + '1' * 122 + '2' * 41 + '0'

while ('00' not in s):
    s = s.replace('02', '101', 1)
    s = s.replace('11', '2', 1)
    s = s.replace('012', '30', 1)
    s = s.replace('010', '00', 1)

print(sum([int(i) for i in s if i != '>']))