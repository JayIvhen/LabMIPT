"""Draw flower"""

import turtle

def flower(n_pairs, radius):
    angle = round(360/(n_pairs*2))
    for i in range(n_pairs):
        turtle.circle(radius)
        turtle.circle(-radius)
        turtle.seth(angle)
        angle = angle + round(360/(n_pairs*2))

flower(3, 40)