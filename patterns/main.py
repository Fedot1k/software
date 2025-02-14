with open('task-7.txt', 'r') as file:
    lines = file.readlines()

big = [list(map(int, l.split())) for l in lines]

for row in range(len(big)):
    if len(set(big[row])) == 5:
        repet = [x for x in big[row] if big[row].count(x) > 1]
        if max(repet) != max(big[row]) and len(repet) == 4:
            print(row)
            break

print(sum(big[786]))