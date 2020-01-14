#/usr/bin/env python3
'''
__author__ = ' abba y abdullahi,abbayabdullahi68@gmail.com'
'''
import turtle


""" Provides the plot function that draws the graph of a mathematical
function on a Cartesian coordinate plane. """


def initialize_plotter(width, height, min_x, max_x, min_y, max_y):
    """Initializes the plotter with a window with dimensions
width x height, the x-axis ranging from
min_x to max_x, and the y-axis ranging from
min_y to max_y. Establishes the global beginning and ending
x values for the plot and the global x_increment value.
Draws the x- and y-axes. """
    global x_begin, x_end, x_increment
    turtle.delay(0)
    x_begin, x_end = min_x, max_x
    turtle.setup(width=width, height=height)
    turtle.screensize(width, height)
    turtle.setworldcoordinates(min_x, min_y, max_x, max_y)
    x_increment = (max_x - min_x)/width
    turtle.hideturtle()
    turtle.pencolor('black')
    turtle.penup()
    turtle.setposition(min_x, 0)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(max_x - min_x)
    turtle.penup()
    turtle.setposition(0, min_y)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(max_y - min_y)
   

def plot(f, color):
    """ Plots function f on the Cartesian coordinate plane
established by initialize_plotter. Plots (x, f(x)),
for all x in the range x_begin <= x < x_end.
The color parameter dictates the curve's color. """
    turtle.penup()
    turtle.setposition(x_begin, f(x_begin))
    turtle.pencolor(color)
    turtle.pendown()
    x = x_begin
    while x < x_end:
        turtle.setposition(x, f(x))
        x += x_increment


def finish_plotting():
    turtle.exitonclick()
    

def quad(x):
    return 1/2 * x**2 + 3
    

def main():
    """ Provides a simple test of the plot function. """
    from math import sin
    initialize_plotter(600, 600, -10, 10, -10, 10)
    plot(quad, 'red')
    plot(lambda x: x, 'blue')
    plot(lambda x: 3*sin(x), 'green')
    finish_plotting()

if __name__ == '__main__':
    main()
