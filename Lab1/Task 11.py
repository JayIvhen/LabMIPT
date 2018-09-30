"""Draw spring"""

import turtle


def spring(loop_count, radius, n=0):
    turtle.seth(90)
    if n != loop_count:
        turtle.circle(-radius, 180)
        turtle.circle(-radius/3, 180)
        spring(loop_count, radius, n+1)
    else:
        turtle.circle(-radius, 180)


spring(5, 20)
