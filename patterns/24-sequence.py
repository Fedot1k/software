s = open('stuff/24-sequence.txt').readline().split('T')

maxi = 0

for i in range(len(s) - 100):
    r = 'T'.join(s[i:i+100]) + 'T'
    maxi = max(maxi, len(r))

print(maxi)
