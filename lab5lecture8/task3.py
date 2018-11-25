"""
recursive koch curve
"""

import turtle as T

def draw_koch(l, n):
    if n == 0:
        T.forward(l)
        return
    draw_koch(l / 3, n - 1)
    T.left(60)
    draw_koch(l / 3, n - 1)
    T.right(120)
    draw_koch(l / 3, n - 1)
    T.left(60)
    draw_koch(l / 3, n - 1)


if __name__ == "__main__":
    T.speed(0)
    draw_koch(300, 1)
