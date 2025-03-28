from ipaddress import *

net = ip_network('216.130.64.0/255.255.192.0', strict=False)

res = 0

for ip in net:
    x = bin(int(ip))[2:]

    if x.count('1') > x.count('0'):
        res += 1

print(res)
