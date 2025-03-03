from turtle import *

k = 50

tracer(0)
screensize(3000, 3000)


for n in range(10):
    right(30)
    forward(4*k)
    right(60)


penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, 'blue')

done()