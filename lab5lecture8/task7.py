"""
dragon curve
"""

import turtle as T
import math

LENGTH = 300
N = 10


def dragon_curve(len_, n):
    draw_right(len_, n)


def draw_right(len_, n):
    if n == 0:
        T.forward(len_)
        print(n)
        return
    T.right(45)
    draw_right(math.sqrt(len_ ** 2 / 2), n - 1)
    T.left(90)
    draw_left(math.sqrt(len_ ** 2 / 2), n - 1)
    T.right(45)


def draw_left(len_, n):
    if n == 0:
        T.forward(len_)
        print(1, n)
        return
    T.left(45)
    draw_right(math.sqrt(len_ ** 2 / 2), n - 1)
    T.right(90)
    draw_left(math.sqrt(len_ ** 2 / 2), n - 1)
    T.left(45)


if __name__ == "__main__":
    T.speed(0)
    dragon_curve(LENGTH, N)
