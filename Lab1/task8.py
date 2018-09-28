"""Draw n n-angles"""

import itertools
import math

import turtle


def n_angle(n, radius):
    angles = []
    angles.append(math.radians(0))
    segment = 360/n
    for i in range(1, n):
        angles.append(math.radians(segment * i))
    angles.append(math.radians(0))
    print(angles)
    x = radius * math.cos(angles[0])
    y = radius * math.sin(angles[0])
    turtle.penup()
    turtle.goto(x, y)
    turtle.pd()
    for angle in angles:
        next_x = radius * math.cos(angle)
        next_y = radius * math.sin(angle)
        turtle.goto(next_x, next_y)


def main(n, radius, increment):
    for i in range(3, n+4):
        n_angle(i, radius)
        radius = radius + increment

main(5, 20, 15)