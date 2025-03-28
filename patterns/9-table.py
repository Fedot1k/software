with open('stuff/9-data.txt') as file:  # получение данных из текста
    lines = file.readlines()

big = [list(map(int, line.split())) for line in lines]  # table = двумерный список из строчек с числами


for row in range(len(big)):
    if len(set(big[row])) == 5:

        repet = [x for x in big[row] if big[row].count(x) > 1][0]
        other = [x for x in big[row] if x != repet]

        avg = sum(other) / 4

        if repet >= avg:
            print(row)
            break
