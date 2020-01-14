#usr/bin/env python3 
'''
__author__ = ' abba y abdullahi, abbayabdullahi68@gmail.com'
'''

import random
import turtle


def polygon(sides, length, x, y, color):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360//sides)
    turtle.end_fill()

turtle.hideturtle()
turtle.tracer(0)
for i in range(120):
    polygon(random.randrange(3, 11), random.randrange(10, 51),
random.randrange(-250, 251), random.randrange(-250, 251),
random.choice(("red", "green", "blue", "black", "yellow")))


turtle.update()
turtle.exitonclick()

