from turtle import *

k = 50  # коэффициент для масштаба

tracer(0)  # отключение анимаций и размер окна
screensize(3000, 3000)


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
