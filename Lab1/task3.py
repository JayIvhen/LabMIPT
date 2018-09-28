"""Draw circle"""

import turtle

def n_angle(angles, side_length):
    rotate = 360 / angles
    n = 0
    while n < angles:
        turtle.forward(side_length)
        turtle.right(rotate)
        n += 1

n_angle(500, 2)