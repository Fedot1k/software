from turtle import *

k = 20

tracer(0)

for n in range(2):
    forward(8 * k)
    right(90)
    forward(18 * k)
    right(90)

penup()

forward(4 * k)
right(90)
forward(10 * k)
left(90)

pendown()

for n in range(2):
    forward(17 * k)
    right(90)
    forward(7 * k)
    right(90)

penup()

for x in range(-500, 500, k):
    for y in range(-500, 500, k):
        goto(x, y)
        dot(3)

done()