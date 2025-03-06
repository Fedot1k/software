from ipaddress import *

net = ip_network('216.130.64.0/255.255.192.0')

res = 0

for ip in net:
    x = str(ip).split('.')

    if all([int(n)%2==0 for n in x]):
        res += 1

print(res)