import math

with open('stuff/27-coordinate.txt') as file:
    file.readline()

    cluster1, cluster2 = [], []  # распределение точек по кластерам через координаты из графика таблицы
    for i in file:
        x, y = map(float, i.replace(',', '.').split())

        if -2 <= x <= 1 and 0 <= y <= 3:
            cluster1.append((x, y))
        if 1 <= x <= 5 and 3 <= y <= 7:
            cluster2.append((x, y))


def centroid(cluster):  # функция нахождения центроида кластера
    xCentre, yCentre, minim = 0, 0, 10**10

    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            res += math.dist(cluster[i], cluster[j])

        if res < minim:
            minim = res
            xCentre, yCentre = cluster[i]

    return xCentre, yCentre


x1, y1 = centroid(cluster1)
x2, y2 = centroid(cluster2)

print((x1 + x2) / 2 * 10000, (y1 + y2) / 2 * 10000)
