"""Draw spider with n-legs"""

import turtle

def spider(legs, length):
    degree_ = 360 / legs
    n = 0
    while n<legs:
        turtle.seth(degree_)
        turtle.forward(length)
        turtle.stamp()
        turtle.backward(length)
        degree_ = degree_ + 360/legs
        print(degree_)
        n += 1


spider(12, 50)