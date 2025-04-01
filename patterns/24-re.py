from re import findall

s = open('stuff/24-express.txt').readline()

check = findall(r'(?:0|[1-9][0-9]*)(?:[+*](?:0|[1-9][0-9]*))*', s)  # корректные выражения

res = [len(x) for x in check]

print(max(res))
