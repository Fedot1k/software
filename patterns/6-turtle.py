from turtle import *

screensize(3000, 3000)
tracer(0)  # отключение анимаций и размер окна

left(90)  # направление по оси Y

k = 50  # коэффициент для масштаба


for n in range(10):
    right(30)
    forward(4 * k)
    right(60)


penup()
for x in range(-50, 50):  # точки на координатах
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5, 'blue')

done()
