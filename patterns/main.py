with open('stuff/task.txt') as file:
    lines = file.readlines()

big = [list(map(int, l.split())) for l in lines]

for row in big:
    repet = [x for x in row if row.count(x) == 2]
    if len(repet) == 4 and max(row) not in repet:
        print(row)
        break