"""" Draw 10 square one in another"""

import turtle

def n_angle(angles, side_length):
    rotate = 360 / angles
    n = 0
    while n < angles:
        turtle.forward(side_length)
        turtle.left(rotate)
        n += 1


def main(count, angles, side_length, space):
    n = 0
    while count>n:
        turtle.penup()
        turtle.goto(turtle.pos()[0] - space, turtle.pos()[1] - space)
        turtle.pendown()
        n_angle(angles, side_length)
        n += 1
        side_length = side_length + space*2

main(12, 4, 10, 5)