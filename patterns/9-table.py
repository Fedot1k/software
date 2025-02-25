with open('stuff/task.txt') as file: # получение данных из текста
    lines = file.readlines()

table = [list(map(int, line.split())) for line in lines] # table = двумерный список из строчек с числами


for row in range(len(table)):
    if len(set(table[row])) == 5:

        repet = [x for x in table[row] if table[row].count(x) > 1][0]
        other = [x for x in table[row] if x != repet]

        avg = sum(other) / 4

        if repet >= avg:
            print(row)
            break