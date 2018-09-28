"""Draw spider with n-legs"""

import itertools
import math

import turtle


def spiral():
    for angle, radius in zip(itertools.cycle(range(1,361, 2)), itertools.count(1, step=0.1)):
        print("({},{})".format(angle, radius))
        next_x = radius * math.cos(math.radians(angle))
        next_y = radius * math.sin(math.radians(angle))
        print("next x: ", next_x)
        print("next y: ", next_y)
        print("POS", turtle.pos())
        turtle.goto(next_x, next_y)
        if angle == 1000:
            break

spiral()
