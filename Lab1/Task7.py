"""Draw square spiral"""

import turtle


def square_spiral(length):
    default_length = length
    n = 0
    while True:
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        length = length + default_length
        if n == 40:
            break

square_spiral(10)
