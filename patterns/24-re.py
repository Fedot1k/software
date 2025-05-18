from re import findall

s = open('stuff/24-express.txt').readline()

res = findall(r'(?:0|[1-9][0-9]*)(?:[+*](?:0|[1-9][0-9]*))*', s)  # корректные выражения

print(max([len(x) for x in res]))
