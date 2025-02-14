with open('stuff/task.txt', 'r') as file:
    lines = file.readlines()

big = [list(map(int, line.split())) for line in lines]

for row in range(len(big)):
    if len(set(big[row])) == 5:
        repet = [x for x in big[row] if big[row].count(x) > 1][0]
        other = [x for x in big[row] if x != repet]
        sredne = sum(other) / 4
        if repet >= sredne:
            print(row)
            break