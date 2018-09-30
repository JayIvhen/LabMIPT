"""Draw butterfly"""

import turtle


def butterfly(n_wings, start_radius, increment=5, n=0):
    turtle.seth(90)
    if n != n_wings:
        turtle.circle(start_radius)
        turtle.circle(-start_radius)
        butterfly(n_wings, start_radius+increment, increment, n+1)
    else:
        pass


butterfly(10, 10)
